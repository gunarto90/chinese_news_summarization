#!/usr/bin/python
# coding=utf-8

import json
from datetime import datetime

def debug(*argv):
  s = ' '.join(map(str, argv))
  print('[{}] {}'.format(datetime.now(), s))

def read_config(filename='db_config.json'):
  try:
    with open(filename) as data_file:
      config = json.load(data_file)
      return config
  except Exception as ex:
    print('Exception in init config file : %s' % ex)
  return None

def system_init():
  status = 200
  return status, read_config()