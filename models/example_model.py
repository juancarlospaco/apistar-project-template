#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from peewee import (  # Types on the PostgreSQL Database.
    CharField,        # varchar
    TextField,        # text
    DateTimeField,    # timestamp
    IntegerField,     # integer
    BooleanField,     # boolean
    FloatField,       # real
    DecimalField,     # numeric
    ForeignKeyField,  # integer
    DateField,        # date
    TimeField,        # time
    TimestampField,   # integer
    BlobField,        # bytea
    UUIDField,        # uuid
)

from models.base import BaseModel


class ExampleModel(BaseModel):  # Delete this class is just an Example model :)
    name = CharField(help_text="Name")  # Write your own fields and models here
    number = IntegerField(help_text="Some Number or something")
