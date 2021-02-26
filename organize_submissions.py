import pandas as pd
import requests #Pushshift accesses Reddit via an url so this is needed
import time
import datetime
from collections import OrderedDict
import os
from utils import readSubDir



def makeSubDataDict(data):
    """
    returns a dictionnary of attributes from the submission.
    This is done manually in order to force you/future me to understand the paramas
    """
    data_dict = {}
    
    #get awards if any
    if data['total_awards_received']:
        data_dict['total_awards_received'] = data['total_awards_received']
    else:
        data_dict['total_awards_received'] = 0
    #get the author name
    data_dict['author'] = data['author']
    #see if author is premium
    try:
        data_dict['author_premium'] = data['author_premium']
    except KeyError:
        data_dict['author_premium'] = False
    
    #get date of creation
    data_dict['created_utc'] = data['created_utc']
    #get the flair
    try:
        data_dict['flair'] = data['link_flair_text']
    except KeyError:
        data_dict['flair'] = ''
        
    #see if has a video
    try:
        data_dict['is_video'] = int(data['is_video'])
    except KeyError:
        data_dict['is_video'] = 0
        
    #get number of comments
    try:
        data_dict['num_comments'] = data['num_comments']
    except KeyError:
        data_dict['num_comments'] = 0
    
    #get score of post
    data_dict['score'] = data['score']
    
    #get the text
    try:
        data_dict['self_text'] = data['self_text']
    except KeyError:
        data_dict['self_text'] = ' '
        
    #get the title
    try:
        data_dict['title'] = data['title']
    except KeyError:
        data_dict['title'] = ' '
        
    #note if its submission or comment
    data_dict['is_submission'] = 1
    
    #note if this is the original commentator
    data_dict['is_op'] = 1
    
    #get subscribers at time of post
    try:
        data_dict['subreddit_subscribers'] = data['subreddit_subscribers']
    except KeyError:
        data_dict['subreddit_subscribers'] = None
    
    #get upvote ratio
    try:
        data_dict['upvote_ratio'] = data['upvote_ratio']
    except KeyError:
        data_dict['upvote_ratio'] = 0
    #see if person has any followers
    data_dict['no_follow'] = data['no_follow']
    
    return data_dict

def main():
    #make a list of submissions
    subs_list = []

    #get all submissions in file
    submission_query_dir = os.path.join('data', 'submission')
    submission_query_list = os.listdir(submission_query_dir)

    for query in submission_query_list:
        #smart join the path
        sub_dir = os.path.join('data', 'submission', query)
        #read all the data inside the list
        data_list = readSubDir(sub_dir)

        for data in data_list:
            data_dict = makeSubDataDict(data)
            subs_list.append(data_dict)
        
    df = pd.DataFrame(subs_list)
    
    #get the save path
    save_path = os.path.join('data', 'submission_df_raw.csv')
    
    df.to_csv(save_path)
    
    print("Done! Saved to...\t{}".format(save_path))

if __name__ == '__main__':
    main()