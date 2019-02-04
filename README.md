## weathergen.py
Generates weather descriptions for fictional environments and tweets them. Can be repurposed for any other randomizer which uses lists to generate results, and then tweet them.

### Requirements
  - [Python 2.7](https://www.python.org/downloads/release/python-2710/)
  - [pip](https://pypi.org/project/pip/) 
  - [tweepy](https://github.com/tweepy/tweepy)
  - a twitter developer account, so that the program may post tweets for you using your dev keys

### Basic setup
Download all included files. 

Open weathergen.py in a text editor and update lines 19 and 24 with the full path to the .txt files.

Update lines 36-39 with your twitter dev keys.

(To temporarily disable posting to twitter (such as in the case of troubleshooting using the command line), simply comment out line 56.)

### More info

This is a pretty basic Python generator, which uses tweepy to interface with twitter. It draws from several different sets of data in text files to generate strings. The RNG is EXTREMELY basic - rather than using any statistics functions to calculate probabilities from homogenous datasets, the probabilities are determined by how many times an entry is literally repeated in a set. To see what I mean, open up THE STATES FILE and use Ctrl+F to see how many times "rain" pops up versus "haboob". Don't ask me how I wrote those text files...it's embarrassing.

FUN CODING LESSON: This method of generation is pretty primitive and likely to be looked down upon by people who call themselves Coding Masters. That's largely because it's not efficient with memory usage (see the note about how probabilities are determined above). This works for ADB because we're working with pretty tiny data sets, on a script that runs once per day in a pretty low-key environment.

Note - Python's sleep() function is notoriously unreliable. It's fine for running in short bursts (for example, every 5 seconds), but it does not serve its purpose well for posting every 24 hours. I've downloaded the script on my phone and use a separate automation program to pull up and launch it daily (if you've ever noticed the bot posting at sort-of weird hours...that's why). It's been sort of a nightmare trying to get the daily posting to work the way I want it to, especially considering my Arduino is currently out of commission. If I ever find a good fix - believe me, you'll know.

This is a deprecated version of the code, by the way. A dev's got to have their secrets!
