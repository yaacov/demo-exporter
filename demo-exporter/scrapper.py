#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
from datetime import datetime
from helpers import get_dimensions_str, convert


def scrapper(config, data, sleep=30):
    """
    Scrape data from some source
    """
    while True:
        for metric in config['metrics']:
            response = {
                'Datapoints': [
                    {
                        "Timestamp": datetime.utcnow(),
                        metric['aws_statistics'][0]:
                            random.randint(1, 420) / 100.0,
                        "Unit": "Percent"
                    },
                ]
            }

            dp = response['Datapoints']
            d = dp[-1]

            #  Example, create this line:
            #    aws_ebs_volume_read_bytes_maximum{volume_id="vol-035faf9767706322e"}
            #  from this config:
            #    aws_namespace: AWS/EBS
            #    aws_metric_name: VolumeReadBytes
            #    aws_dimensions: [VolumeId]
            #    aws_dimension_select:
            #      VolumeId: [vol-035faf9767706322e]
            #    aws_statistics: [Maximum]
            line = '{n}_{n}_{s}{{{u}}}'.format(
                ns=convert(metric['aws_namespace']),
                n=convert(metric['aws_metric_name']),
                s=convert(metric['aws_statistics'][0]),
                u=get_dimensions_str(metric['aws_dimension_select']))
            data[line] = d[metric['aws_statistics'][0]]

        # sleep for 30 sec
        time.sleep(sleep)
