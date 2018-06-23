# coding:utf8
import itchat

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    print(msg.text)
    if msg.text == "uplooking":
        msg.user.send("hello world")

itchat.auto_login(hotReload=True)
itchat.run()