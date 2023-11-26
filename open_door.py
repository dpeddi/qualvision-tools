#!/usr/bin/env python3

import argparse
import requests
import json

import xmltodict
import json
import hashlib

parser = argparse.ArgumentParser(
                    prog='door_open')

parser.add_argument('ip')
parser.add_argument('-p', '--password', required=True)

args = parser.parse_args()

username = "adminapp2"

TARGETS = [ args.ip ]

from enum import Enum
class CgiError(Enum):
    CGI_NOT_SUPPORT = 1
    CGI_OK = 0
    CGI_FAIL = -1
    CGI_ERROR_BLOCKEDLIST = -2
    CGI_ERROR_USERNAME = -3
    CGI_ERROR_PASSWORD = -4
    CGI_USERNAME_LOGINED = -5
    CGI_ERROR_OVER_USERNUMMAX = -6
    CGI_ERROR_IP_BLOCKING = -7
    CGI_ERROR_ACCOUNT_INACTIVE = -8
    CGI_ERROR__SUBSETOVERLAP = -10
    CGI_ERROR_PORTCONFLICT = -12
    CGI_ERROR_NOAUTH = -45
    CGI_ERROR_NOSPARINGTIME = -46

m = hashlib.sha256()
m.update(args.password.encode('utf-8'))
passwordencode = m.hexdigest()

def send_command(command, payload):

    headers = {
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept': '*/*',
      'Accept-Encoding': 'gzip, deflate',
      'Referer': f'http://{t}/index.html',
      'Connection': 'Close',
      'Host': f'{t}',
      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
      'Content-Type': 'application/xml;charset=UTF-8',
#      'Content-Length': '220',
      'Origin': f'http://{t}',
      'DNT': '1',
      'Cookie': '_goaheadwebSessionId=1653323156817220_389847650_644209849'
    }
    try:
      print ("command:",command)
      #print ("posting", payload)
      response = session.post(url, data=payload, headers=headers, allow_redirects=True, verify=False)
      print ("STATUS_CODE:",response.status_code)
#      print (response.text)

      doc = xmltodict.parse(response.text, process_namespaces=True)

      print ("Response Error:",doc["envelope"]["body"]["error"])
      print ("Response Content:",doc["envelope"]["body"]["content"])
      print ("Response Friendly Error:",CgiError(int(doc["envelope"]["body"]["error"])).name)
      print ()
      return doc

    except Exception as e:
      print ("Exception",e)


if __name__ == "__main__":
  session = requests.session()

  for t in TARGETS:
    url = f'http://{t}/tdkcgi'
    command = "get.product.info"
    payload = "<?xml version='1.0' encoding='utf-8'?>\n<envelope><header><security>username</security><username>%s</username><password>%s</password></header><body><command>%s</command><content></content></body></envelope>" % (username, passwordencode, command)
    print ("SOFTWARE VERSION:",send_command(command, payload)["envelope"]["body"]["content"]["info"]["version"])

    command = "get.product.time"
    payload = "<?xml version='1.0' encoding='utf-8'?>\n<envelope><header><security>username</security><username>%s</username><password>%s</password></header><body><command>%s</command><content></content></body></envelope>" % (username, passwordencode, command)
    print ("TIMEZONE:",send_command(command, payload)["envelope"]["body"]["content"]["time"]["timezone"])


#    command = "get.system.login" ko
    command = "get.device.status"

    payload = "<?xml version='1.0' encoding='utf-8'?>\n<envelope><header><security>username</security><username>%s</username><password>%s</password></header><body><command>%s</command><content></content></body></envelope>" % (username, passwordencode, command)
    send_command(command, payload)


#    command = "get.device.streamkey" ko
#    command = "get.device.streamkey" ko
#    command = "get.network.config"
#    command = "get.network.base"
#    command = "get.system.upgradestatus"
#    command = "get.product.time"
#    command = "get.videoswitch.vionoff" #ko
#    command = "get.wifi.list" # ko
#    payload = "<?xml version='1.0' encoding='utf-8'?>\n<envelope><header><security>username</security><username>%s</username><password>%s</password></header><body><command>%s</command><content></content></body></envelope>" % (username, passwordencode, command)

#    command = "set.opendoor.checkpassword"
#    payload = "<?xml version='1.0' encoding='utf-8'?>\n<envelope><header><security>username</security><username>%s</username><password>%s</password></header><body><command>%s</command><content><password>%s</password></content></body></envelope>" % (username, passwordencode, command, passwordencode)
#    send_command(command, payload)

    #1/2 camera 1/camera2
    #1/2 lock/gate
    command = "set.device.opendoor"
    payload = "<?xml version='1.0' encoding='utf-8'?>\n<envelope><header><security>username</security><username>%s</username><password>%s</password></header><body><command>%s</command><content><door>%d</door><locknumber>%d</locknumber><password>%s</password></content></body></envelope>" % (username, passwordencode, command, 1, 1, passwordencode)
    send_command(command, payload)
