# Twitter skill

Currently skill gets the follower count of the user that is specified in the mycroft.conf file.  It also gets the current amount of followers for the president.

## Setup Twitter API
Eventually, it will be implemented so that once the user provides login credentials, Mycroft will obtain the access keys for the user using Twitter's oauth verification. For the time being, these keys must be obtained manually. These can be placed into the Mycroft config file by doing the following

Go over to https://apps.twitter.com/ and create an app.  This will give you the following information that you need to put into your mycroft.conf file located in /etc/mycroft/mycroft.conf.  Populate the fields accordingly, whatever the twitter_user is what is used for follower count, etc.

```
"TwitterSkill": {
    "consumer_key": "",
    "consumer_secret": "",
    "access_token": "",
    "access_secret": "",
    "twitter_user": ""
  }
```

## Description 
This Mycroft skill allows a user to post to their, message friends, retweet, get what's trending, get most recent items on their home timeline and much more.

## Future:
Eventually, the skill will have the ability to provide metrics about a given tweet/user/hashtag. For example, after Mycroft reads a tweet, the user will be given the opportunity to retweet, reply to the post, see how many favorites/retweets the post has or obtain the geo-location (low priority, will probably be one of the last items implemented). Or if Mycroft is providing multiple tweets in sequence, Mycroft will wait in between reading each tweet for the users next action or until the user says "next" or "next tweet" or anything along those lines. This will require implementing a way for Mycroft to remember the last read in tweet, even after the app has been exited. In the future, It will be implemented for the user to also be able to obtain metrics about themselves and their most recent tweet, as well as the ability to delete the most recent tweet.

## Installation

Clone the repository into your `~/.mycroft/skills` directory. Then install the
dependencies inside your mycroft virtual environment:

If on picroft just skip the workon part and the directory will be /opt/mycroft/skills

```
cd ~/.mycroft/skills
git clone https://github.com/btotharye/mycroft-twitter-skill.git TwitterSkill
workon mycroft
cd TwitterSkill
pip install tweepy
```

## Current state

Working phrases:
 - How many twitter followers do I have
 - How many twitter followers does trump have
 - How many twitter followers does the president have.
 - Follow br1anhopkins - To follow me on twitter, otherwise can be any twitter userid.
 - Unfollow br1anhopkins - To unfolow me but why would you want to do that :).  Same way any userid.
 - Post to twitter today is a great day to tweet from mycroftai - This will post a tweet with anything after the post to twitter part, use with caution no verify yet before it posts to twitter
* "Hey Mycroft How many followers do I have"
* "Hey Mycroft send a message to MichaelTHomer"
* "Hey Mycroft read my timeline"
* "Hey Mycroft what is the most recent tweet for realDonaldTrump"

Known issues:
 - ...

TODO:
 - implement the new functionalities from the TwitterInterface class to the skill
 - Whats trending
 - Search users
 - Get last status update from President (aka what he last tweeted)


## Credits 
mikelhomeless
btotharye
