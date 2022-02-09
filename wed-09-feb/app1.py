from http import server
from unittest import result
from bottle import delete, error, get, hook, response, run, post, request, put
import json
import uuid

items = [
    {"id":"ec060aeb-3ff7-4f36-93f1-8ca9d7385707",
    "name":"a",
    "last_name":"b"}
]
############################## HOOK AFTER REQUEST ##############################
@hook("after_request")
def _():
    response.content_type = "application/json"


############################## GET HOME ##############################
@get("/")
def _():
    return "home"
############################## GET ITEMS ##############################
@get("/items")
def _():
    return json.dumps(items)
############################## POST ITEMS ##############################
@post("/items")
def _():
    item_id = str(uuid.uuid4())
    item_name = request.json.get("name")
    item = {"id":item_id, "name":item_name}
    items.append(item)
    print(type(item_id))
    response.status = 201
    return {"id":item_id}


############################## DELETE SPECIFIC ITEM ##############################
@delete("/items/<item_id>")
def _(item_id):
    for index, item in enumerate(items): # 
        if item["id"] == item_id:
            items.pop(index)
            return {"info":"item deleted"}
    
    response.status = 204
    return 
    #204 Doesnt care about you
    # json.dumps({"info":f"Item with id {item_id} not found"})

############################## GET SPECIFIC ITEM ##############################
'''@get("/items/<item_id>")
def _(item_id):
    for item in items:
        if item["id"] == item_id:
            return json.dumps(items)
    return'''

#List Comprehension
@get("/items/<item_id>")
def _(item_id):
    # [Return value     Loop    condition]
    matches = [item for item in items if item["id"] == item_id]
    if not matches:
        response.status = 204
        return

    return matches[0]

############################## PUT ITEM ##############################
@put("/items/<item_id>")
def _(item_id):
    try:
        item = [item for item in items if item["id"] == item_id][0]
        if not request.json.get("name"):
            pass
        else:
            item["name"] = request.json.get("name")
        
        if not request.json.get("last_name"):
            pass
        else:
            item["last_name"] = request.json.get("last_name")       
        return item
    except Exception as ex:
        print(ex)
        response.status = 204
        return

############################## Error ITEMS 404 ##############################
@error(404)
def _(error):
    response.content_type = "application/json"
    return json.dumps({"info":"page not found"})

############################## RUN ##############################
# Create webservern, on Port, debug?, reloader keeps server alive
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")