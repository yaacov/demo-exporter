#!/usr/bin/env python

import re


def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name.replace('/', '_'))
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def get_dimensions(d):
    return [{"Name": k, "Value": v[0]} for (k, v) in d.items()]


def get_dimensions_str(d):
    return ",".join(["%s=\"%s\"" % (convert(k), v[0]) for (k, v) in d.items()])
