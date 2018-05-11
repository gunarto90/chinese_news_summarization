#!/usr/bin/env python
# coding=utf-8
### General library
import numpy as np
import pandas as pd
### Custom import
import lalala.functions as fn
import lalala.database as mysql

def main():
    status, config = fn.system_init()
    if status != 200:
        return
    fn.debug(config)
    # db_config = config['database']
    # mysql.connect_via_config(db_config)

if __name__ == '__main__':
    main()