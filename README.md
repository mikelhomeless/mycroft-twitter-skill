# Twitter skill

Currently skill gets the follower count of the user that is specified in the mycroft.conf file.  It also gets the current amount of followers for the president.

## Installation

Clone the repository into your `~/.mycroft/skills` directory. Then install the
dependencies inside your mycroft virtual environment:

If on picroft just skip the workon part and the directory will be /opt/mycroft/skills

```
workon mycroft
pip install tweepy
```


## Current state

Working features:
 - How many twitter followers do I have
 - How many twitter followers does trump have
 - How many twitter followers does the president have.

Known issues:
 - ...

TODO:
 - Post tweets
 - Get last status update from President (aka what he last tweeted)
 - Tell mycroft to follow a user
