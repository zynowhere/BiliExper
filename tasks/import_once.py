from BiliClient import asyncbili
import time

ids = None
async def get_ids(biliapi: asyncbili):
    '''全局单例ids，避免重复请求'''
    global ids
    if not ids:
        ids = await biliapi.getRegions()
    return ids

now_time = int(time.time()) #第一次加载模块的时间
taday = time.localtime(now_time + 28800 + time.timezone).tm_mday #今天是几号