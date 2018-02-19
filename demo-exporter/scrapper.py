#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time


def scrapper(config, data, sleep=30):
    """
    Scrape data from some source
    """
    while True:
        for m in config['metrics']:
            line = "{n}{{dimensions=\"{d}\",region=\"{r}\"}}".format(
                n=m['aws_metric_name'],
                d=",".join(m['aws_dimensions']),
                r=config['region'])
            data[line] = random.randint(1, 420) / 100.0

        # sleep for 30 sec
        time.sleep(sleep)
