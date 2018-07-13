"""Manages persisting data onto disk, things like
templates and dynamic configuration details.
"""

from faqbot.legacy.faq import COMMANDS
from faqbot.core.defaults import DEFAULTS

import pickle
import copy
import os

STORE_DIRECTORY = 'store'

def store_path(name):
    """Internal function."""

    return os.path.join(STORE_DIRECTORY, name + '.p')

def save_config(store, name):
    """Give it a dictionary of your config,
    and a name of your config and it'll save it ;)
    """
    pickle.dump(store, open(store_path(name), 'w'))

def load_config(name):
    """Load back the stored configs.
    Again, pass in the name of your config.
    """

    return pickle.load(open(store_path(name)))

def gen_defaults(defaults, name):
    """Pass it defaults, and it'll check if the
    config store already exists, if it doesn't
    it'll dump the defaults.
    """

    if not os.path.exists(store_path(name)):
        store = copy.deepcopy(defaults)
        save_config(store, name)

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