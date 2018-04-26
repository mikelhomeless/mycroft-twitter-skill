

# TODO
# Make the trending work based off the location of the user by default
# Make application obtain access keys for different users
# remove keys once pushing to main (security reasons)

''' 
This class is designed to handle api calls to Twitter and is based off the 
Twitter API library Tweepy https://github.com/tweepy/tweepy
For all functions, unless stated otherwise, return values are twitter objects (tweet/message/user objects) and not individual data points.
To get the data from these returned objects, you must know how the file is stored in JSON format. The JSON file structures 
can be found on Twitter's API website https://developer.twitter.com/en/docs

To obtain the data out of these objects we do as follows outside of the class:
Say we want to get the text of a tweet from the object t1. We represent this request in code as:
    "t1.full_text"
For a time stamp
    t1.created_at
And so on and so forth'''

class TwitterInterface:
    
    __author__ = "mikelhomeless"

    def __init__(self):
        import tweepy
        self.__DISCARD_CHARACTERS = '@#'
        self.auth = tweepy.OAuthHandler('G13Mg6NgxaHhNnOo5KYCGVqS9',
                                        'XCvEll6hjQ3JZlmN3im4NYeWfgmZf28gpq46dvuzZUDqAq845r')
        # eventually this file will contain the user's keys, but for now it's a dummy account on Twitter
        self.auth.set_access_token(*self.__get_access_keys())
        self.__api = tweepy.API(self.auth)

    def __get_access_keys(self):
        key_file = open("keys.txt", 'r')
        TOKENS = [x.strip() for x in key_file]
        return TOKENS
    
    '''Finds and returns a tweet object by the tweet id'''
    def __get_tweet_by_id(self, tweetId):
        return self.__api.get_status(tweetId)
    
    '''Returns a user object for the logged in user'''
    def get_me(self):
        return self.__api.me()


    ''' returns the latest tweet from a given username as a tweet object
        expects a unique twitter username to be passed in'''
    def get_usr_tweet_latest(self, usrName):
       return self.__api.user_timeline(screen_name=usrName, tweet_mode="extended", count=1)[0]

    ''' Returns the top 10 items trending as a list of strings
        Requires that a WOEID for the location be passed in'''
    def get_trending(self, WOEID):
        data = self.__api.trends_place(WOEID)
        return [x["name"].strip(self.__DISCARD_CHARACTERS) for x in data[0]["trends"]][:10]

    ''' returns most recent tweets in which the user was mentioned as a list of tweet objects
        count variable may be passed in to specify max number of tweets to return'''
    def get_rencent_mentions(self, mcount=20):
        return [x for x in self.__api.mentions_timeline(count=mcount, tweet_mode="extended")]

    ''' returns the users home feed as a list of tweet objects
        count variable may be passed to specify max number of tweets to return an cannot be greater than 20'''
    def get_home_tweets(self, mcount=20):
        return [x for x in self.__api.home_timeline(count=mcount, tweet_mode="extended")]

    ''' updates the user's status
        Arguments passed in are allowed to be anything specified in the api documentation for the update_status function
        However, the tweet text MUST be passed in'''
    def status_update(self, **kwargs):
        self.__api.update_status(**kwargs)
    
    ''' Allows user to retweet
        a tweet id must be given'''
    def retweet(self, id):
        self.__api.retweet(id)
        
     ''' Allows user to like a post
         a tweet id must be given'''
    def favorite_post(self, tweetId):
        self.__api.create_favorite(tweetId)
    
    ''' recieves mcount direct messages the user has received as a list of message objects
        messages are returned in order of time sent. Ex. messages[0] will be the most recent message'''
    def get_messages(self, mcount=1):
        return self.__api.direct_messages(count=mcount, full_text=True)
    
    ''' Sends a message to a user
        A username/userid must be provided as well as a message sting'''
    def send_message(self, target_usr, msg):
        self.__api.send_direct_message(target_usr, text=msg)
    
    ''' Blocks a user from sending messages and viewing a user's profile
        a user id or username must be provided'''
    def block_user(self, usr):
        self.__api.create_block(usr)
    
    ''' Follows a user
        user id or username must be provided'''
    def follow_user(self, usr):
        self.__api.create_friendship(usr)

    ''' returns the number of times a tweet has been retweeted as an integer
        tweet id must be provided'''
    def get_retweets(self, tweetId):
        return self.__api.get_status(tweetId).retweet_count

    ''' returns number of favorites a tweet has
        tweet id must be provided'''
    def get_favoites(self, tweetId):
        return self.__api.get_status(tweetId).favorite_count

    ''' returns the number of followers a user has
        userName or id must be provided'''
    def get_followers(self, usrName):
        return self.__api.get_user(usrName).followers_count



if __name__ == "__main__":
    Twitter = TwitterInterface()
    print(Twitter.get_followers("realDonaldTrump"))
    print(Twitter.get_usr_tweet_latest("realDonaldTrump").full_text)
    print(Twitter.get_trending(23424977))
    print(Twitter.get_rencent_mentions(10))
    x = Twitter.get_usr_tweet_latest(Twitter.get_me().screen_name)
    print(x.full_text)
    print(Twitter.get_messages()[0].text)

    #Twitter.retweet(x.id)
