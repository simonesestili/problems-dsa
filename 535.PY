from string import digits, ascii_lowercase as lowercase, ascii_uppercase as uppercase
from random import choices
class Codec:
    def __init__(self):
        self.map = {}
        self.characters = ''.join([digits, lowercase, uppercase])

    def encode(self, long):
        code = self.generate_code()
        self.map[code] = long
        return code

    def decode(self, short):
        return self.map[short]

    def generate_code(self):
        return ''.join(choices(self.characters, k=8))
