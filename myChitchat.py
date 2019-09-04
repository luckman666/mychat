import random
from time import sleep
import requests


def GenerateWord():

    s=''
    for num in range(5):
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xf9)  
        val = f'{head:x}{body:x}'
        s += bytes.fromhex(val).decode('gb2312')
    return s

def Checkrepetition(chat,chatList):

    if len(chatList) > 5:
        chatList.pop(0)
    if chat in chatList:
        myword = GenerateWord()

        return myword,chatList
    else:
        chatList.append(chat)
        return chat,chatList


def Chitchat():
    zs = input("请主人输入话题：")
    chatList=[]

    while True:

        resp = requests.get("http://api.qingyunke.com/api.php", {'key': 'free', 'appid':0, 'msg': zs})
        resp.encoding = 'utf8'
        resp = resp.json()
        sleep(1)
        print('赵四：', resp['content'])

        ln,chatList=Checkrepetition(resp['content'],chatList)
        resp = requests.get("http://api.qingyunke.com/api.php", {'key': 'free', 'appid':0, 'msg': ln})
        resp.encoding = 'utf8'
        resp = resp.json()
        sleep(1)
        print('刘能：', resp['content'])
        zs,chatList=Checkrepetition(resp['content'], chatList)


if __name__ == "__main__":
    Chitchat()