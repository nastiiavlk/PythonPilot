import os
from Task4 import capitalize_string
from Task5 import News, Tweet, Ads

DEFAULT_FILENAME = 'Task6_default.txt'


class FeedTXT:
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
            content = ("N\n"
                       "THIS IS the DEFAULT! news text\n"
                       "Prague\n"
                       "$A\n"
                       "THIS IS the DEFAULT! aDS text\n"
                       "Brno\n"
                       "2024-01-01\n"
                       "$T\n"
                       "THIS IS the DEFAULT! twEET text\n"
                       "Unknown\n"
                       )
            default_file.write(content)

    def read_file(self, filepath):
        with open(filepath, 'r') as file:
            feeds = file.read()
            for feed in feeds.split('$'):
                lines = feed.split('\n')
                if lines[0] == "N":
                    text = capitalize_string(lines[1])
                    city = lines[2]
                    News(text, city)
                elif lines[0] == "A":
                    text = capitalize_string(lines[1])
                    city = lines[2]
                    expired = lines[3]
                    Ads(text, city, expired)
                elif lines[0] == "T":
                    text = capitalize_string(lines[1])
                    author = lines[2]
                    Tweet(text, author)
                else:
                    self.fail_flag = True
                    print("Unsupported feed content: ", feed)
