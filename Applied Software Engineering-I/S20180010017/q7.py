#!/bin/python3
# Most Active Authors

import math
import os
import random
import re
import sys

# Answer
def getUsernames(threshold):
    from http import client
    from json import loads
    users = []
    cl = client.HTTPSConnection('jsonmock.hackerrank.com')
    page_no = 1
    while True:
        url = f'https://jsonmock.hackerrank.com/api/article_users?page={page_no}'
        cl.request('GET', url)
        res = cl.getresponse()
        res_body = res.read().decode()
        temp = loads(res_body)
        
        for x in temp['data']:
            if int(x['submission_count']) > threshold:
                if x['username'] not in users:
                    users.append(x['username'])
        
        if int(temp['total_pages']) <= page_no:
            break
        page_no += 1
        
    return users

if __name__ == '__main__':
    threshold = int(input().strip())

    result = getUsernames(threshold)

    print('\n'.join(result))
    print('\n')

