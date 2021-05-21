import requests
import json
# import configtoken           ##contains bearer token
import tweepy, sys
from random import randint
import os
from boto.s3.connection import S3Connection

s3 = S3Connection(os.environ['consumer_key'], os.environ['consumer_secret'],
                  os.environ['access_token'],
                  os.environ['access_token_secret'],os.environ['brToken'])

# brToken = "AAAAAAAAAAAAAAAAAAAAACTCPgEAAAAApQVwDho4mLKixdozJfjvgfqw7t0%3De0xqhnIzmjNjmlTXtXLgqtULqLWIy9UVOY8DfMZo6jZzqy4oMY"
# keys = {
#     "consumer_key": "L6hQa4ojav1gemYYwmmFdriaA",
#     "consumer_secret": "MVhP8zTNqZrtjngCGyEuB9StV3gRIx3G4dvehBSyRp0yBGCTmZ",
#     "access_token": "1393850500504637440-jD5EW7vPzGkiL7K5E9m0UXFk1YwMXK",
#     "access_token_secret": "IBaMXWQrj1N5ACvOJdu9GjCPVJAFRDpn67Do9Fc6AAt5I"
# }



# CONSUMER_KEY = keys['consumer_key']
# CONSUMER_SECRET = keys['consumer_secret']
# ACCESS_TOKEN = keys['access_token']
# ACCESS_TOKEN_SECRET = keys['access_token_secret']
print(type(os.environ['consumer_key']))
CONSUMER_KEY = str(os.environ['consumer_key'])
CONSUMER_SECRET =str(os.environ['consumer_secret'])
ACCESS_TOKEN = str(os.environ['access_token'])
ACCESS_TOKEN_SECRET = str(os.environ['access_token_secret'])
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# handle = 'MadavanaB'
# user_id = api.get_user(handle).id_str
# message = 'hello, testing again from tweepy'
# dm = api.send_direct_message(recipient_id = user_id,text = message)
# print(dm.message_create['message_data']['text'])

def create_url_tweets():
    return "https://api.twitter.com/2/tweets/search/stream?tweet.fields=in_reply_to_user_id,author_id,referenced_tweets,conversation_id,public_metrics,created_at,source"

# def create_url_users(authID):
#     return "https://api.twitter.com/2/users?ids="+str(authID)+"&user.fields=profile_image_url"

# def create_url_parent_tweets(refTweet):
#     return "https://api.twitter.com/2/tweets?ids="+str(refTweet["id"])+"&tweet.fields=author_id,referenced_tweets,conversation_id,public_metrics,created_at,source"

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint_tweet(url, headers):
    response = requests.request("GET", url, headers=headers, stream=True)
    print('twitter response: ',response.status_code)
    # print(response.headers)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    else:
        try:
            for response_line in response.iter_lines():
                if response_line:
                    json_response = json.loads(response_line)
                    print(json.dumps(json_response, indent =4,sort_keys=True))
                    authID = json_response["data"]["author_id"]
                    parentTwtID = json_response["data"]["referenced_tweets"][0]["id"]
                    parentauthor = json_response["data"]["in_reply_to_user_id"]
                    message = "https://twitter.com/"+parentauthor+"/status/"+parentTwtID
                    # message="hello, you are gay"
                    dm = api.send_direct_message(recipient_id = authID,text = message)
                    print(dm.message_create['message_data']['text'])
        except:
            print("calling again")
            return "callagain"


# def get_all_parents(refTweet,headers):
#     url = create_url_parent_tweets(refTweet)
#     response = requests.request("GET", url, headers=headers)
#     print('twitter parent response: ',response.status_code)
#     # print(response.headers)
#     if response.status_code != 200:
#         raise Exception(
#             "Request returned an error: {} {}".format(
#                 response.status_code, response.text
#             )
#         )
#     else:
#         json_response = json.loads(response.content)
#         print(json.dumps(json_response, indent =4,sort_keys=True))
#         authID = json_response["data"][0]["author_id"]
#         connect_to_endpoint_users(authID,headers)
#         store_tweet_data(json_response)
#         if(json_response["data"][0]["id"]!=json_response["data"][0]["conversation_id"]):
#             get_all_parents(json_response["data"][0]["referenced_tweets"][0],headers)


# def connect_to_endpoint_users(authID, headers):
#     url = create_url_users(authID)
#     response = requests.request("GET", url, headers=headers)
#     print('user response: ',response.status_code)
#     # print(response.headers)
#     if response.status_code != 200:
#         raise Exception(
#             "Request returned an error: {} {}".format(
#                 response.status_code, response.text
#             )
#         )
#     else:
#         json_response = json.loads(response.content)
#         # store_user_data(json_response)
#         print(json.dumps(json_response,indent=4))


# def store_tweet_data(json_response):
#     data=dict()
#     for key,value in json_response["data"].items():
#         data[key]= value
#     if "referenced_tweets" not in data:
#         data["referenced_tweets"] = [{"id":"none","type":"none"}]
#     print(json.dumps(data, indent =4,sort_keys=True))



# def store_user_data(json_response):
#     data=dict()
#     for key,value in json_response["data"][0].items():
#         data[key]= value
#     print(json.dumps(data, indent =4,sort_keys=True))





def main():
    bearer_token = os.environ['brToken']
    url = create_url_tweets()
    headers = create_headers(bearer_token)
    timeout = 0
    error = connect_to_endpoint_tweet(url=url,headers=headers)
    if error == "callagain":
        connect_to_endpoint_tweet(url=url,headers=headers)


if __name__ == "__main__":
    main()