#!/usr/bin/env python

"""
Testing chatbot

Usage:
  main.py <bot_url> <content_file>
"""

from pathlib import Path

from docopt import docopt
from basecamp_chatbot.chatbot import Chatbot

def main(bot_url, content_file):
    print(f"bot_url={bot_url}")
    print(f"content_file={content_file}")
    
    bot = Chatbot(bot_url)
    bot.post_string("Posting update from string")
    bot.post_file(Path(content_file))

if __name__ == "__main__":
    args = docopt(__doc__)
    main(args["<bot_url>"], args["<content_file>"])