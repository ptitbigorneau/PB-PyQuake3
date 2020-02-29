# -*-coding:Utf-8 -*

# PBUrTRcon (PYTHON 3)
# Copyright (C) 2020 PtitBigorneau
#
# PtitBigorneau - www.ptitbigorneau.fr
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
__author__  = 'PtitBigorneau'
#########################################################################################################
import sys
import os
import time
import configparser

from pyquake3 import PyQuake3

if sys.version_info < (3,):
    raise SystemExit("Sorry, requires Python 3, not Python 2.")
#########################################################################################################
# Config
#########################################################################################################
config = configparser.ConfigParser()
config.read("pburtrcon_config.ini")
address = config.get('server', 'address')
port = config.get('server', 'port')
rcon_password = config.get('server', 'rcon_password')

address = address +':' + port

#########################################################################################################
# Clean Color Name
#########################################################################################################
def cleancolorname(data):

    data = data.replace('^1','')
    data = data.replace('^2','')
    data = data.replace('^3','')
    data = data.replace('^4','')
    data = data.replace('^5','')
    data = data.replace('^6','')
    data = data.replace('^7','')
    data = data.replace('^8','')
    data = data.replace('^9','')
    data = data.replace('^0','')

    return data
#########################################################################################################
# GameType
#########################################################################################################
def gametype(data):
    if data == 0:
        gametype = ["FFA", "Free For All"]
    elif data == 1:
        gametype = ["LMS", "Last Man Standing"]
    elif data == 2:
        gametype = ["FFA", "Free For All"]
    elif data == 3:
        gametype = ["TDM", "Team DeathMatch"]
    elif data == 4:
        gametype = ["TS", "Team Survivor"]
    elif data == 5:
        gametype = ["FTL", "Follow The Leader"]
    elif data == 6:
        gametype = ["CandH", "Capture And Hold"]
    elif data == 7:
        gametype = ["CTF", "Capture The Flags"]
    elif data == 8:
        gametype = ["Bomb", "Bomb Mode"]
    elif data == 9:
        gametype = ["Jump", "Jump Mode"]
    elif data == 10:
        gametype = ["Freeze", "Freeze Tag"]
    elif data == 11:
        gametype = ["GunGame", "GunGame"]
    else:
        gametype = ["Unkown", "Unkown"]
    return gametype
#########################################################################################################
# Status
#########################################################################################################
def status(q):
    q.update()
    q.rcon_update()
    nbots = 0
    for player in q.players:
        if player.address == "bot":
            nbots = nbots + 1
 
    tbots = ""
    if nbots > 0:
        tbots = " + %s bot"%nbots
        if nbots > 1:
            tbots = " + %s bots"%nbots

    tprivateslots =""
    if int(q.values['sv_privateClients']) > 0:
        tprivateslots = "(%s) (*Private Clients)"%q.values['sv_privateClients']

    print("UrbanTerror: %s - (%s)"%(q.values['g_modversion'], q.values['version']))    
    print("Server: %s - Address: %s" % (cleancolorname(q.values['sv_hostname']), q.get_address()))
    print("--------------------------------------------------------------------------------------")
    print("Gametype: %s - Players: %s%s - Slots: %s%s" % (gametype(int(q.values['g_gametype']))[1], len(q.players) - nbots, tbots, q.values['sv_maxclients'], tprivateslots))
    reponse = q.rcon("status")
    for data in reponse:
        if data != "t":
            print(cleancolorname(data))
#########################################################################################################
# Main
#########################################################################################################
def main():
    q = PyQuake3(server=address, rcon_password = rcon_password)
    cmd = None
    status(q)
    print("Command RCON (\"quit\" or \"q\" for exit.)")
    cmd = input('?: ')
    cmd = cmd.lower()
    if cmd == "q" or cmd == "quit":
        sys.exit()
    if cmd == "status":
        main()
    reponse = q.rcon(cmd)
    for data in reponse:
        if data != "t":
            print(cleancolorname(data))
    time.sleep(2)
    main()
#########################################################################################################
if __name__ == '__main__':
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print("--------------------------------------------------------------------------------------")
    main()
