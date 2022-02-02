from bottle import run, error, get

##############################
@get("/")
def _():
    return "My First MicroService"


##############################
@error(404)
def _(error):
    print(type(error))
    print(dir(error))
    return "Uppps... Page not Found"

##############################

run(host="127.0.0.1", port=3333, debug=True, reloader=True) #Always Last