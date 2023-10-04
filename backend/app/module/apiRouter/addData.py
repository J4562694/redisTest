from flask import Blueprint, abort
from app.module.redisCli import redisCli

router=Blueprint('addData', __name__)

@router.route('/')
def index1():
    
    # 新增資料到redis
    try:
        hashData = {
            'chen' : "good",
            'chenChung' : "verygood",
            'chenJianChung' : 'prettygood!'
        }

        hashData1 = {
            'dog' : "cat",
            'coffee' : "tea",
            'sandwitch' : 'switch!'
        }

        dict_1 = [hashData, hashData1]

        for item in range(len(dict_1)):
            redisCli.hmset(item, dict_1[item])
        return 'verry good',201

    except Exception as e:
        print(e)
        abort(404)