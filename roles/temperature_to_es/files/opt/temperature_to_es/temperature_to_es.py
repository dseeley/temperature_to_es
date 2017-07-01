#!/usr/bin/env python

from elasticsearch import Elasticsearch
import time
import datetime
import glob

import config

temp_sensor = glob.glob('/sys/bus/w1/devices/28-*')[0] + '/w1_slave'


def read_temp():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()

    temp_output = lines[1].find('t=')

    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c


def main():
    temp_c = read_temp()

    es = Elasticsearch([
        {'host': config.config['es_host'], 'port': config.config['es_port']}
    ])

    es.indices.create(index=config.config['es_index'], ignore=400, body= \
        { \
            'settings': { \
                'index.codec': 'best_compression', \
                'index.number_of_shards': 1, \
                'index.number_of_replicas': 0, \
                'index.refresh_interval': '5s', \
                'index.mapping.ignore_malformed': True, \
                'index.mapping.coerce': True, \
                'index.mapping.total_fields.limit': 1500 \
            } \
        })

    es.index(index=config.config['es_index'], doc_type="temp", body={"timestamp": datetime.datetime.now(), "temp_c": temp_c})


if __name__ == "__main__":
    main()
