from datetime import datetime
import os

OUTPUT_FILENAME = "6_content_feed.txt"
INPUT_FOLDER = "input"
INPUT_FILENAME = "input_file.txt"


class Base:
    def __init__(self, filename: str = OUTPUT_FILENAME) -> None:
        self._filename = filename

    def _write_to_file(self, output: str): 
        # When we want to denominate a "private" function, 
        # we use _ although private functions don't exist in Python
        with open(self._filename, "a") as f:
            f.write(output)


class News(Base):
    _CONTENT = "News\n-----------------------------\n{text}\n{city}, {date}\n\n"

    def __init__(self, text: str, city: str) -> None:
        super().__init__()
        self._text = text
        self._city = city

    def publish(self):
        output = self._CONTENT.format(
            text = self._text, 
            city = self._city,
            date = datetime.now()
        )
        self._write_to_file(output)


class PrivateAd(Base):
    _CONTENT = "Ad\n-----------------------------\n{text}\nActual until: {exp_date}, {left} days left\n\n"

    def __init__(self, text: str, exp_date: datetime) -> None:
        super().__init__()
        self._text = text
        self._exp_date = exp_date

    def publish(self):
        output = self._CONTENT.format(
            text = self._text, 
            exp_date = self._exp_date,
            left = (self._exp_date-datetime.now()).days
        )
        self._write_to_file(output)


class Joke(Base):
    _CONTENT = "Joke\n-----------------------------\n{text}\n\n"

    def __init__(self, text: str) -> None:
        super().__init__()
        self._text = text

    def publish(self):
        output = self._CONTENT.format(text = self._text) 
        self._write_to_file(output)


class Feed:
    def __init__(
            self, 
            output_f: str = OUTPUT_FILENAME, 
            input_f: str = INPUT_FILENAME,
            input_folder: str = INPUT_FOLDER,
        ) -> None:
        self._output_filename = output_f
        self._default_input = os.path.join(input_folder, input_f)

    def read_feed(self) -> None:
        try:
            with open(self._output_filename, "r") as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print("No records found in the news feed.")


    def publish(self) -> None:
        print("Select what to publish:")
        print("1. News\n2. Ad\n3. Joke")
        
        choice = input("Enter your choice (1/2/3): ")
        
        match choice: # match (switch) can be used in Python 3.10+
            case "1":
                text = input("Enter news text: ")
                city = input("Enter city: ")

                new_news = News(text, city)
                new_news.publish()
            case "2":
                text = input("Enter advertisement text: ")
                exp_date_str = input("Enter expiration date (DD-MM-YYYY): ")
                exp_date = datetime.strptime(exp_date_str, "%d-%m-%Y")

                new_ad = PrivateAd(text, exp_date)
                new_ad.publish()
            case "3":
                text = input("Enter joke text: ")

                new_joke = Joke(text)
                new_joke.publish()
            case _:
                print("Invalid choice.")

    def publish_file(self) -> None:
        file_path = input("File path (or press Enter to use '{}'): ".format(self._default_input)).strip()
        if not file_path:
            file_path = self._default_input

        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                file_content = f.read()
                file_content += "\n"
                print(file_content)
            self._write_to_file(file_content)
            os.remove(file_path)
            print("Added publications from file {} to file {}".format(file_path, self._output_filename))
        else:
            print("File not found")
        

    def _write_to_file(self, output: str): # This is done quick. Better to not reuse the code
        with open(self._output_filename, "a") as f:
            f.write(output)


def main():
    news_feed = Feed()
    
    while True:
        print("1. Publish\n2. Read Feed\n3. Publish from file\n4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        match choice: # match (switch) can be used in Python 3.10+
            case "1":
                news_feed.publish()
            case "2":
                news_feed.read_feed()
            case "3":
                news_feed.publish_file()
            case "4":
                break
            case _:
                print("Invalid choice.")


main()
