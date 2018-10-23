import re
from wxpy import *

bot = Bot()

my_friend = bot.friends().search('邓伟')[0]

adve_group = bot.groups().search('测试群聊')[0]

#注册监听的群组
@bot.register(adve_group, NOTE)
def forward_to_me(msg):
    m = re.search('加入',msg.text)
    #截取邀请后面的第一个引号后的第二个内容
    #noti = msg.text.split('邀请')[1].split()[0].split('"')[1]
    #直接截取第三个引号后的字符串
    noti = msg.text.split('"')[3]
    if m is not None:
        print(msg)
        #return msg.forward(my_friend, prefix='新人加入：')
        msg.reply(u'''@{},宝宝你好,欢迎加入群!
品牌工厂店直销，超级特卖，长按下图识别二维码，进入相册随意挑选哈。看中的请私信截图给@A萌萌 品牌工厂店直销
        '''.format(noti))
        msg.reply_image('xcx.png')
        #msg.forward(my_friend)
        #return adve_group.send('@img@xcx.png'),'欢迎: @{} '.format(noti)
        #return '欢迎: @{} '.format(noti)
    else:
        print("失败了")





bot.join()
