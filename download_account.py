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

import requests

from InstagramAPI import InstagramAPI


def download(pic_url, name):
    with open('/Users/ramdani/Documents/practices/Instagram-API-python/results/' + name + '.jpg', 'wb') as handle:
        response = requests.get(pic_url, stream=True)

        if not response.ok:
            print("Failed download for ", name, pic_url)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


def write_text(text, name):
    fh = open('/Users/ramdani/Documents/practices/Instagram-API-python/results/' + name + '.txt', 'w')
    fh.write(text)
    fh.close()


PhotoPath = "/Users/ramdani/Documents/practices/Instagram-API-python/examples/photo" # Change Directory to Folder with Pics that you want to upload
IGUSER    = "jakarumana" # Change to your Instagram USERNAME
PASSWD    = "master88" # Change to your Instagram Password
# Change to your Photo Hashtag
IGCaption = "Selamat Hari Raya Idul Fitri #idulfitri"

os.chdir(PhotoPath)
ListFiles = [f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))]
print ("Total Photo in this folder:" + str (len(ListFiles)))

#Start Login and Uploading Photo
igapi = InstagramAPI(IGUSER,PASSWD)
igapi.login() # login

igapi.getUserFeed('1552719530')

response = igapi.LastJson
results = set()
print(len(response['items']))

next_max_id = response['next_max_id']
while next_max_id:
    print(next_max_id)
    for resp in response['items']:
        results.add(resp['image_versions2']['candidates'][0]['url'])

        # print(resp['caption']['text'], resp['id'])

        try:
            write_text(resp['caption']['text'], resp['id'])
        except:
            print("aya nu eror:", resp['id'])

        download(resp['image_versions2']['candidates'][0]['url'], resp['id'])

    igapi.getUserFeed('1552719530', next_max_id)
    response = igapi.LastJson

    try:
        next_max_id = response['next_max_id']
    except KeyError:
        next_max_id = False

print("Total Images:",len(results))

