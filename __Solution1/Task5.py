from datetime import datetime

from Task10 import DBWriter
from common import FILENAME
from Task7 import recalculate_words_statistic


class Feed:
    def publish(self, text):
        with open(FILENAME, 'a') as file:
            file.write(text)
        recalculate_words_statistic()

    def write_to_db(self, type: str, args: list[str]):
        DBWriter(type, args)


class News(Feed):
    def __init__(self, text, city):
        self.text = ("----== NEWS ==----\n"
                     "Text : {}\n"
                     "City : {}\n"
                     "Date : {}\n"
                     ).format(text, city, datetime.now())
        self.publish(self.text)
        self.write_to_db("N", [text, city, ('{}').format(datetime.now())])


class Ads(Feed):
    def __init__(self, text, city, expired):
        self.days_left = (datetime.strptime(expired, '%Y-%m-%d') - datetime.now()).days
        if self.days_left > 1:
            self.text = ("----== ADS ==----\n"
                         "Text : {}\n"
                         "City : {}\n"
                         "Expired: {}\n"
                         "Days left : {:n}\n"
                         ).format(text, city, expired, self.days_left)
            self.publish(self.text)
            self.write_to_db("A", [text, city, expired, self.days_left])
        else:
            print("ADS is outdated, cannot publish this")


class Tweet(Feed):
    def __init__(self, text, author):
        self.text = ("----== TWEET ==----\n"
                     "Text : {}\n"
                     "Author : {}\n"
                     "Text length : {:n}\n"
                     ).format(text, author, len(text))
        self.publish(self.text)
        self.write_to_db("T", [text, author, len(text)])
