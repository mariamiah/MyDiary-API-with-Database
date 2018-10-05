from flask import Flask
import psycopg2

# Connect to the database


class Databaseconnection:

    def set_up_database(self):
        """ This function sets up a database connection"""
        self.conn = psycopg2.connect(host="localhost",
                                     database="mydiarydatabase",
                                     user="postgres", password="123")
        return self.conn

    def create_cursor(self):
        """ This function creates a cursor object """
        self.cur = self.conn.cursor()
        return self.cur

    def create_users_table(self):
        """ This function creates a users table in the mydiary database"""
        Users_table = """create table if not exists users(user_id serial PRIMARY KEY NOT NULL,
                                             user_name VARCHAR NOT NULL,
                                             email VARCHAR,
                                             password VARCHAR
                                             )"""
        self.cur.execute(Users_table)

    def create_diaries_table(self):
        """ This function creates an diaries table in the database"""
        Diaries_table = """create table if not exists diaries(diary_id serial PRIMARY KEY NOT NULL,
                                             diary_name VARCHAR NOT NULL,
                                             date_created TIMESTAMP
                                             )"""
        self.cur.execute(Diaries_table)

    def create_entries_table(self):
        """ This function creates an entries table in the database"""
        Entries_table = """create table if not exists entries(entry_id serial PRIMARY KEY NOT NULL,
                                                     entry_text VARCHAR,
                                                     date_created TIMESTAMP
                                                     )"""
        self.cur.execute(Entries_table)

    def close_database_connection(self):
        self.conn.commit()
        self.conn.close()

db = Databaseconnection()
db.set_up_database()
db.create_cursor()
db.create_users_table()
db.create_diaries_table()
db.create_entries_table()
db.close_database_connection()
