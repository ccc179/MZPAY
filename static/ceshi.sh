#!/bin/bash


    LANG=en_US.UTF-8

    title="您有一条未读快递信息"
    content="您赞助的礼包已准时送达！感谢使用梦诛快递！如有问题请联系群主QQ：2223099004"
    itemid=210151112
    count=999

    java -cp /home/mhzx/mhzx_4095/gs/JMXTool.jar com.wanmei.mhzx.InvokeMethod 127.0.0.1 18608 controlRole kym IWEB:type=GameControl mailItemAward long -1 java.lang.String $title java.lang.String $content int $itemid int $count