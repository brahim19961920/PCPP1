#!/usr/bin/env python

import sqlite3


def main():
    db = ToDoDB()
    db.add_task()
    db.show_tasks()


class ToDoDB:
    def __init__(self):
        self.conn = sqlite3.connect("tasks.db")
        self.c = self.conn.cursor()
        self.create_db()

    def create_db(self):
        self.c.execute(
            """CREATE TABLE IF NOT EXISTS tasks 
        (id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        priority INTEGER NOT NULL); """
        )
        self.conn.commit()

    def add_task(self):
        name = input("Enter task name: ")
        if self.find_task(name):
            print(f'Skipping, "{name}" task already exists')
            return

        if not name:
            print("Skipping, cannot add an empty task.")
            return

        priority = int(input("Enter priority: "))
        if priority < 1:
            print("Skipping, cannot add a task with a priority less than 1.")
            return

        self.c.execute("INSERT INTO tasks (name, priority) VALUES (?,?)", (name, priority))
        self.conn.commit()
        print("Task added successfully")

    def find_task(self, test):
        records = self.c.execute(f"SELECT id, name, priority from tasks where name ='{test}'").fetchall()
        return records if records else None

    def show_tasks(self):
        print("Showing all taks in the DB:")
        for task in self.c.execute("SELECT * from tasks"):
            print(task)


if __name__ == "__main__":
    main()
