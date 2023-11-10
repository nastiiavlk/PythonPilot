import os, json
from Task4 import capitalize_string
from Task5 import News, Tweet, Ads

DEFAULT_FILENAME = 'Task8_default.json'


class FeedJSON:
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
        with open(DEFAULT_FILENAME, 'w') as default_file:
            content = {
                "feeds": [
                    {
                        "id": 1,
                        "type": "N",
                        "text": "This IS the eXAMple of task 8! news text",
                        "city": "Prague"
                    },
                    {
                        "id": 2,
                        "type": "A",
                        "text": "This IS the eXAMple of task 8! aDS text",
                        "city": "Brno",
                        "expired": "2024-01-01"
                    },
                    {
                        "id": 3,
                        "type": "T",
                        "text": "This IS the eXAMple of task 8! twEET text",
                        "author": "Unknown"
                    }
                ]
            }
            json_data = json.dumps(content)
            default_file.write(json_data)

    def read_file(self, filepath):
        with open(filepath, 'r') as file:
            feeds = json.load(file)
            for feed in feeds['feeds']:
                if feed['type'] == "N":
                    text = capitalize_string(feed['text'])
                    city = feed['city']
                    News(text, city)
                elif feed['type'] == "A":
                    text = capitalize_string(feed['text'])
                    city = feed['city']
                    expired = feed['expired']
                    Ads(text, city, expired)
                elif feed['type'] == "T":
                    text = capitalize_string(feed['text'])
                    author = feed['author']
                    Tweet(text, author)
                else:
                    self.fail_flag = True
                    print("Unsupported feed content: ", feed)
