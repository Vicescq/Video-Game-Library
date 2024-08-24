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
        self._data = {
            "status": {
                "code": 200,
                "reason": "OK",
            }
        }
        self._token = ""
        self._base_endpoint = "https://api.igdb.com/v4/"
        self._endpoint = "" 
        self._headers = {}
        self._body = ""
    
    
    # Getter and Setters
    @property
    def token(self):
        return self._token
    @token.setter
    def token(self, value):
        self._token = value
    
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value

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
    def init_token(self):
        endpoint = "https://id.twitch.tv/oauth2/token"
        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("CLIENT_SECRET")
        body = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        }
        response = requests.post(endpoint, data=body)
        if self.handle_response(response):
            token = response.json()["access_token"]
            self.token = token
            
            # setting the header due to token being retrieved
            self.headers = {
                "Client-ID": client_id,
                "Authorization": f"Bearer {self.token}"
            }
    
    def handle_response(self, response):
        try:
            response.raise_for_status()
            return True

        except requests.exceptions.HTTPError as err:
            self.data["data"] = {} # resetting everything since something went wrong
            self.data["status"]["code"] = err.response.status_code
            self.data["status"]["reason"] = err.response.reason
            
    def serialize_data(self, raw_data):
        self.data["data"] = raw_data

    def quick_search(self, game_query: str):
        self.endpoint = self.base_endpoint + "games"
        self.body = """
                search "{}";
                fields cover, first_release_date, name, url;
                where version_parent = null;
                limit 10;
        """.format(game_query)
        response = requests.post(self.endpoint, headers=self.headers, data=self.body)
        if self.handle_response(response):
            games = response.json()
            self.serialize_data(games)
            for i, game in enumerate(self.data["data"]):
                self.get_game_img(i, game["cover"])
            
    def get_game_img(self, i, cover_id):
        self.endpoint = self.base_endpoint + "covers"
        self.body = """
                fields *;
                where id = {};
        """.format(cover_id)
        response = requests.post(self.endpoint, headers=self.headers, data=self.body)
        if self.handle_response(response):
            hash = response.json()[0]["image_id"]
            img = f"https://images.igdb.com/igdb/image/upload/t_cover_big/{hash}.jpg"
            self.data["data"][i]["img"] = img
                
