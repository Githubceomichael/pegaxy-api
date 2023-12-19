import pygsheets
import pandas as pd
import requests
import json
import sys
import time as time
from datetime import datetime

def convertDatetime24(epoch):
    convertedDatetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
    return convertedDatetime

def convertDatetime12(epoch):
    convertedDatetime = time.strftime('%b %d %I:%M %p', time.localtime(epoch))
    return convertedDatetime

now = datetime.now()
nowDatestamp = now.strftime('%m%d')
nowDatetime24 = now.strftime('%Y-%m-%d %H:%M:%S')
nowDatetime12 = now.strftime('%b %d %I:%M %p')

filename = nowDatestamp + '_apollo.txt'

with open(filename, 'r') as data:
    for line in sorted(data, key=lambda data_entry: int(data_entry[0])):
        print(line, end='')