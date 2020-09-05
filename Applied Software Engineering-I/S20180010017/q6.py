#!/bin/python3
# Root Threshold in IOT Devices

import math
import os
import random
import re
import sys

# Answer
def numDevices(statusQuery, threshold, dateStr):
    from http import client
    from json import loads
    from datetime import date, datetime, timedelta
    date = date(int(dateStr[3:]), int(dateStr[:2]), 1)
    devices = []
    cl = client.HTTPSConnection('jsonmock.hackerrank.com')
    page_no = 1
    while True:
        url = f'/api/iot_devices/search?status={statusQuery}&page={page_no}'
        cl.request('GET', url)
        res = cl.getresponse()
        res_body = res.read().decode()
        temp = loads(res_body)
        # print(temp)
        for x in temp['data']:
            if statusQuery.lower() == x['status'].lower():
                x_date = datetime(1970, 1, 1) + timedelta(milliseconds=int(x['timestamp']))
                if date.month == x_date.month and date.year == x_date.year:
                    if x['operatingParams']['rootThreshold'] > threshold:
                        devices.append(x)
        
        if int(temp['total_pages']) <= page_no:
            break
        page_no += 1
        
    return len(devices)

if __name__ == '__main__':

    statusQuery = input()

    threshold = int(input().strip())

    dateStr = input()

    result = numDevices(statusQuery, threshold, dateStr)

    print(str(result) + '\n')