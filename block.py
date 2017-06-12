import hashlib
from . import block_params


class Block():

    def __init__(self, params):
        self.index = params.index
        self.previous_hash = params.previous_hash
        self.timestamp = params.timestamp
        self.data = params.data
        self.hash = self.calc_hash()

print('hey, I work!')
