# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


# Visit https://docs.mycroft.ai/skill.creation for more detailed information
# on the structure of this skill and its containing folder, as well as
# instructions for designing your own skill based on this template.


# Import statements: the list of outside modules you'll be using in your
# skills, whether from other files in mycroft-core or from external libraries
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import tweepy


__author__ = 'btotharye'

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)


class TwitterAPI(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret, user):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(auth)
        self.user = user


    def get_followers(self):
        twitter_user = self.api.get_user(self.user)
        followers = twitter_user.followers_count
        return followers

# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"
class TwitterSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(TwitterSkill, self).__init__(name="TwitterSkill")
        self.user = self.config.get('twitter_user')
        self.twitter = TwitterAPI(self.config.get('consumer_key'),
            self.config.get('consumer_secret'),
            self.config.get('access_token'),
            self.config.get('access_secret'),
            self.user)
        consumer_key = self.config.get('consumer_key')
        consumer_secret = self.config.get('consumer_secret')
        access_token = self.config.get('access_token')
        access_secret = self.config.get('access_secret')
        user = self.user
        LOGGER.debug('The consumer key is {}, the consumer secret is {}, the access_token is {}, the access secret is {}, the user is {}.'.format(consumer_key, consumer_secret, access_token, access_secret, user))


    def get_followers(self):
        user = self.twitter.api.get_user(self.user)
        followers = user.followers_count
        return followers

    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))

        get_followers_intent = IntentBuilder("GetFollowersIntent").\
            require("GetFollowersKeyword").build()
        self.register_intent(get_followers_intent, self.handle_get_followers_intent)


    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.
    def handle_get_followers_intent(self, message):
        followers_count = self.twitter.get_followers()
        self.speak_dialog("followers", data={followers_count})


    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, the method just contains the keyword "pass", which
    # does nothing.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return TwitterSkill()
