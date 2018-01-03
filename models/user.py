#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""User Data model, with all possible attributes it can have.

Copied, simplified and Adapted from:
https://github.com/django/django/blob/master/django/contrib/auth/models.py
"""


from datetime import date, datetime

import pyotp
from peewee import BooleanField, CharField, DateTimeField, FixedCharField
from peewee_extra_fields import (CountryISOCodeField, LanguageISOCodeField,
                                 PastDateField, PositiveSmallIntegerField)
from playhouse.fields import PasswordField

from models.base import BaseModel


class User(BaseModel):

    """User Model,with 2 Factor Auth (TOTP 2FA) for FreeOTP and profile data."""

    MAX_LEN = 128  # Maximum Lenght for Charfields on the class. Up to 255 is Ok.

    # User personal data.
    username = CharField(max_length=MAX_LEN, unique=True, help_text=f'Username, {MAX_LEN} characters max, required')
    password = PasswordField(help_text=f'Password, from 8 to {MAX_LEN} characters, required')
    email = CharField(max_length=MAX_LEN, help_text='Email address, required')
    first_name = CharField(max_length=MAX_LEN, null=True, help_text='First name')
    last_name = CharField(max_length=MAX_LEN, null=True, help_text='Last name')
    company = CharField(max_length=MAX_LEN, null=True, help_text='Company')
    bio = CharField(max_length=MAX_LEN, null=True, help_text='Biography')
    url_home = CharField(max_length=MAX_LEN, null=True, help_text="Web Homepage")
    totp_secret = FixedCharField(max_length=16, default=pyotp.random_base32, help_text='OTP Secret, 16 characters, required')

    # Dates and Times for the User.
    date_joined = PastDateField(default=date.today, help_text="Sign-Up Date")
    last_login = DateTimeField(default=datetime.utcnow, help_text="Last Sign-In Date & Time")
    bday = PastDateField(null=True, help_text="Birthday Date")

    # Boolean attributes to define permissions by combining them.
    is_active = BooleanField(default=True, help_text="Is the User active?")
    is_staff = BooleanField(default=False, help_text="Is the User part of the Staff?")
    is_guest = BooleanField(default=False, help_text="Is the User a Guest?")
    is_admin = BooleanField(default=False, help_text="Is the User an Admin?")

    # Misc.
    likes = PositiveSmallIntegerField(default=0, help_text="Likes")          # 32K max
    country = CountryISOCodeField(default="ar", help_text="Preferred Country")
    language = LanguageISOCodeField(default="es", help_text="Preferred Language")

    def __str__(self) -> str:
        return self.username

    def set_password(self, password) -> bool:
        self.password = password
        return self.save()

    def check_password(self, password) -> bool:
        return self.password.check_password(password)

    def set_totp_secret(self) -> bool:
        self.totp_secret = pyotp.random_base32()
        return self.save()

    def check_pin(self, pin) -> bool:
        return bool(pyotp.TOTP(self.totp_secret).verify(pin, valid_window=1))
