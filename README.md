# opentdb
A free api_wrapper for trivia question and answer

You can download the file and keep it anywhere in your code

Usage

from opentdb import OpenTDB

async def main():
    opentdb = OpenTDB("https://opentdb.com/api.php?amount=10&type=multiple",1,10")
    question = await opentdb.question()
    answers = await opentdb.answers()
    category = await opentdb.category()
    difficulty = await opentdb.difficulty()
    
