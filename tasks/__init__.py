#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Tasks Queue for APIStar, uses Huey, from Peewee Dev, simpler than Celery."""


#  https://huey.readthedocs.io Sqlite works Ok with Threads,uses Peewee.
from huey.contrib.sqlitedb import RedisHuey, SqliteHuey, crontab
from huey.exceptions import *

from settings import settings


huey: SqliteHuey = SqliteHuey(
    name=settings["HUEY"].get("NAME", "apistar"),
    filename=settings["HUEY"].get("FILENAME", 'huey_tasks_queue.db'),
)

# huey: RedisHuey = RedisHuey(
#     name=settings["HUEY"].get("NAME", "apistar"),
#     host=settings["HUEY"].get("HOST", '127.0.0.1'),
# )


@huey.task()
def example_task():
    print(f"This is a basic example Huey task from the queue using: {huey}.")


# https://huey.readthedocs.io/en/latest/api.html#crontab
@huey.periodic_task(crontab(month='*', day='*', day_of_week='*', hour='3', minute='0'))
def example_periodic_task():
    print(f"This is a example Huey periodic task from the queue using: {huey}")
