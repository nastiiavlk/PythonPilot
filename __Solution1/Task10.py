import sqlite3
from common import DB_NAME


class DBWriter:
    def __init__(self, type, args):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()
        self.write_to_db(type, args)
        self.cursor.close()
        self.connection.close()

    def write_to_db(self, type, args):
        if type == 'N':
            self.cursor.execute('create table if not exists news (text TEXT, city TEXT, date TEXT)')
            self.cursor.execute('select count(*) from news where text = ? and city = ?', (args[0], args[1]))
            if self.cursor.fetchone()[0] == 0:
                print("Inserting news to db: ", args)
                self.cursor.execute('insert into news(text, city, date) values (?, ?, ?)', (args[0], args[1], args[2]))
                self.connection.commit()
            else:
                print("The news is duplicate")
        elif type == 'A':
            self.cursor.execute('create table if not exists ads (text TEXT, city TEXT, expired TEXT, days_left INT)')
            self.cursor.execute('select count(*) from ads where text = ? and city = ? and expired = ?',
                                (args[0], args[1], args[2]))
            if self.cursor.fetchone()[0] == 0:
                print("Inserting ads to db: ", args)
                self.cursor.execute('insert into ads(text, city, expired, days_left) values (?, ?, ?, ?)',
                                    (args[0], args[1], args[2], args[3]))
                self.connection.commit()
            else:
                print("The ads is duplicate")
        elif type == 'T':
            self.cursor.execute('create table if not exists tweet (text TEXT, author TEXT, length INT)')
            self.cursor.execute('select count(*) from tweet where text = ? and author = ?', (args[0], args[1]))
            if self.cursor.fetchone()[0] == 0:
                print("Inserting tweet to db: ", args)
                self.cursor.execute('insert into tweet(text, author, length) values (?, ?, ?)',
                                    (args[0], args[1], str(args[2])))
                self.connection.commit()
            else:
                print("The tweet is duplicate")
