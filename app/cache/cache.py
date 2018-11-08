from datetime import datetime

class Cache():
    def set(self, key, value):
        raise NotImplementedError("Should have implemented this")

    def get(self, key):
        raise NotImplementedError("Should have implemented this")

class SimpleCache(Cache):

    def __init__(self):
        # A cache is a library of Id: Datetime
        self.cache = {}

    def set(self, key, value):
        self.cache[id] = value

    def get(self, key):

        try:
            till = self.cache[id]
            if till > datetime.now():
                return till
            else:
                # not valid anymore, remove it from the cache
                self.cache.pop(id)
        except KeyError:
            pass
