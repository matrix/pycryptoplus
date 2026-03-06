try:
    from Crypto.Random import get_random_bytes
except ImportError:
    import os
    def get_random_bytes(n):
        return os.urandom(n)

class RandPool:
    def __init__(self):
        self.pool = b""

    def add_entropy(self, data):
        pass

    def get_bytes(self, n):
        return get_random_bytes(n)

def new(*args, **kwargs):
    return RandPool()
