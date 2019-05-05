"""Manages persisting data onto disk, things like
templates and dynamic configuration details.
"""

from pymongo import MongoClient
from faqbot.config import *
import copy

client = MongoClient(MONGO_URL)
db = client.get_database()
collection = db.settings

def save_config(store, name):
    """Give it a dictionary of your config,
    and a name of your config and it'll save it ;)
    """
    collection.replace_one({
        "name": name
    }, {
        "name": name,
        "data": store
    }, upsert=True)

def load_config(name):
    """Load back the stored configs.
    Again, pass in the name of your config.
    """
    return collection.find_one({
        "name": name
    })["data"]


def gen_defaults(defaults, name):
    """Pass it defaults, and it'll check if the
    config store already exists, if it doesn't
    it'll dump the defaults.
    """
    if not collection.find_one({"name": name}):
        store = copy.deepcopy(defaults)
        save_config(store, name)
    else:
        # We know the store exists, but see if any new
        # keys popped up in defaults.
        loaded_config = load_config(name)
        new_keys = set(defaults.keys()) - set(loaded_config.keys())

        for new_key in new_keys:
            loaded_config[new_key] = copy.deepcopy(defaults[new_key])

        save_config(loaded_config, name)


class Store(object):
    """Neat wrapper interface for accessing
    store configs. Use as,

        with s as Store('stats'):
            s['something'] = something

    """

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.store = load_config(self.name)
        return self

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __exit__(self, type, value, traceback):
        save_config(self.store, self.name)
