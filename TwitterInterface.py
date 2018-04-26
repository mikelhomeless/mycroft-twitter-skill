

# TODO
# Make the trending work based off the location of the user by default
# Make application obtain access keys for different users
# set functions that return tweets to return twitter objects rather than texts/counts...etc
# add exception handling

class TwitterInterface:

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

    def __get_tweet_by_id(self, tweetId):
        return self.__api()

    def get_me(self):
        return self.__api.me()


    # returns the latest tweet from a given username
    # expects a unique twitter username to be passed in
    def get_usr_tweet_latest(self, usrName):
       return self.__api.user_timeline(screen_name=usrName, tweet_mode="extended", count=1)[0]

    # Returns the top 10 items trending
    # Requires that a WOEID for the location be passed in
    def get_trending(self, WOEID):
        data = self.__api.trends_place(WOEID)
        return [x["name"].strip(self.__DISCARD_CHARACTERS) for x in data[0]["trends"]][:10]

    # returns most recent tweets in which the user was mentioned
    # count variable may be passed in to specify max number of tweets to return
    def get_rencent_mentions(self, mcount=20):
        return [x for x in self.__api.mentions_timeline(count=mcount, tweet_mode="extended")]

    # returns the users home feed
    # count variable may be passed to specify max number of tweets to return
    def get_home_tweets(self, mcount=20):
        return [x for x in self.__api.home_timeline(count=mcount, tweet_mode="extended")]

    # updates the user's status
    # requires a string to be passed
    def status_update(self, **kwargs):
        self.__api.update_status(**kwargs)

    def retweet(self, id):
        self.__api.retweet(id)

    def favorite_post(self, tweetId):
        self.__api.create_favorite(tweetId)

    def get_messages(self, mcount=1):
        return self.__api.direct_messages(count=mcount, full_text=True)

    def send_message(self, target_usr, msg):
        self.__api.send_direct_message(target_usr, text=msg)

    def block_user(self, usr):
        self.__api.create_block(usr)

    def follow_user(self, usr):
        self.__api.create_friendship(usr)

    # returns the number of times a tweet has been retweeted
    # requires a tweet id to be passed
    def get_retweets(self, tweetId):
        return self.__api.get_status(tweetId).retweet_count

    # returns number of favorites a tweet has
    # requires a tweet id to be passed
    def get_favoites(self, tweetId):
        return self.__api.get_status(tweetId).favorite_count

    # returns the number of followers a user has
    # requires a username to be passed
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
