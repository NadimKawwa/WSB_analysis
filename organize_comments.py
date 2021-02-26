import pandas as pd
import requests #Pushshift accesses Reddit via an url so this is needed
import time
import datetime
from collections import OrderedDict
import os
from utils import readSubDir


def makeCommDataDict(data):
    """
    returns a dictionary of attributes from the comment
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
    data_dict['flair'] = ''
    
    #comment is not a video
    data_dict['is_video'] = 0
    
    #can't determine number of comments
    data_dict['num_comments'] = 0
    
    #get score of post
    data_dict['score'] = data['score']
    
    #get the text
    try:
        data_dict['self_text'] = data['body']
    except KeyError:
        data_dict['self_text'] = ' '
    
    #comments have no title
    data_dict['title'] = ' '
    
    #note if its submission or comment
    data_dict['is_submission'] = 0
    
    #note if this is the original commentator
    data_dict['is_op'] = int(data['is_submitter'])
    
    #can't get num subscribers
    # we can interpolate this later
    data_dict['subreddit_subscribers'] = None
    
    #no upvote ratio
    data_dict['upvote_ratio'] = 0
    
    #see if person has any followers
    data_dict['no_follow'] = data['no_follow']
    
    
    return data_dict
    
    
def main():
    #make a list of submissions
    comms_list = []

    #get all comments in file
    query_dir = os.path.join('data', 'comment')
    query_list = os.listdir(query_dir)

    for query in query_list:
        #smart join the path
        comm_dir = os.path.join('data', 'comment', query)
        #read all the data inside the list
        data_list = readSubDir(comm_dir)

        for data in data_list:
            data_dict = makeCommDataDict(data)
            comms_list.append(data_dict)
        
    df = pd.DataFrame(comms_list)
    #get the save path
    save_path = os.path.join('data', 'comment_df_raw.csv')
    
    df.to_csv(save_path)
    
    print("Done! Saved to...\t{}".format(save_path))

if __name__ == '__main__':
    main()