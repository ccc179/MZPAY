import os
import time

import paramiko
from celery import shared_task

from OnlinePay.settings import BASE_DIR
from Pay.models import OrderList


@shared_task
def take_item(orderinfo):

    # getroleid_str = '''#!/bin/bash
    #
    #
    # java -cp /home/mhzx/mhzx_4095/gs/JMXTool.jar com.wanmei.mhzx.InvokeMethod 127.0.0.1 18608 controlRole kym IWEB:type=GameControl getRoleidByName java.lang.String ''' + orderinfo.get(
    #     'userid')
    # localpath = os.path.join(BASE_DIR, 'static/getroleid_str.sh')
    # with open(localpath, 'w', encoding='utf-8') as f:
    #     f.write(getroleid_str)
    trans = paramiko.Transport(('211.159.186.68', 22))
    trans.connect(username='root', password='str147852.')
    # filename = 'getroleid_str.sh'
    # path = '/home/mhzx/mhzx_4095/gs/'
    # remotepath = path + filename
    #
    # sftp = paramiko.SFTPClient.from_transport(trans)
    # sftp.put(localpath=localpath, remotepath=remotepath)
    # time.sleep(1)
    cmd = 'sh /home/mhzx/mhzx_4095/gs/getroleid_str.sh '+orderinfo.get('userid')

    # 将sshclient的对象的transport指定为以上的trans
    ssh = paramiko.SSHClient()
    ssh._transport = trans
    # 执行命令，和传统方法一样
    stdin, stdout, stderr = ssh.exec_command(cmd)
    response = stdout.read().decode('utf-8')
    # .split(str="=")[-1]
    response_id = str(response).split("=")[-1].strip()
    # 关闭连接
    print(response_id)
    # trans.close()
    time.sleep(1)
    '''
    :param orderinfo:
    :return: 负责物品发放，发放完毕后返回ok
    '''
    print("跳转成功")

    orders = OrderList.objects.filter(order_info=orderinfo)
    order = orders.first()
    if order.order_success == "0":  # 如果数据库里的seccess字段是0就执行发放。发放完毕后字段写成1
        print(orderinfo)
        userid = response_id
        realmoney = int(float(orderinfo.get('realmoney')))
        extdata = orderinfo.get('extdata')
        print("进入if语句")
        if extdata == "110" and realmoney == 1:#10:   110是金柳露210151109 ，10元999个
            count_item = '999'
            itemid = '210151109'
        elif extdata == "111" and realmoney == 1:#20:   111是金柳露210151109 ，20元2000个
            count_item = '2000'
            itemid = '210151109'
        elif extdata == "112" and realmoney == 1:#50:   112是金柳露210151109 ，50元6000个
            count_item = '6000'
            itemid = '210151109'
        elif extdata == "113" and realmoney == 1:#58:   113是三才勾玉210151112 ，58元999个
            count_item = '999'
            itemid = '210151112'
        elif extdata == "114" and realmoney == 1:#10:   114是人参果211401000 ，10元388个
            count_item = '388'
            itemid = '211401000'
        elif extdata == "115" and realmoney == 1:#50:   115是醒神丹211300000 ，10元388个
            count_item = '388'
            itemid = '211300000'
        elif extdata == "116" and realmoney == 1:#50:   116是顶级技能自选包254301051 ，10元10个
            count_item = '20'
            itemid = '254301051'
        elif extdata == "117" and realmoney == 1:#50:   117是顶级技能自选包254301051 ，20元25个
            count_item = '50'
            itemid = '254301051'
        print("开始生成字符串")
    #     danren_str = '''#!/bin/bash
    #
    #
    # LANG=en_US.UTF-8
    #
    # title="您有一条未读快递信息"
    # content="您赞助的礼包已准时送达！感谢使用梦诛快递！如有问题请联系群主QQ：2223099004"
    # itemid='''+itemid+'''
    # count='''+count_item+'''
    #
    # java -cp /home/mhzx/mhzx_4095/gs/JMXTool.jar com.wanmei.mhzx.InvokeMethod 127.0.0.1 18608 controlRole kym IWEB:type=GameControl mailItemAward long '''+userid+''' java.lang.String $title java.lang.String $content int $itemid int $count'''
    #     localpath = os.path.join(BASE_DIR, 'static/ceshi.sh')
    #     print("开始写入文件")
    #     with open(localpath,'w',encoding='utf-8') as f:
    #         f.write(danren_str)
    #     trans = paramiko.Transport(('211.159.186.68',22))
    #     trans.connect(username='root',password='str147852.')
        # filename = 'ceshi.sh'
        # path = '/home/mhzx/mhzx_4095/gs/'
        # remotepath = path+filename
        #
        # sftp = paramiko.SFTPClient.from_transport(trans)
        # sftp.put(localpath=localpath, remotepath=remotepath)
        # time.sleep(1)
        cmd = 'sh /home/mhzx/mhzx_4095/gs/ceshi.sh '+itemid+' '+count_item+' '+response_id

        # 将sshclient的对象的transport指定为以上的trans
        # ssh = paramiko.SSHClient()
        # ssh._transport = trans
        # 执行命令，和传统方法一样
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.read().decode())

        # 关闭连接
        trans.close()
        order.order_success = "1"
        order.save()
        return "ok"