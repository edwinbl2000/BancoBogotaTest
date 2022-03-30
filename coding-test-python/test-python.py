#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************
# **       BullDocker         **
# ** Date  : 18/05/2019       **
# ** Author: ADL DevOps Team  **
# ******************************


from sys import exit

import sys
sys.path.append('/content/sample_data/test')

import main

if __name__ == "__main__":
    exit(main.run())