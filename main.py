import praw
import re

reddit = praw.Reddit(
    client_id = "yPDyln-ZgS8diFhhcVRtZw",
    client_secret = "v_dYfZmSEKXUOSHiBJZyZOTac0N9mA",
    username = "CheckLinkBot",
    password = "amogussussybaka",
    user_agent = "CheckLinkBot"
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
        
