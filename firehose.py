#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
# author: mehmet@mkorkmaz.com
# last_updated: 2016-04-07

import os
from twython import TwythonStreamer
from twython import Twython
import myutils
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config = myutils.read_yaml(BASE_DIR + '/config.ini')

client_args = {
    'headers': {
        'User-Agent': 'DontHateMeBot'
    },
    'allow_redirects': False
}
tw_config = config['twitter']
twitter = Twython(tw_config['api_key'], tw_config['api_secret'], tw_config['access_token'],
                  tw_config['access_token_secret'])


class MyStreamer(TwythonStreamer):

    def on_success(self, tweet_data):
        if 'text' in tweet_data:
            for idx, val in enumerate(config['keywords'], start=0):
                if re.search(val, tweet_data['text'], re.IGNORECASE):
                    if tw_config['user_name'] != tweet_data['user']['screen_name']:
                        status = '@' + tweet_data['user']['screen_name'] + ' ' + config['responses'][idx]
                        twitter.update_status(status=status)
                        print("Replied to:" + tweet_data['user']['screen_name'] + " for:" + val)

    def on_error(self, status_code, data):
        #  @TODO: Handle 420 errors
        print(status_code)


def firehose():
    words = config['keywords']
    stream = MyStreamer(tw_config['api_key'], tw_config['api_secret'], tw_config['access_token'],
                        tw_config['access_token_secret'])
    stream.statuses.filter(track=words)

if __name__ == '__main__':
    firehose()
