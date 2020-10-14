from sqlalchemy import create_engine, inspect, text
import os
from collections import OrderedDict


DATABASE_URL = os.environ.get('DATABASE_URL')


class Record(object):
    __slots__ = ('_keys', '_values')

    def __init__(self, keys, values):
        self._keys = keys
        self._values = values

        assert len(self._keys) == len(self._values)

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def __repr__(self):
        return '<Record {}>'.format(str(zip(self._keys, self._values)))

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.values()[key]

        if key in self.keys():
            i = self.keys().index(key)
            return self.values()[i]

        raise KeyError("Record contains no '{}' field.".format(key))

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError(e)

    def __dir__(self):
        standard = dir(super(Record, self))
        return sorted(standard + [str(k) for k in self.keys()])

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def as_dict(self, ordered=False):
        items = zip(self.keys(), self.values())
        return OrderedDict(items) if ordered else dict(items)








class Database(object):
    def __init__(self, db_url=None, **kwargs):
        self.db_url = db_url or DATABASE_URL

        if not self.db_url:
            raise ValueError('You must provide a db_url.')

        self._engine = create_engine(self.db_url, **kwargs)
        self.db = self._engine.connect()
        self.open = True

    def close(self):
        self.db.close()
        self.open = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __repr__(self):
        return '<Database open={}>'.format(self.open)

    def get_tbale_name(self, internal=False):
        return inspect(self._engine).get_table_names()

    def query(self, query, fetchall=False, **params):
        cursor = self.db.execute(text(query), **params)
        row_gen = (Record(cursor.keys(), row) for row in cursor)
        








