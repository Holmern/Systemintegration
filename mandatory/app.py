from bottle import get, run, view, default_app, request, route
import jwt
import time

##############################
def jwtFunc():
    cpr = "12345"
    iat = int(time.time())
    exp = iat + 600
    encoded_jwt = jwt.encode({"cpr": cpr, "iat": iat, "exp": exp}, "secret", algorithm ="HS256")
    print(encoded_jwt)
    return encoded_jwt


##############################
@get("/")
@view("index")
def _():
    return jwtFunc()


##############################
@route('/jwt', method='POST')
def get_jwt():
    queryString = request.forms.get("queryString")
    print ('queryString is:', queryString)
    return "<p>Your jwt information was correct.</p>"
##############################


try:
    import production
    application = default_app()
except:
    run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")