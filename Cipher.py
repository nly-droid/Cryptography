class Cipher:

    def __init__(self, key):
        self.name = ""
        self.key = key

    def __str__(self):
        return f"This is {self.name} cipher."

    def decipher(self, cipher):
        pass

    def encipher(self, cipher):
        pass

    def change_key(self, key):
        self.key = key
        return
