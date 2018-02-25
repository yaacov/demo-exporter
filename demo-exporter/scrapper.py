#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
from datetime import datetime


def scrapper(config, data, sleep=30):
    """
    Scrape data from some source
    """
    while True:
        for m in config['metrics']:
            dp = [
                {
                    "Timestamp": datetime.utcnow(),
                    "Maximum": random.randint(1, 420) / 100.0,
                    "Unit": "Percent"
                },
            ]

            d = dp[0]
            line = "{n}{{unit=\"{u}\",region=\"{r}\"}}".format(
                n=m['aws_metric_name'],
                u=d['Unit'],
                r=config['region'])
            data[line] = d['Maximum']

        # sleep for 30 sec
        time.sleep(sleep)
