import os
import xml.etree.ElementTree as ET

from Task4 import capitalize_string
from Task5 import News, Tweet, Ads

DEFAULT_FILENAME = 'Task9_default.xml'


class FeedXML:
    def __init__(self, file_path):
        if not file_path:
            self.__create_default_file()
            self.file_path = DEFAULT_FILENAME
        else:
            self.file_path = file_path
        self.fail_flag = False
        self.read_file(self.file_path)
        if not self.fail_flag:
            os.remove(self.file_path)

    def __create_default_file(self):
        feeds = ET.Element('feeds')

        example_news = ET.SubElement(feeds, "feed")
        example_news.set("type", "N")
        example_news.set("id", "1")
        news_text = ET.SubElement(example_news, "text")
        news_text.text = "This IS the eXAMple of task 9! news text"
        news_city = ET.SubElement(example_news, "city")
        news_city.text = "Prague"

        example_ads = ET.SubElement(feeds, "feed")
        example_ads.set("type", "A")
        example_ads.set("id", "2")
        ads_text = ET.SubElement(example_ads, "text")
        ads_text.text = "This IS the eXAMple of task 9! aDS text"
        ads_city = ET.SubElement(example_ads, "city")
        ads_city.text = "Brno"
        ads_expired = ET.SubElement(example_ads, "expired")
        ads_expired.text = "2024-01-01"

        example_tweet = ET.SubElement(feeds, "feed")
        example_tweet.set("type", "T")
        example_tweet.set("id", "3")
        tweet_text = ET.SubElement(example_tweet, "text")
        tweet_text.text = "This IS the eXAMple of task 9! twEET text"
        tweet_author = ET.SubElement(example_tweet, "author")
        tweet_author.text = "Unknown"

        tree = ET.ElementTree(feeds)
        tree.write(DEFAULT_FILENAME)

    def read_file(self, filepath):
        tree = ET.parse(filepath)
        root = tree.getroot()
        for feed in root.iter("feed"):
            if feed.attrib["type"] == "N":
                text = capitalize_string(feed.find("text").text)
                city = feed.find("city").text
                News(text, city)
            elif feed.attrib["type"] == "A":
                text = capitalize_string(feed.find("text").text)
                city = feed.find("city").text
                expired = feed.find("expired").text
                Ads(text, city, expired)
            elif feed.attrib["type"] == "T":
                text = capitalize_string(feed.find("text").text)
                author = feed.find("author").text
                Tweet(text, author)
            else:
                self.fail_flag = True
                print("Unsupported feed content: ", feed)
