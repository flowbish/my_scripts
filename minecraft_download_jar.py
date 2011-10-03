#!/usr/bin/env python

import urllib2,os,sys

username='SuckyBlowfish'
password='jQ35uvJ4eE'
version='13'

minecraft_download_base_url='http://s3.amazonaws.com/MinecraftDownload/'
minecraft_jar_url='minecraft.jar?user={user}&ticket={ticket}'

# Acquire session info from minecraft.net

minecraft_info=urllib2.urlopen('https://login.minecraft.net',
                               'user='+username+
                               '&password='+password+
                               '&version='+version).read()
session_id=minecraft_info.split(':')[3]
download_ticket=minecraft_info.split(':')[1]
username=minecraft_info.split(':')[2]
jar_version=minecraft_info.split(':')[0]

print 'Downloading '+username+"'s minecraft.jar with ticket #"+download_ticket

minecraft_jar=urllib2.urlopen(minecraft_download_base_url+minecraft_jar_url.format(user=username,ticket=download_ticket))
with open('minecraft.jar','w') as f:
    f.write(minecraft_jar.read());
