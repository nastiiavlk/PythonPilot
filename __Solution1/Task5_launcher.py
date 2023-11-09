import os
from Task5 import News, Tweet, Ads
from Task6 import FeedTXT
from Task8 import FeedJSON
from Task9 import FeedXML
from common import FILENAME


class Launcher:
    def __init__(self):
        self.active = True
        while self.active:
            print("Main menu")
            self.__main_menu()

    def __main_menu(self):
        menu_msg = """Choose action :
            1. Add Feed
            2. Add from External file
            3. Read Feeds
            4. Exit
            """
        choice = int(input(menu_msg))
        if choice == 1:
            print("Add Menu")
            self.__add_menu()
        elif choice == 2:
            print("Add from External file Menu")
            self.__add_external_menu()
        elif choice == 3:
            self.read_file()
            input("Press Enter to continue...")
            print("Main menu")
            self.__main_menu()
        elif choice == 4:
            self.active = False

    @staticmethod
    def read_file():
        if not os.path.exists(FILENAME):
            print("There is no feed so far")
            return
        with open(FILENAME, 'r') as file:
            content = file.read()
            print(content)

    def __add_external_menu(self):
        menu_msg = """Choose action:
            1. Add from txt
            2. Add from json
            3. Add from xml
            4. Back
            """
        choice = int(input(menu_msg))
        if choice == 1:
            print("Adding from TXT file: ")
            file_path = input("Provide File Path, left empty for default file: ")
            FeedTXT(file_path)
        elif choice == 2:
            print("Adding from JSON file: ")
            file_path = input("Provide File Path, left empty for default file: ")
            FeedJSON(file_path)
        elif choice == 3:
            print("Adding from XML file: ")
            file_path = input("Provide File Path, left empty for default file: ")
            FeedXML(file_path)
        elif choice == 4:
            print("Main menu")
            self.__main_menu()

    def __add_menu(self):
        menu_msg = """Choose action :
            1. Add News
            2. Add Ads
            3. Add Tweet
            4. Back
            """
        choice = int(input(menu_msg))
        if choice == 1:
            print("Adding a NEWS: ")
            text = input("Provide News text: ")
            city = input("Provide News city: ")
            News(text, city)
        elif choice == 2:
            print("Adding an ADS: ")
            text = input("Provide Ads text: ")
            city = input("Provide Ads city: ")
            expired = input("Provide Ads expiration date YYYY-MM-DD format: ")
            Ads(text, city, expired)
        elif choice == 3:
            print("Adding a TWEET: ")
            text = input("Provide TWEET text: ")
            author = input("Provide TWEET author: ")
            Tweet(text, author)
        elif choice == 4:
            print("Main menu")
            self.__main_menu()


if __name__ == "__main__":
    Launcher()
