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
One way to test or try out this bot might be to:
1. Create a virtual environment for it (`python -m venv haiku-mxbot` or whatever you'd like to name it)
2. Activate the virtual environment - Windows: `.\\haiku-mxbot\\Scripts\\activate` - Linux/Mac OS: `source haiku-mxbot/bin/activate` 
3. Install the dependencies mentioned above this section: `pip install simplematrixbotlib nltk dotenv`
4. Create a `.env` for bot account credentials:

   
      `MATRIX_HOMESERVER=https://matrix.example.chat`

   
      `MATRIX_USER=@bot:example.chat`

   
      `MATRIX_PASSWORD=password`


6. `python3 ./haiku-detector-strict.py` or `python3 ./haiku-detector.py`

### Dockerfile
If you really want to use it for your own server, then you could use the Dockerfile provided in this repo. Default Python image is used, so expect a filesize of around 2GB unless the Dockerfile is edited with better practices.

1. Edit the Dockerfile according to whether you want to use "strict" or otherwise (line 7).
2. `docker build -t haiku-mxbot .`
3. Create the `.env` file mentioned in the previous section.
4. `docker run -d --env-file /to/your/.env --restart unless-stopped haiku-mxbot`
