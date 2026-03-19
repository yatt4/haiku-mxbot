# haiku-mxbot
A haiku Matrix bot. Inspired by YtnomSnrub's HaikuBot.
It is a Python beginner's script, made for fun, expect dragons (maybe?)

There are two scripts included in this repo:

`haiku-detector.py` will echo messages that are estimated to be 14-17 syllables long as a haiku.

`haiku-detector-strict.py` will also attempt to format messages, but in this case those that are estimated to be 17 syllables.

Strict may be better if you want to see the bot once in a while and are solely interested in 5-7-5 haikus.  
Uses:
- simplematrixbotlib
- nltk
- dotenv
## Usage
As of right now, the best way to use this bot might be to:
1. Create a virtual environment for it
2. Install the `requirements.txt`
3. Create a `.env` for bot account credentials and
4. then run it.

Might provide a dockerfile at some point.
