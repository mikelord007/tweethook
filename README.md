![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)

# tweethook
For TinkerHub Build From Home Contest- Python Script that uses the Twitter API to save and display a tweet thread.

Write a personal script that uses the Twitter API to save the tweet thread in a suitable form for later consumption.

Check Out the bot: https://twitter.com/hook_tweet
## Team members
1. Manu Jasan [https://github.com/mikelord007]
2. Allen George Ajith [https://github.com/allen-del]
3. Bennett B Madavana [https://github.com/bennett1412]
## Team Id
 BFH/recKGoOYu2vV9QHCH/2021 
## Link to product walkthrough
[link to video](https://drive.google.com/file/d/1rC-u5A2BqRn3NvJZZAa1By6PqNtYv3jG/view?usp=sharing)

## How it works?
1. The bot uses 2 API's. One is an filtered stream connection that is open indefinitely ( unless rate limited ) and will return the relevant data whenever someone tags the bot in a tweet. The data includes the author ID of the person who tagged the bot, tweet id of the referenced tweet and author ID of the author of the referenced tweet. This is then used to create a link to that referenced tweet.
2. The second API is a normal API which sends the link as a direct message to the person who tagged the bot. This API is set up using tweepy, a lightweight library for twitter API.

## Libraries used
- requests - 2.25.1
- requests-oauthlib - 1.3.0
- requests-toolbelt - 0.9.1
- json5 - 0.9.5
- jsonschema - 3.2.0
- tweepy - 3.10.0
- boto - 2.49.0
## How to configure
Theres nothing much to configure. The bot is already hosted on heroku and won't allow multiple instances of itself to run.
All the API tokens and keys are given as an environment variable in heroku and the dependencies used for the bot are saved in requirements.txt
To run in your system make a twitter dev account and use the tokens and access keys.
## How to Run
The bot is now live. To save a tweet, the user needs to mention the bot as a reply to that tweet ( mention @hook_tweet ) and that tweet will be sent as a dm to the user.  
If you want to run on your system, install the required libraries:  
run:`pip install -r requirements.txt` in your shell.  
Simply run the tweetHook.py script  
And then use the bot as mentioned above  

