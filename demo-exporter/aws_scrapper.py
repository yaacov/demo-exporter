#!/usr/bin/env python

import boto3
from datetime import datetime, timedelta


SECOUNDS = 300


def list_to_dimentions(ds):
    """
    convert a list of dimention strings to dimentions dicts
    """
    out = [{'Name': 'Dimension%d' % i, 'Value': d} for (i, d) in enumerate(ds)]
    return out


def scrapper(config, data, sleep=30):
    """
    Scrape metrics from AWS cloudwatch
    """
    c = boto3.client('cloudwatch', region_name=config['region'])

    while True:
        for metric in config['metrics']:
            print('INFO: Reading metric %s from aws_namespace %s' %
                  (metric['aws_metric_name'], metric['aws_namespace']))

            response = c.get_metric_statistics(
                Namespace=metric['aws_namespace'],
                MetricName=metric['aws_metric_name'],
                Dimensions=list_to_dimentions(metric['aws_dimensions']),
                StartTime=datetime.utcnow() - timedelta(seconds=SECOUNDS),
                EndTime=datetime.utcnow(),
                Period=SECOUNDS,
                Statistics=['Average', 'Minimum', 'Maximum'],
                Unit='Count'
            )

            dp = response['Datapoints']

            if len(dp) == 0:
                print('WARN: Empty metric %s in namespace %s' %
                      (metric['aws_metric_name'], metric['aws_namespace']))
            else:
                print('INFO: Metric %s in namespace %s:' %
                      (metric['aws_metric_name'], metric['aws_namespace']))

                print(dp)
