from bottle import get, run, view, default_app
import jwt, time, random, requests
from get_api_key import api_key

##############################
@get("/")
@view("index")
def _():
    return


##############################
try:
    import production
    application = default_app()
except:
    run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")