import asyncio
import simplematrixbotlib as botlib
import re
import nltk
from nltk.corpus import cmudict
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

creds = botlib.Creds(
    os.environ["MATRIX_HOMESERVER"],
    os.environ["MATRIX_USER"],
    os.environ["MATRIX_PASSWORD"]
)
bot = botlib.Bot(creds)

# cmu dictionary download
nltk.download('cmudict')
dic = cmudict.dict()

# lumo generated code - it counts syllables by using something known as stress markers 
def count_syllables(word):
    # lowercases and gets rid of punctuation
    word = word.lower().strip(".,!?")   
    phones = dic.get(word, [[]])[0] # uses the first pronunciation from it's list
    if phones:
        # it returns number of digits (phoneme stress markers) as those will indicate the syllable count
        # hello = H, AH0, L, OW1 - two syllables
        return len([c for phone in phones for c in phone if c.isdigit()])
    # vowel groups for unknown words (using regex)
    return len(re.findall(r'[aeiouy]+', word))

def count_sylls_text(text):
    count = 0
    for word in text.split():
        count += count_syllables(word)
    return count

def normalize_words(text):
    return re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower())

def haiku_format(message):
    if count_sylls_text(message) in [14, 15, 16, 17, 18]:
        print("Haiku detected?")
        print("Estimated syllable count: " + str(count_sylls_text(message)))
        line_break = []
        line = []
        count = 0
        line_num = 0
        result = "_"

        # patterns depending on length
        match count_sylls_text(message):
            case 14:
                line_break = [4, 10, 14]
            case 15:
                line_break = [4, 11, 15]
            case 16:
                line_break = [5, 11, 16]
            case 17:
                line_break = [5, 12,17]
            case 18:
                line_break = [5, 13, 18]

        # iteration to format the message into haiku
        for word in message.split():
            line.append((word))
            count += count_syllables(word)
            if line_num < 3 and count >= line_break[line_num]:
                result += " ".join(line)
                if line_num < 2:
                    result += "\n"
                line = []
                line_num += 1

        # check in case the iteration did not process the message correctly (by comparing word count)
        if normalize_words(result) == normalize_words(message):
            result += "_"
            print(result)
            return result
        else:
            print("Failed to parse (or false positive?)")
            return 0

# modified example from simple-matrix-bot-lib documentation
@bot.listener.on_message_event
async def haiku_handler(room, message):
    match = botlib.MessageMatch(room, message, bot)
    if match.is_not_from_this_bot() and count_sylls_text(match.event.body) in [14, 15, 16, 17, 18]:
        response = haiku_format(match.event.body)
        if response != 0:
            await bot.api.send_markdown_message(room.room_id, response)
            await asyncio.sleep(2)

bot.run()