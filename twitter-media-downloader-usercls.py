import json
import os
import shutil
import time

from common.console import process_data, read_data
from common.redisCli import getConnection
from common.tools import getUserId

r = getConnection()

if __name__ == '__main__':
    url_list = (read_data('data.hot'))
    for u in url_list:
        res = getUserId(u.split("/")[0])
        if res is not None:
            r.set("u:suc:"+u,json.dumps(url_list, ensure_ascii=False))
        else:
            r.set("u:fail:"+u,"")
        time.sleep(10)

