# -*- coding: UTF-8 -*-
"""
__Author__ = "Fork WECENG" && "Samsepi0l"
__Version__ = "1.1.0"
__Description__ = "大麦抢票脚本"
__Created__ = 2023/10/10 17:12
__Modified__ = 2024/11/10 23:08
"""
import json
import time

from concert import Concert
from config import Config


def load_config():
    with open('config.json', 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)
    return Config(config['index_url'],
                  config['login_url'],
                  config['target_url'],
                  config['users'],
                  config['city'],
                  config['dates'],
                  config['prices'],
                  config['if_listen'],
                  config['if_commit_order'])


def grab():
    # 加载配置文件
    config = load_config()
    # 初始化
    con = Concert(config)
    try:
        # 进入页面
        con.enter_concert()
        # 抢票
        con.choose_ticket()
        # 页面停留5分钟
        time.sleep(300)
    except Exception as e:
        print("get tickets error: {}".format(e))
        con.finish()


# exec
grab()
