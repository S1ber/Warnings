                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             # -*- coding: utf-8 -*-

import requests
from datetime import datetime
from bs4 import BeautifulSoup
import os
import sys
import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from config import tok,str_token,main_str_token,ip_token,passs
import time
bots_list=open("bots.txt","r")
bots_list=bots_list.readline().split()
print(bots_list)
g=[]
def chat_sender(text):
    a=text.split("\n")
    b = ""
    if len(text) > 1200:
        for i in a:
            b += i + "\n"
            if len(b) > 1200:
                print(b)
                vk_session.method('messages.send', {'chat_id': 20, 'message': b, 'disable_mentions': 1, 'random_id': 0})
                b = ""
        vk_session.method('messages.send', {'chat_id': 20, 'message': b, 'disable_mentions': 1, 'random_id': 0})
    else:
        vk_session.method('messages.send', {'chat_id': 20, 'message': text, 'disable_mentions': 1, 'random_id': 0})

vk_session = vk_api.VkApi(token = tok)
longpoll = VkBotLongPoll(vk_session,204604686)
c=0
print("?????? ??????????????")
#while True:
#    if str(datetime.now().hour)=="23":
#        break
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Atom/13.0.0.44 Safari/537.36'}
sess=requests.session()
sess.headers.update(header)
k=0
resp=sess.post("http://ulog.union-u.net/login.php",data={"mail":"hrhhhdki@gmail.com","pass":passs,"login":"??????????"})
main_str=sess.get("http://ulog.union-u.net/index.php")
strokll=[]
bots={}
bots2={}
bots3={}
business={}
houses={}
zams_biz=[]
zams_fam=[]
fams={}
bots_ip=["46.147.164.212","109.70.151.2","185.169.233.101","45.149.175.239","92.55.191.184","193.176.30.131","185.169.233.252","89.179.65.3","80.95.44.177","93.124.89.7","91.197.1.76"]
vzloms={}



