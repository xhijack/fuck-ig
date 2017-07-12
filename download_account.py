#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

import os
import requests
import redis

from InstagramAPI import InstagramAPI
dir_path = os.path.dirname(os.path.realpath(__file__))


r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def download(pic_url, name):
    with open(dir_path + '/results/' + name + '.jpg', 'wb') as handle:
        response = requests.get(pic_url, stream=True)

        if not response.ok:
            print("Failed download for ", name, pic_url)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


def write_text(text, name):
    fh = open(dir_path + '/results/' + name + '.txt', 'w')
    fh.write(text)
    fh.close()


PhotoPath = dir_path + "/examples/photo" # Change Directory to Folder with Pics that you want to upload
IGUSER    = "jakarumana" # Change to your Instagram USERNAME
PASSWD    = "master88" # Change to your Instagram Password
# Change to your Photo Hashtag

#Start Login and Uploading Photo
igapi = InstagramAPI(IGUSER,PASSWD)
igapi.login() # login

igapi.getUserFeed('3669636824')

response = igapi.LastJson
results = set()
print(len(response['items']))

next_max_id = response['next_max_id']
while next_max_id:
    print(next_max_id)
    for resp in response['items']:
        results.add(resp['image_versions2']['candidates'][0]['url'])

        # # print(resp['caption']['text'], resp['id'])
        #
        # try:
        #     write_text(resp['caption']['text'], resp['id'])
        # except:
        #     print("aya nu eror:", resp['id'])

        download(resp['image_versions2']['candidates'][0]['url'], resp['id'])
        try:
            text = resp['caption']['text'].encode('utf-8')
        except TypeError:
            text = "#khimar #khimarinstan #ciput #ciputrajut #khimarwolvis #khimarwolpeach #khimarwolpis #khimarsyari " \
                   "#khimarmurah #jilbab #jilbabinstan #pashminainstan #kaoskakiwudlu #kaoskaki #handsock"
        finally:
            r.set(resp['id'], text)

    igapi.getUserFeed('3669636824', next_max_id)
    response = igapi.LastJson

    try:
        next_max_id = response['next_max_id']
    except KeyError:
        next_max_id = False

print("Total Images:",len(results))

