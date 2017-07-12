#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint

import redis

from InstagramAPI import InstagramAPI

dir_path = os.path.dirname(os.path.realpath(__file__))


class Bot(object):

    def __init__(self, username, password, photo_path, redis):
        self.username = username
        self.password = password
        self.photo_path = photo_path
        self.redis = redis
        self.igapi = InstagramAPI(self.username,self.password)

    def _login(self):
        self.igapi.login()

    def _dirphotolist(self):
        ListFiles = [f for f in listdir(self.photo_path) if isfile(join(self.photo_path, f)) and f.endswith(".jpg")]
        return ListFiles

    def _get_caption(self, name):
        return self.redis.get(name[:-4])

    def _delete_data(self, name):
        self.redis.delete(name[:-4])

    def run(self):
        print ("Tyring login")
        self._login()
        print("Trying Uploads")
        self._uploads()
        print("Trying Logout")
        self._logout()

    def _logout(self):
        self.igapi.logout()

    def _uploads(self):
        list_files = self._dirphotolist()
        print("Total Uploads: ", len(list_files))
        for file in list_files:
            print("Uoload ", file)
            caption = self._get_caption(file)
            self._delete_data(file)
            self.igapi.uploadPhoto(file, caption=caption, upload_id=None)
            n = randint(600, 1200)
            print("Sleep upload for seconds: " + str(n))
            time.sleep(n)

    def _upload(self, file, caption):
        self.igapi.uploadPhoto(file, caption=caption, upload_id=None)

if __name__ == '__main__':
    r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    # bot = Bot(username='jakarumana', password='master88', photo_path=dir_path + "/results", redis=r)
    # try:
    #     bot.run()
    # except KeyboardInterrupt:
    #     print("\n Wow interupt keyboard")
    #     bot._logout()

    from accounts import ACCOUNTS

    bots = []
    for acc in ACCOUNTS:
        bot = Bot(username=acc['username'], password=acc['password'], photo_path=dir_path + "/results", redis=r)
        print("Login for ", acc['username'])
        bot._login()
        bots.append(bot)

    # list_files = bot._dirphotolist()
    photo_path = dir_path + "/results"
    list_files = [f for f in listdir(photo_path) if isfile(join(photo_path, f)) and f.endswith(".jpg")]

    print(photo_path)
    print(list_files)
    # print("Total Uploads: ", len(list_files))
    # for file in list_files:
    #     print("trying upload ", file)
    #     for bot in bots:
    #         print("Bot {} upload {}".format(bot.username, file))
    #         bot._upload(file, bot._get_caption(file))
    #     n = randint(600, 1200)
    #     print("Sleep upload for seconds: " + str(n))
    #     time.sleep(n)
    #
    # for bot in bots:
    #     bot._logout()
    #     print("User {} logout", bot.username)




