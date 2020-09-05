#!/bin/python3
# Get Author Articles

import math
import os
import random
import re
import sys

# Answer
def getArticleTitles(author):
    from http import client
    from json import loads
    titles = []
    cl = client.HTTPSConnection('jsonmock.hackerrank.com')
    page_no = 1
    while True:
        url = f'/api/articles?author={author}&page={page_no}'
        cl.request('GET', url)
        res = cl.getresponse()
        res_body = res.read().decode()
        temp = loads(res_body)
        for x in temp['data']:
            if x.get('title', None):
                titles.append(x['title'])
            elif x.get('story_title', None):
                titles.append(x['story_title'])
        
        if int(temp['total_pages']) <= page_no:
            break
        page_no += 1
    
    return titles

if __name__ == "__main__":
    author = input()
    result = getArticleTitles(author)
    print('\n'.join(result))
    print('\n')
