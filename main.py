import os
from lyricsgenius import Genius
from dotenv import load_dotenv

load_dotenv()


class APIgenius():
    TOKEN = os.getenv('TOKEN')

    genius = Genius(TOKEN)
