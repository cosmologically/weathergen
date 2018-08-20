#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Description: Generates weather descriptions for fictional environments and tweets them.
#Written for @ark_forecast on twitter.
#Author: Per Wolf
#Date: 08/19/2018
#Contact: per.c.wolf@gmail.com

import tweepy, time, random 

#initializing variables 
available = 0 
i = 0
statuscat = "■■TODAY'S WEATHER:■■\n"
biome = ["Sea of Nectar: ", "Sea of Tranquility: ", "Sea of Crises: ", "0"]
descriptor = ["Light ", "Heavy ", "Intermittent ", "Hints of ", "Relentless ", "Overcast ", "Oppressive ", "Violent ", "Gentle ", "Pleasant ", "Mild ", "Aggressive ", "Impending ", "Thick ", "Thin ", "Sporadic ", "Strange ", "Unusual ", "Unreal ", "Hazy ", "Smoggy ", "Dusty ", "Questionable ", "Blissful ", "Unending ", "Sunny "]
state = ["rain", "showers", "thunderstorms", "sunshine", "fog", "wind", "dryness", "humidity", "clouds", "snow", "drizzle", "smog", "sandstorms", "snowstorms", "hurricanes", "mist", "blizzard", "heatwaves", "hail", "rainbows", "flurries"]

#calculate how many biomes there are 	
while not biome[i] == "0":
	available = available + 1
	i = i + 1

	
#global variables for twitter keys 
#CONSUMER_KEY = '...'  
#CONSUMER_SECRET = '...'
#ACCESS_KEY = '...'
#ACCESS_SECRET = '...'
#auth = tweepy.0AuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#api = tweepy.API(auth)

	
#iterate through list of biomes, concatenate randomized descriptions together
#then tweet, reinitialize statuscat, sleep, reiterate, repeat
while i > 0:
	for i in range(0, available):
		rand_desc = random.choice(descriptor)
		rand_state = random.choice(state)
		statuscat = statuscat + biome[i] + rand_desc + rand_state + "\n" 
	print(statuscat) #for debugging on console
	#api.update_status(status=statuscat)
	statuscat = "■■TODAY'S WEATHER:■■\n"
	time.sleep(5) # tweet every 24 hours = 86400 sec. use 5 sec for console debugging
	
	
