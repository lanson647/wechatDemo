import re
from wxpy import *

bot = Bot(console_qr=True, cache_path=True)

#my_friend = bot.friends().search('lanson')[0]

adve_group = bot.groups().search('测试群聊')[0]

@bot.register(adve_group, NOTE)
def notice(msg):
        
        # 测试群聊 : "lanson"邀请"posidon"加入了群聊 (Note)
        try:
            noti = msg.text.split('邀请')[1].split()[0].split('"')[1]
            #print(type(msg.text))
            #return boring_group.send_image('xcx.png', media_id=None)
            return adve_group.send('@img@xcx.png')
        #return '欢迎: @{} '.format(noti)

        except Exception as e:
            print(e)


embed()