# WallStreetBets Analysis
![WSB Banner](https://github.com/NadimKawwa/WSB_analysis/blob/main/plots/wsb_banner.png)

The objective of this repository is to dissect r/wallstreetbets using data science. Particularly, I aim to show the trends among the swarm of loosely-coordinated, individual retail investors who short squeezed GME. I will do this by first, demonstrating how to collect the data. Next, I will present plots that offer snapshots into WSB. Finally, I will use NLP to measure emotional engagement on the subreddit.



# Environment

All code is written in Python 3.6.
Packages are summarized in [requirements.txt](https://github.com/NadimKawwa/WSB_analysis/blob/main/requirements.txt)

# Getting Started

To collect data and customize the range, refer to [submission_pushshift.py](https://github.com/NadimKawwa/WSB_analysis/blob/main/submission_pushshift.py) and [comment_pushshift.py](https://github.com/NadimKawwa/WSB_analysis/blob/main/comment_pushshift.py).
Be sure to customize the range and paramters that suit your needs.
You might want to modify the decorator @slow_down to do just that: slow down the function based on your connection speed and so not to overload pushsift.

To compile the data, refer to [organize_submissions.py](https://github.com/NadimKawwa/WSB_analysis/blob/main/organize_submissions.py) and [organize_comments.py](https://github.com/NadimKawwa/WSB_analysis/blob/main/organize_comments.py). I made a point to add as many comments as possible beccause it did take me a while to discover what I'm working with :).

# Where is Your Data?
Data is not uploaded since it won't fit on Github.
In addition, pushshift returns Reddit usernames, I would rather not share that.

# How Is This Different From Other Analyses?
The sentiment analysis account for the following:
- Upvote Ratio
- Time Trending
- Number of Comments Received
- Total Awards Received

Therefore this analysis takes into account the temporal effect of a post and the interaction it received on WSB Forums. 
  

# Plots

![WSB member count](https://datapane.com/u/nadim/reports/wsb-member-count/)

![Emoji Use Cumulative Sum](https://datapane.com/u/nadim/reports/wsb-emoj-cumsum/)

![Mention of Stocks](https://datapane.com/u/nadim/reports/wsb-ticker-cumsum/)

![7 Day Rolling Average Sentiment](https://datapane.com/u/nadim/reports/wsb-emotion-7drolling/)

