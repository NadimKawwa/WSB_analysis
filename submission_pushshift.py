import pandas as pd
import requests #Pushshift accesses Reddit via an url so this is needed
import json #JSON manipulation
import csv #To Convert final table into a csv file to save to your machine
import time
import datetime
from collections import OrderedDict
import os
import functools

def slow_down(_func=None, *, rate=1):
    """Sleep given amount of seconds before calling the function"""
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down

    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)

def makeQueryUrlSubmission(after, before, size=1000):
    """
    make a query url for pushshift
    """
    #create the base URL
    url_base = 'https://api.pushshift.io/reddit/search/submission/?'
    
    #search paramters for comments
    search_params = OrderedDict()
    #search term
    search_params['q'] = ''
    #get specific comments via their ids
    search_params['size'] = str(size)
    #sort results in a specific order
    search_params['sort'] = 'desc'
    #sort by a specific attribute
    search_params['sort_type'] = 'score'
    #restrict to a specific subbreddit
    search_params['subreddit'] = 'wallstreetbets'
    #return results after this date
    search_params['after'] = str(after)
    #return results before this date
    search_params['before'] = str(before)
    #display query metadata
    search_params['metadata'] = 'true'
    
    #create query url
    query_url =url_base
    for k, v in search_params.items():
        #if value is not none
        if v:
            query = k+'='+v+'&'
            query_url += query
    
    return query_url

@slow_down(rate=1)
def getRequestSubmissionData(query_url, after):
    #get the url
    r = requests.get(query_url)
    #load the data with json
    data = json.loads(r.text)
    #create filename
    filename = 'submission_' + str(after) + '.json'
    #select directory
    file_dir = os.path.join('data', 'submission', filename)
    print(f"Saving to... \t {file_dir}")
    with open(file_dir, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
        
    
    #set start and end date
    after = 1593561600
    #get interval of collection ALWAYS USE INTEGER DIVISION
    interval = 86_400//3
    
    #86400 seconds = 1 day
    before = after + interval

    #assume that we will query everything until today
    query_window_limit = time.time()

    while before <= query_window_limit:
        #get the query url
        query_url = makeQueryUrlSubmission(after=after, before = before)
        #save the file 
        getRequestSubmissionData(query_url, after)
        
        #move  ahead
        after, before = before, before + interval
    
    
    
    