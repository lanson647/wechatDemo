from wxpy import *

bot = Bot(cache_path=True)

# 获取群组
adve_group = bot.groups().search('动车组')[0]

#  注册获得个人的图灵机器人key 填入
tuling = Tuling(api_key='7960dcf949674d369098d9760ef0cf46')


# 使用图灵机器人自动与指定好友聊天
@bot.register(adve_group)
def reply_my_friend(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        tuling.do_reply(msg)


embed()