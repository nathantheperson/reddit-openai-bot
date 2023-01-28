#Python 3.11.1 
#dependencies
import time
import random2
import praw
import openai





#openai key can be found at beta.openai.com/account/api-keys
API_KEY = "FOO"
openai.api_key = API_KEY
ai_model = "text-davinci-003"


#you can get the information you need to connect to the api from old.reddit.com/prefs/apps
reddit = praw.Reddit(
    client_id = "FOO",
    client_secret = "FOO",
    password = "FOO",
    user_agent = "FOO",
    username = "FOO",
)



#these are the subreddits that will be picked at random on the beginning of the while loop 
#add as many as you would like
subreddits_to_choose_from = ["FOO", "FOO"]



#these are the replies that will be randomly picked  
#you can add as many as you would like and I am unaware of any character limits
comment_replies = ["test1", "test2", "test3"]



#set "ai = False" to use randomly generated responses (comment_replies line 37) instead of ai generated response
ai = True 
#ai = False 


pull_random_subreddit = random2.randint(0, len(subreddits_to_choose_from) - 1)

while True: 
    subreddit = reddit.subreddit(subreddits_to_choose_from[pull_random_subreddit])
    #subreddit.new can be changed to subreddit.hot, subreddit.controversial, etc...
    #limit=20 is the amount of posts that are in the scope of the application's string search
    for submission in subreddit.new(limit = 20):
        for comment in submission.comments:
            if hasattr(comment, "body"):
                comment_lower = comment.body.lower()
                #" test string " on line 59 is the string that will be searched for and replied to
                if " test string " in comment_lower:
                    print("--------------------------------COMMENT----------------------------------")
                    print("comment being replied to ---> ", comment.body)
                    if ai == True:
                        ai_response = openai.Completion.create(
                            prompt = comment.body, 
                            model = ai_model,
                            #the more tokens, the more detailed the response
                            max_tokens = 1000,
                            temperature = 0.9
                        )
                        comment.reply(ai_response["choices"][0]["text"])
                        print("ai reply ---> ", ai_response["choices"][0]["text"])
                    else:
                        random_index = random2.randint(0, len(comment_replies) - 1)
                        local_reply = comment.reply(comment_replies[random_index])
                        print("randomly generated reply ---> ", local_reply.body)
                    time.sleep(random2.randint(600, 1200))
