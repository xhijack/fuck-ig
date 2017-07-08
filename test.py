#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("jakarumana", "master88")
InstagramAPI.login() # login
InstagramAPI.tagFeed("000studio") # get media list by tag #cat
media_id = InstagramAPI.LastJson # last response JSON
InstagramAPI.like(media_id["ranked_items"][0]["pk"]) # like first media
InstagramAPI.getUserFollowers(media_id["ranked_items"][0]["user"]["pk"]) # get first media owner followers

photo = "/Users/ramdani/Downloads/Abu-Immo-v2.png"


# InstagramAPI.uploadPhoto(photo=photo)
