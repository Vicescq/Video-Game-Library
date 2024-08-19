import os, requests
from dotenv import load_dotenv
load_dotenv()


"""
TODO:
    CREATE DATABASE AND IMPLEMENT TOKEN REFRESH
    PROPER ERROR HANDLING
"""


class IGDB:
    def __init__(self):
        self._error_code = 1
        """
        Error codes
        0 -> Good
        1 -> No connection to API
        """

        self._token = ""
        self._base_endpoint = "https://api.igdb.com/v4/"
        self._endpoint = "" 
        self._headers = {}
        self._body = ""
    
    @property
    def token(self):
        return self._token
    @token.setter
    def token(self, value):
        self._token = value
    @property
    def init_token(self):
        endpoint = "https://id.twitch.tv/oauth2/token"
        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("CLIENT_SECRET")
        body = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        }
        token_res = requests.post(endpoint, data=body)
        token = token_res.json()["access_token"]
        self.token = token

        # setting the header due to token being retrieved
        self.headers = {
            "Client-ID": client_id,
            "Authorization": f"Bearer {self.token}"
        }


    # Getter and Setters
    @property
    def error_code(self):
        return self._error_code
    @error_code.setter
    def error_code(self, value):
        self._error_code = value

    @property
    def base_endpoint(self):
        return self._base_endpoint

    @property
    def endpoint(self):
        return self._endpoint
    @endpoint.setter
    def endpoint(self, value):
        self._endpoint = value

    @property
    def headers(self):
        return self._headers
    @headers.setter
    def headers(self, value):
        self._headers = value

    @property
    def body(self):
        return self._body
    @body.setter
    def body(self, value):
        self._body = value


    # Methods
    def search(self, game_query: str):
        self.endpoint = self.base_endpoint + "games"
        self.body = """
                search "{}";
                fields *;
                limit 15;
                exclude checksum, collection, created_at, follows, forks, game_engines, hypes, rating, rating_count, screenshots, slug, total_rating, total_rating_count, updated_at, version_parent, version_title, videos;
        """.format(game_query)
        return requests.post(self.endpoint, headers=self.headers, data=self.body).json()
    



class Game:
    def __init__(self):
        pass