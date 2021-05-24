from BiliClient import asyncbili
from .push_message_task import webhook
from .import_once import taday
import logging

async def vip_task(biliapi: asyncbili,
                   task_config: dict
                   ) -> None:
    if taday == 1:
        try:
            ret = await biliapi.vipPrivilegeReceive(1)
            if ret["code"] == 0:
                logging.info(f'{biliapi.name}: 成功领取大会员B币')
            else:
                logging.warning(f'{biliapi.name}: 领取大会员B币失败，信息为({ret["message"]})')
                webhook.addMsg('msg_simple', f'{biliapi.name}:领取B币劵失败\n')
        except Exception as e:
            logging.warning(f'{biliapi.name}: 领取大会员B币异常，原因为({str(e)})')
            webhook.addMsg('msg_simple', f'{biliapi.name}:领取B币劵失败\n')

        try:
            ret = await biliapi.vipPrivilegeReceive(2)
            if ret["code"] == 0:
                logging.info(f'{biliapi.name}: 成功领取大会员优惠券')
            else:
                logging.warning(f'{biliapi.name}: 领取大会员优惠券失败，信息为({ret["message"]})')
                webhook.addMsg('msg_simple', f'{biliapi.name}:领取优惠劵失败\n')
        except Exception as e:
            logging.warning(f'{biliapi.name}: 领取大会员优惠券异常，原因为({str(e)})')
            webhook.addMsg('msg_simple', f'{biliapi.name}:领取优惠劵失败\n')

    elif taday == 28:
        if not 'BpCharge' in task_config or not task_config["BpCharge"]:
            return

        for x in task_config["BpCharge"]:
            if not task_config["BpCharge"][x] > 0:
                continue

            if x == 'charge':
                try:
                    cbp = (await biliapi.getUserWallet())["data"]["couponBalance"] #B币劵数量
                    if cbp > 0:
                        cbp = cbp if cbp < task_config["BpCharge"][x] else task_config["BpCharge"][x]
                        ret = await biliapi.elecPayBcoin(biliapi.uid, cbp)
                        if ret["data"]["order_no"]:
                            logging.info(f'{biliapi.name}: 成功用{cbp}张B币劵给自己充电，订单编号为{ret["data"]["order_no"]}')
                        else:
                            logging.warning(f'{biliapi.name}: 给自己充电失败，信息为{ret["data"]["msg"]}')
                            webhook.addMsg('msg_simple', f'{biliapi.name}:充电失败\n')
                    else:
                        logging.info(f'{biliapi.name}: B币劵数量为0，跳过给自己充电')
                except Exception as e:
                    logging.warning(f'{biliapi.name}: 获取账户B币劵并给自己充电异常，原因为{str(e)}')
                    webhook.addMsg('msg_simple', f'{biliapi.name}:充电失败\n')

            elif x == 'Bp2Gold':
                try:
                    cbp = (await biliapi.getUserWallet())["data"]["couponBalance"]
                    if cbp > 0:
                        cbp = cbp if cbp < task_config["BpCharge"][x] else task_config["BpCharge"][x]
                        ret = await biliapi.xliveBp2Gold(cbp)
                        if ret["code"] == 0:
                            logging.info(f'{biliapi.name}: 成功将{cbp}张B币劵兑换为金瓜子，订单编号为{ret["data"]["order_id"]}')
                        else:
                            logging.warning(f'{biliapi.name}: 将B币劵兑换为金瓜子失败，信息为{ret["message"]}')
                            webhook.addMsg('msg_simple', f'{biliapi.name}:兑换金瓜子失败\n')
                    else:
                        logging.info(f'{biliapi.name}: B币劵数量为0，跳过兑换金瓜子')
                except Exception as e:
                    logging.warning(f'{biliapi.name}: 获取账户B币劵并兑换金瓜子异常，原因为{str(e)}')
                    webhook.addMsg('msg_simple', f'{biliapi.name}:兑换金瓜子失败\n')
