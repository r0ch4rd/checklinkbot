import praw
import re

reddit = praw.Reddit(
    client_id = "",
    client_secret = "",
    username = "",
    password = "",
    user_agent = ""
)

subreddit = reddit.subreddit("all")
for comment in subreddit.stream.comments(skip_existing=True):
    
    if '<a' and 'href="' and '</a>' in comment.body_html:
        s = comment.body_html
        start = 'href="'
        end = '">'
        
        result = re.search('%s(.*)%s' % (start, end), s).group(1)

        if comment.author != "CheckLinkBot" and comment.locked == False:
            comment.reply(result + "    &nbsp;    ^This ^action ^was ^performed ^automatically.")


        
        print(comment)
        print(result)
        
