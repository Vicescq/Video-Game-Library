from flask import Flask
from AppClasses import IGDB



app = Flask(__name__)

@app.route("/")
def home():

    IgdbInstance = IGDB()
    IgdbInstance.init_token
    IgdbInstance.search("persona 5 royal")
    #IgdbInstance.get_game_img(266008)
    return IgdbInstance.data

    


if __name__ == "__main__":
    app.run()