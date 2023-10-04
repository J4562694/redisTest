from flask import Blueprint, abort
from app.module.redisCli import redisCli
import redis

router=Blueprint('test', __name__)

@router.route('/')
def index():

    # 從redis讀取資料出來
    try:
        dict_1 = []
        key = 'Lamp_2','EPower_water2',"EPower_r","EPower_s","EPower_t","EPower_rs",'0','1'
        for item in range(len(key)):
            value = redisCli.hgetall(key[item])
            print({key[item]:value})
            dict_1.append(value)
        return  dict_1
    except Exception as e:
        print(e)
        abort(404)
