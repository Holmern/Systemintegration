from bottle import get, run, view, default_app

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