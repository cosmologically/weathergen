#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Description: Generates weather descriptions for fictional environments and tweets them.
#Author: Per Wolf
#Date: 08/19/2018
#Contact: per.c.wolf@gmail.com

import tweepy, time, random 

#initializing variables 
available = 0 
i = 0
statuscat = "TODAY'S WEATHER:\n"
biome = ["Biome 1: ", "Biome 2: ", "Biome 3: ", "0"]


descriptor = []
with open("...", "r") as f: # "..." needs to be full file path to descriptor file. ex: "C:\Users\Legion\Desktop\weatherbot\descriptorfile.txt"
	for line in f.readlines():
		descriptor = descriptor + line.strip("\n").split("\n")	
f.close()	
state = []
with open("...", "r") as f: # "..." needs to be full file path to states file. ex: "C:\Users\Legion\Desktop\weatherbot\statesfile.txt"
	for line in f.readlines():
		state = state + line.strip().split("\n")	
f.close()		
#calculate how many biomes there are 	
while not biome[i] == "0":
	available = available + 1
	i = i + 1

	
#global variables for twitter keys 
CONSUMER_KEY = '...'  
CONSUMER_SECRET = '...'
ACCESS_KEY = '...'
ACCESS_SECRET = '...'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

user = api.me()
print (user.name)

	
#iterate through list of biomes, concatenate randomized descriptions together
#then tweet, reinitialize statuscat, sleep, reiterate, repeat
while i > 0:
	for i in range(0, available):
		rand_desc = random.choice(descriptor)
		rand_state = random.choice(state)
		statuscat = statuscat + biome[i] + rand_desc + rand_state + "\n" 
	print(statuscat) #for debugging on console
	api.update_status(statuscat)
	statuscat = "TODAY'S WEATHER:\n"
	time.sleep(86400) # tweet every 24 hours = 86400 sec. use 5 sec for console debugging
	
	
