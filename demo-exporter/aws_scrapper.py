#!/usr/bin/env python

import time
import boto3
from datetime import datetime, timedelta
from helpers import get_dimensions_str, get_dimensions, convert


def scrapper(config, data, sleep=30):
    """
    Scrape metrics from AWS cloudwatch
    """
    c = boto3.client('cloudwatch', region_name=config['region'])

    while True:
        # Run a new scrape each "sleep" scoundes
        for metric in config['metrics']:
            print('INFO: Reading metric %s from aws_namespace %s [%s]' %
                  (metric['aws_metric_name'],
                   metric['aws_namespace'],
                   config['region']))

            request_args = dict(
                Namespace=metric['aws_namespace'],
                MetricName=metric['aws_metric_name'],
                Dimensions=get_dimensions(metric['aws_dimension_select']),
                StartTime=(datetime.utcnow() -
                           timedelta(seconds=int(metric['range_seconds']))),
                EndTime=datetime.utcnow(),
                Period=60,
                Statistics=[metric['aws_statistics'][0]]
            )

            response = c.get_metric_statistics(**request_args)
            dp = response['Datapoints']

            #  Example, create this line:
            #    aws_ebs_volume_read_bytes_maximum{volume_id="vol-035faf9767706322e"}
            #  from this config:
            #    aws_namespace: AWS/EBS
            #    aws_metric_name: VolumeReadBytes
            #    aws_dimensions: [VolumeId]
            #    aws_dimension_select:
            #      VolumeId: [vol-035faf9767706322e]
            #    aws_statistics: [Maximum]
            line = '{ns}_{n}_{s}{{{u}}}'.format(
                ns=convert(metric['aws_namespace']),
                n=convert(metric['aws_metric_name']),
                s=convert(metric['aws_statistics'][0]),
                u=get_dimensions_str(metric['aws_dimension_select']))

            if len(dp) == 0:
                print('WARN: Empty metric %s in namespace %s [%s]' %
                      (metric['aws_metric_name'],
                       metric['aws_namespace'],
                       config['region']))

                # Clear data point
                if line in data:
                    del data[line]
            else:
                # Update data with new value
                # last value is the newset
                d = dp[-1]
                data[line] = d[metric['aws_statistics'][0]]

                print('INFO: Metric %s in namespace %s [%s]:' %
                      (metric['aws_metric_name'],
                       metric['aws_namespace'],
                       config['region']))

        # Wait "sleep" scounds
        time.sleep(sleep)
