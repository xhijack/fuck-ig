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
from InstagramAPI import InstagramAPI


PhotoPath = "/Users/ramdani/Documents/practices/Instagram-API-python/results" # Change Directory to Folder with Pics that you want to upload
IGUSER    = "jakarumana" # Change to your Instagram USERNAME
PASSWD    = "master88" # Change to your Instagram Password
# Change to your Photo Hashtag
IGCaption = "Selamat Hari Raya Idul Fitri #idulfitri"

os.chdir(PhotoPath)
import pdb
#
# ListFiles = [f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f)) and f.endswith(".jpg")]
# print("Total Photo in this folder:" + str(len(ListFiles)))
#
# def ambil_text(name):
#     if os.path.isfile(name[:-3] + 'txt'):
#         data = open(name[:-3] + 'txt')
#         return data.read()
#     return False
#
# # Start Login and Uploading Photo
# igapi = InstagramAPI(IGUSER,PASSWD)
# igapi.login() # login
#
# for i in range(len(ListFiles)):
#     photo = ListFiles[i]
#     print ("Progress :" + str([i+1]) + " of " + str(len(ListFiles)))
#     print ("Now Uploading this photo to instagram: " + photo)
#     caption = ambil_text(photo)
#     if caption:
#         igapi.uploadPhoto(photo,caption=caption,upload_id=None)
#         # sleep for random between 600 - 1200s
#         n = randint(600,1200)
#         print ("Sleep upload for seconds: " + str(n))
#         time.sleep(n)
#     else:
#         print('Skip for ', photo)



class Bot(object):

    def __init__(self, username, password, photo_path):
        self.username = username
        self.password = password
        self.photo_path = photo_path

        self.igapi = InstagramAPI(self.username,self.password)

    def _login(self):
        self.igapi.login()

    def _dirphotolist(self):
        ListFiles = [f for f in listdir(self.photo_path) if isfile(join(self.photo_path, f)) and f.endswith(".jpg")]
        return ListFiles

    def _get_caption(self, name):
        if os.path.isfile(name[:-3] + 'txt'):
            data = open(name[:-3] + 'txt')
            return data.read()
        return False

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
            if caption:
                if caption == "":
                    caption = "#khimar %khimarinstan #ciput #ciputrajut #khimarwolvis #khimarwolpeach #khimarwolpis #khimarsyari #khimarmurah #jilbab"
                self.igapi.uploadPhoto(file, caption=caption, upload_id=None)
                n = randint(600, 1200)
                print("Sleep upload for seconds: " + str(n))
                time.sleep(n)
            else:
                print("skip for ", file)


if __name__ == '__main__':
    bot = Bot(username='jakarumana', password='master88', photo_path="/Users/ramdani/Documents/practices/Instagram-API-python/results")
    try:
        bot.run()
    except KeyboardInterrupt:
        print("Wow interupt keyboard")
        bot._logout()