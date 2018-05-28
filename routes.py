from bottle import HTTPResponse, abort, request, get
from tinydb import TinyDB, Query
import json

db = TinyDB("db.json")
table = db.table("subway")
Data = Query()
#i = 0
res ={}


@get('/search')
def search():

    # パラメータを取得
    name = request.params.name
    types = request.params.type

    # nameパラメータに値が入っているのかを確認
    if name:
        # typeパラメータに値が存在するか判定
        if types:
            # name,typeパラメータ共に値が存在するとき
            get_data = table.search((Data.name == name) & (Data.type == types))
        else:
            # nameパラメータのみに値が存在するとき
            get_data = table.search(Data.name == name)

    else:
        # typeパラメータに値が存在するか判定
        if types:
            # typeパラメータのみに値が存在するとき
            get_data = table.search(Data.type == types)
        else:
            # パラメータが指定されていない場合、全てのエントリを返す
            get_data = table.all()

    i = 0
    for row in get_data:
        res[i] = row
        i = i + 1

    body = json.dumps(res)

    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')

    return r