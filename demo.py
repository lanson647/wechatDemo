import re
from wxpy import *

bot = Bot(console_qr=True,cache_path=True)
#bot = Bot(console_qr=True)

my_friend = bot.friends().search('lanson')[0]

adve_group = bot.groups().search('测试群聊')[0]

# @bot.register(adve_group, NOTE)
# def notice(msg):
        
#         # 测试群聊 : "lanson"邀请"posidon"加入了群聊 (Note)
#         try:
#             noti = msg.text.split('邀请')[1].split()[0].split('"')[1]
#             #print(type(msg.text))
#             #return boring_group.send_image('xcx.png', media_id=None)
#             return adve_group.send('@img@xcx.png')
#         #return '欢迎: @{} '.format(noti)

#         except Exception as e:
#             print(e)

# @bot.register(my_friend, TEXT)
# def reply_m(msg):
#     # my_friend.send_raw_msg(
#     #     # 名片的原始消息类型
#     #     raw_type=42,
#     #     # 注意 `username` 在这里应为微信 ID，且被发送的名片必须为自己的好友
#     #     raw_content='<msg username="wxpy_bot" nickname="lanson"/>'
#     # )
#     print(msg)

# @bot.register()
# def just_print(msg):
#     # 打印消息
#     #print(msg)
#     my_friend.send_raw_msg(
#         # 名片的原始消息类型
#         raw_type=49,
#         # 注意 `username` 在这里应为微信 ID，且被发送的名片必须为自己的好友
#         raw_content='''
#         <msg><appmsg appid=""
#     sdkver = "0" > < title > 欢迎关注我的云相册 < /title><des>代购云相册</des > < action > < /action><type>33</type > < showtype > 0 < /showtype><soundtype>0</soundtype > < mediatagname > < /mediatagname><messageext></messageext > < messageaction > < /messageaction><content></content > < contentattr > 0 < /contentattr><url>https:/ / mp.weixin.qq.com / mp / waerrpage ? appid = wxb40fc5967ade5b3a & amp;type = upgrade & amp;upgradetype = 3# wechat_redirect < /url><lowurl></lowurl > < dataurl > < /dataurl><lowdataurl></lowdataurl > < appattach > < totallen > 0 < /totallen><attachid></attachid > < emoticonmd5 > < /emoticonmd5><fileext></fileext > < cdnthumburl > 30580201000451304 f02010002040960778302032f559702044cd11d7002045bcc3152042a777875706c6f61645f777869645f716d746138306535356a666a32323332325f313534303130383632360204010400030201000400 < /cdnthumburl><cdnthumbmd5>b89d7d72cc9df874a3cf6cce6a627b04</cdnthumbmd
#     5 > < cdnthumblength > 787680 < /cdnthumblength><cdnthumbwidth>1242</cdnthumbwidth > < cdnthumbheight > 2016 < /cdnthumbheight><cdnthumbaeskey>3724715693724fc18447eafe23197fd6</cdnthumbaeskey > < aeskey > 3724715693724 fc18447eafe23197fd6 < /aeskey><encryver>0</encryver > < filekey > wxid_qmta80e55jfj22322_1540108626 < /filekey></appattach > < extinfo > < /extinfo><sourceusername></sourceusername > < sourcedisplayname > 代购云相册 < /sourcedisplayname><thumburl></thumburl > < md5 > < /md5><statextstr></statextstr > < weappinfo > < username > < /username><appid><![CDATA[wxb40fc5967ade5b3a]]></appid > < type > 2 < /type><version>23</version > < weappiconurl > < ![CDATA[http: //mmbiz.qpic.cn/mmbiz_png/7l4AicXQo1vnIU7STFUxrmwgPGEHZJwWCrdzazyibBj74vrOWVXKR6bTBFGVhhbWCItL67sRBmcesacFqbY3OuvQ/640?wx_fmt=png&wxfrom=200]]></weappiconurl><pagepath><![CDATA[package/pages/share/index.html?unionid=oXZ2O0o-zR8FAqdDzOcB7Q0Bp7Ys]]></pagepath><shareId><![CDATA[0_wxb40fc5967ade5b3a_3458909843_1540007232_0]]></shareId><appservicetype>0</appservicetype></weappinfo></appmsg><fromusername></fromusername><scene>0</scene><appinfo><version>1</version><appname></appname></appinfo><commenturl></commenturl></msg>
#         '''
#     )
#     return 'test'

@bot.register()
def reply_my_friend(msg):
    print(msg)
    return adve_group.send('@img@xcx.png')
    return 'received: {} ({})'.format(msg.text, msg.type)


embed()