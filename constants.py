API_KEY = '#####'  # REPLACE WITH YOUR API KEY
API_URL = 'https://api.hypixel.net/'
UUID_RESOLVER = 'https://sessionserver.mojang.com/session/minecraft/profile/'
KEY_LENGTH = 36


class Setter:

    @staticmethod
    def set_api_key(key):
        API_KEY = key
