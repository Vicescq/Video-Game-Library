from flask import Flask
from AppClasses import IGDB



app = Flask(__name__)

@app.route("/")
def home():
    IgdbInstance = IGDB()
    IgdbInstance.init_token
    #return IgdbInstance.search("persona")
    return IgdbInstance.get_game_img(266008)


    


if __name__ == "__main__":
    app.run()