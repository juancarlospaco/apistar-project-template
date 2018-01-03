#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""BaseModel for all models, with a PooledPostgresqlExtDatabase connection."""


from datetime import datetime
from uuid import uuid4

from peewee import DateTimeField

from apistar_peewee import get_model_base


Model = get_model_base()


class BaseModel(Model):

    def __repr__(self):
        try:  # Try to get all the fields on the model for the str repr.
            all_the_fields = self._meta.fields.keys()
        except Exception:
            all_the_fields = ""
        return (f'{self.__class__.__name__}(uuid={self.uuid}, '
                f'timestamp={self.timestamp}, {all_the_fields})')