if "??????????" in main_str.text:
    print("??????????")
    year="2022"
    month="06"
    day="28"
    logs=sess.get(f"http://ulog.union-u.net/event.php?server=30&type=&day={day}&mount={month}&year={year}&go=%D0%9F%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B5%D1%82%D1%8C&hour=all&listen=0")
    while f"{year}-{month}-{day}" in logs.text:
        logs=BeautifulSoup(logs.text ,"lxml")
        stroki=logs.find_all("table")[5]
        stroki=stroki.find_all("tr")
        print(stroki[0].text.split()[1])
        for i in stroki:
            if "???? ????????????" in i.text and "???? ??????????" in i.text and ("????????????????" in i.text or "????????" in i.text or "????????????????" in i.text):

                b=i.text.replace("??????????"," ??????????")
                if b not in strokll:
                    nick=b.split()[3]
                    if nick not in bots:
                        bots[nick]=0
                    else:
                        bots[nick]+=1
                strokll.append(b)
            if "?????????????? ????????????" in i.text.lower() or "?????????????? ????.??????????" in i.text.lower():
                b=i.text.replace("??????????"," ??????????")
                if b not in strokll:
                    nick=b.split()[3]
                    if nick not in vzloms:
                        vzloms[nick]=[]
                        vzloms[nick].append(b)
                    else:
                        vzloms[nick].append(b)
                strokll.append(b)


            if "??????????????" in i.text:
                b = i.text.replace("??????????", " ??????????")
                if b not in strokll:
                    nick=b.split()[3]
                    if nick in bots_list:
                        chat_sender(f"WARNING\n???????????????? ???? ???????? ????????\n{b}")
                strokll.append(b)

            if "??????????????????????????????????" in i.text:
                b = i.text.replace("??????????", " ??????????")
                if b not in strokll:
                    nick = b.split()[3]
                    if nick not in bots2:
                        bots2[nick] = 0
                strokll.append(b)
            if "????????????" in i.text:
                b = i.text.replace("??????????????????????????", " ??????????????????????????")
                if b not in strokll:
                    nick = b.split()[7][:-1]
                    if nick not in bots3:
                        bots3[nick] = 0
                strokll.append(b)
            if "??????????" in i.text and i.text.split()[7] in bots_ip:
                b = i.text.replace("??????????", " ??????????")
                if b not in strokll:
                    nick = b.split()[3]
                    if not nick in bots2:
                        bots[nick]=250
                        bots2[nick]=0
                        #chat_sender(f"New warning bots: {i}")
                    strokll.append(b)

            if "???????????????? ??????????????????????" in i.text.lower():
                zams_biz.append(i.text.split()[5])
            if "???????????????????????? ??????????" in i.text.lower():
                zams_fam.append(i.text.split("????????????????")[1].split("????????????????????????")[0])

            if "???????? ???????????? ?? ??????????????" in i.text.lower() or "?????????????? ???????????? ?? ????????????" in i.text.lower():
                b = i.text.replace("??????????", " ??????????")
                c = b.split("idb:")[1].split("(")[0]
                if b not in strokll:
                    if c not in business:
                        business[c]=[]
                        business[c].append(b)
                    else:
                        business[c].append(b)
                strokll.append(b)
            if "???? ?????????? ??????????" in i.text.lower() or "???? ???????????? ??????????" in i.text.lower():
                b = i.text.replace("??????????", " ??????????")
                c = b.split("ID:")[1].split("(")[0]
                if b not in strokll:
                    if c not in fams:
                        fams[c]=[]
                        fams[c].append(b)
                    else:
                        fams[c].append(b)
                strokll.append(b)

            if "???????? ???????????? ???? ????????" in i.text.lower() or "?????????????? ???????????? ?? ??????" in i.text.lower():
                b = i.text.replace("??????????", " ??????????")
                c = b.split("idh:")[1].split("(")[0]
                if b not in strokll:
                    if c not in houses:
                        houses[c]=[]
                        houses[c].append(b)
                    else:
                        houses[c].append(b)
                strokll.append(b)






            if (((("?????????????? ???????????????? ??????????" in i.text or "???? ??????????." in i.text) and int(i.text.split()[5])>=50000) or (("???????? ???? ?????????????????? ????????" in i.text or "?????????????? ?? ???????????????? ????????" in i.text or "???? ??????????????" in i.text or "?????????????? ?? ??????????????" in i.text.lower() or "?????????????? ?? ??????????" in i.text or "???????? ???? ????????????" in i.text.lower() or "???????? ???? ?????????????????? ??????????" in i.text.lower() or "?????????????? ?? ???????????????? ????????" in i.text.lower()) and ("??????????" in i.text.lower() or "????????????????????" in i.text.lower() or "??????????????" in i.text.lower() or "??????????????????" in i.text.lower() or "????????????????????" in i.text.lower() or "????????????????????" in i.text.lower() or "??????????????" in i.text.lower() or "????????????".lower() in i.text.lower() or "?????????????????? ???? ??????????" in i.text.lower() or ("????????????" in i.text.lower() and "????????????????????" not in i.text.lower()) or "??????????????????" in i.text.lower())) and not "??????????????????????" in i.text.lower())):
                b=i.text.replace("??????????"," ??????????")
                if b not in strokll:
                    chat_sender(b)
                strokll.append(b)
        logs = sess.get(f"http://ulog.union-u.net/event.php?server=30&type=&day={day}&mount={month}&year={year}&go=%D0%9F%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B5%D1%82%D1%8C&hour=all&listen={k}")
        k+=1
        #time.sleep(1)
        print(f"???????????????????? ???????????????? ?????????? {k}")
    print('???????????????? ??????????????????')
    bans=""""""
    for i in bots:
        if bots[i]>=200 and i in bots2 and i not in bots3:
            bans+=f"/banoff 0 {i} 2000 ?????? ???????? // ??????\n"
            bots_list.append(i)

    aaaa = open("bots.txt", "w")
    aaaa.write(" ".join(bots_list))
    aaaa.close()
    print(business)
    print(houses)
    print(bots_list)
    for i in business:
        try:
            nick=business[i][0].split()[3]
            print(nick)
            for i1 in business[i]:
                if i1.split()[3] in zams_biz:
                    chat_sender(f"!!!?????????????????? ?????????????? ?????????? ????????????!!! {nick}\n"+"\n".join(business[i]))
                    break
        except:
            pass
    for i in fams:
        try:
            nick = fams[i][0].split()[3]
            print(nick)
            for i1 in fams[i]:
                if i1.split()[3] in zams_fam:
                    chat_sender(f"!!!?????????????????? ?????????????? ?????????? ????????!!! {nick}\n" + "\n".join(business[i]))
                    break
        except:
            pass
    for i in houses:
        try:
            nick=houses[i][0].split()[3]
            print(nick)
            for i1 in houses[i]:
                if i1.split()[3]!=nick:
                    chat_sender("!!!?????????????????? ?????????????? ?????????? ??????!!!\n"+"\n".join(houses[i]))
                    break
        except:
            pass
    for i in vzloms:
        if len(vzloms[i])==2:
            bans+=f"/banoff 0 {i} 2000 ???? ??????????????????(??????????????) // ??????\n"
    chat_sender(bans)
    print(fams)
    print(zams_fam)
    print(business)
    print(zams_biz)
    #bann=""

    #for i in g:
        #bann+=f"/banoff 0 {i} 2000 ????????????\n"
    #chat_sender(bann)
    os.execl(sys.executable, sys.executable, *sys.argv)