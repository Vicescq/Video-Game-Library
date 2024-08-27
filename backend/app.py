import requests
from flask import Flask
from AppClasses import IGDB
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
IGDB_INSTANCE = IGDB()

@app.route("/quick_search")
def quick_search():
    query =  requests.args.get("query")
    IGDB_INSTANCE.quick_search(query)
    return IGDB_INSTANCE.data

@app.route("/dev")
def dev():
    IGDB_INSTANCE.init_token()
    IGDB_INSTANCE.quick_search("final fantasy")
    return IGDB_INSTANCE.data

if __name__ == "__main__":
    app.run(debug=True)
    IGDB_INSTANCE.init_token()