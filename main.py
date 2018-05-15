#!/usr/bin/env python
# coding=utf-8
### General library
import numpy as np
import pandas as pd
### Custom import
from lalala.functions import debug, read_config, system_init
import lalala.database as mysql

def main():
    status, config = system_init()
    if status != 200:
        return
    # debug(config)
    # db_config = config['database']
    # mysql.connect_via_config(db_config)

if __name__ == '__main__':
    main()