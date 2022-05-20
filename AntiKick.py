import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction
from time import sleep


extension_info = {
    "title": "Anti Kick",
    "description": ":ak on/off",
    "version": "0.1",
    "author": "funkydemir66"
}

ext = Extension(extension_info, sys.argv, silent=True)
ext.start()

KATMER = "Chat"

MESSAGE = ":mt mute "


sc = True

sec_kod = True

sec_kod2 = True

def konusma(msj):
    global sc, sec_kod, sec_player, kod2, player_id, mobi_id, kod, sec_kod2


    text = msj.packet.read_string()

    if text == ':ak on':
        msj.is_blocked = True
        sec_kod = True
        sec_kod2 = True
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Click on the person you want to moderate, enter the "ambassador" section and press "unmute" from there"}{i:0}{i:30}{i:0}{i:0}')

    if text == ':ak off':
        msj.is_blocked = True
        sec_kod = False
        sec_kod2 = False
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Click on the person you want to moderate, enter the "ambassador" section and press "unmute" from there"}{i:0}{i:30}{i:0}{i:0}')


def yukle_kod(p):
    global kod, sec_kod, user_id2

    if sec_kod:
        p.is_blocked = True
        ext.send_to_server('{out:GetGuestRoom}{i:'+str(kod2)+'}{i:0}{i:1}')

def lol(d):
    global kod2, sec_kod2

    if sec_kod2:
        user_id2, _, _ = d.packet.read("iii")
        kod2 = str(user_id2)
        if sc:
              ext.send_to_client('{in:Chat}{i:123456789}{s:"Room: Saved v/ '+str(user_id2)+'"}{i:0}{i:30}{i:0}{i:0}')
              sleep(0.2)


ext.intercept(Direction.TO_CLIENT, yukle_kod, 'GenericError')
ext.intercept(Direction.TO_SERVER, konusma, 'Chat')
ext.intercept(Direction.TO_SERVER, lol, 'GetGuestRoom')




