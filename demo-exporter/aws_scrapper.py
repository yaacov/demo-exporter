#!/usr/bin/env python

import time
import boto3
from datetime import datetime, timedelta


SECOUNDS = 300


def scrapper(config, data, sleep=30):
    """
    Scrape metrics from AWS cloudwatch
    """
    c = boto3.client('cloudwatch', region_name=config['region'])

    while True:
        # TODO:
        # Clear data, before each new scrape

        # Run a new scrape each "sleep" scoundes
        for metric in config['metrics']:
            print('INFO: Reading metric %s from aws_namespace %s [%s]' %
                  (metric['aws_metric_name'],
                   metric['aws_namespace'],
                   config['region']))

            response = c.get_metric_statistics(
                Namespace=metric['aws_namespace'],
                MetricName=metric['aws_metric_name'],
                StartTime=datetime.utcnow() - timedelta(seconds=SECOUNDS),
                EndTime=datetime.utcnow(),
                Period=SECOUNDS,
                Statistics=['Maximum']
            )

            dp = response['Datapoints']

            if len(dp) == 0:
                print('WARN: Empty metric %s in namespace %s [%s]' %
                      (metric['aws_metric_name'],
                       metric['aws_namespace'],
                       config['region']))
            else:
                print('INFO: Metric %s in namespace %s [%s]:' %
                      (metric['aws_metric_name'],
                       metric['aws_namespace'],
                       config['region']))

                # update data with new value
                d = dp[0]
                line = "{n}{{unit=\"{u}\",region=\"{r}\"}}".format(
                    n=metric['aws_metric_name'],
                    u=d['Unit'],
                    r=config['region'])
                data[line] = d['Maximum']

        # Wait "sleep" scounds
        time.sleep(sleep)
