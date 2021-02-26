import pandas as pd
import numpy as np
import os
import re
from collections import Counter
from tqdm import tqdm


ticker_list= ['AAPL',
 'ACB',
 'AMC',
 'AMD',
 'AMZN',
 'BABA',
 'BB',
 'BBBY',
 'BYND',
 'CGC',
 'FB',
 'GE',
 'GLD',
 'GM',
 'GME',
 'MSFT',
 'NIO',
 'NKLA',
 'NVDA',
 'PFE',
 'PLTR',
 'QQQ',
 'RIOT',
 'RKT',
 'SNOW',
 'SPY',
 'TLRY',
 'TSLA',
 'ZM']

def countStockMention(text, ticker_list):
    
    
    #keep only alphabetical characters
    text_alpha = re.sub('[^a-zA-Z]+', ' ', text)
    
    #make all text lower
    #text_lower = text_alpha.lower()
    
    #split on blackspace
    text_split = text_alpha.split(' ')
    
    #get counter
    text_counter = Counter(text_split)
    
    #keep only tickers
    ticker_count = {ticker: text_counter[ticker] for ticker in ticker_list}
    
    return ticker_count


def loadData():
    
    path = os.path.join('data', 'data_munged.csv')
    df = pd.read_csv(path,
                     index_col=0,
                     parse_dates=['created_utc'])

    #download all nasdaq companies
    stock_df = pd.read_csv(os.path.join('data', 'nyse_stocks.csv'))
    #take symbols and make lower
    #symbol = stock_df['Symbol'].str.lower()
    symbol = stock_df['ACT Symbol']
    
    return df, symbol



def main():
    
    df, symbol = loadData()
    
    ticker_count_list = []

    for self_text, title in tqdm(zip(df['self_text'], df['title'])):
        t = ' '.join([self_text, title])
        #count mentions and return dict
        ticker_count = countStockMention(t, ticker_list)
        #add dict to list
        ticker_count_list.append(ticker_count)

    #make dataframe from list of dicts
    ticker_df = pd.DataFrame(ticker_count_list)
    
    
    #get sum by columns
    ticker_col_sum = ticker_df.sum(axis=0)
    
    #keep top k emojis
    df_ticker_topk = ticker_df[ticker_col_sum.sort_values(ascending=False).index[:15]]
    
    
    #add date at end
    df_ticker_topk['created_utc'] = df['created_utc']
    
    #save the work
    df_ticker_topk.to_csv(os.path.join('data', 'ticker_count.csv'),
                     chunksize=5000)
    

if __name__ == '__main__':
    main()


