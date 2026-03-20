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
1. Create a virtual environment for it (`python -m venv haiku-mxbot` or whatever you'd like to name it)
2. Activate the virtual environment - Windows: `.\\haiku-mxbot\\Scripts\\activate` - Linux/Mac OS: `source haiku-mxbot/bin/activate` 
3. Install dependencies using `requirements.txt`: `pip install -r requirements.txt`
4. Create a `.env` for bot account credentials:

   
      `MATRIX_HOMESERVER=matrix.placeholder.chat`

   
      `MATRIX_USER=@bot:placeholder.chat`

   
      `MATRIX_PASSWORD=password`


6. Run it in a CLI

Might provide a dockerfile at some point.
