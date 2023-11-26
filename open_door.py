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

COMMAND_GET_ALARM_CRYDETECTION = "get.alarm.crydetection"
COMMAND_GET_ALARM_HUMANDETECTION = "get.alarm. humandetection"
COMMAND_GET_ALARM_INPUT = "get.alarm.alarmin"
COMMAND_GET_ALARM_MOTION_DETECTION = "get.alarm.motiondetection"
COMMAND_GET_ALARM_VIDEO_LOST = "get.alarm.videolost"
COMMAND_GET_ALARM_VIDEO_SHELTER = "get.alarm.videoshelter"
COMMAND_GET_ATTACHMENT_INFO = "get.device.attachInfo"
COMMAND_GET_DEVICE_ALARM_ALARMIN_SCHEDULE = "get.alarm.alarmin.schedule"
COMMAND_GET_DEVICE_ALARM_CHANNELLIST = "get.encode.channelname"
COMMAND_GET_DEVICE_ALARM_MOTIONDETECTION_SCHEDULE = "get.alarm.motiondetection.schedule"
COMMAND_GET_DEVICE_ALARM_VIDEOLOST_SCHEDULE = "get.alarm.videolost.schedule"
COMMAND_GET_DEVICE_ALARM_VIDEOSHELTER_SCHEDULE = "get.alarm.videoshelter.schedule"
COMMAND_GET_DEVICE_ALL_INFO = "get.device.status" # ok
COMMAND_GET_DEVICE_INFO = "get.product.info" # ok
COMMAND_GET_DEVICE_LATEST_VERSION = "get.system.upgradeversion" # ok
COMMAND_GET_DEVICE_SECRET = "get.device.streamkey"
COMMAND_GET_DEVICE_UPGRADE_PROCESS = "get.system.upgradeprocess" # ok
COMMAND_GET_DEVICE_UPGRADE_STATUS = "get.system.upgradestatus" # ok
COMMAND_GET_FPS = "get.encode.fps"
COMMAND_GET_HUMANTRACE_INFO = "get.humantrace.info"
COMMAND_GET_MOTION_DETECTION = "get.motiondetection.info"
COMMAND_GET_MOVEDETECTION_INFO = "get.movedetection.info"
COMMAND_GET_NETWORK_BASE = "get.network.base"
COMMAND_GET_NETWORK_CONFIG = "get.network.config"
COMMAND_GET_NETWORK_WORKMODE = "get.network.workmode"
COMMAND_GET_PAN_TILT_CONTROL_POSITION = "get.ptz.position"
COMMAND_GET_PTZ_PRESET = "get.ptz.preset"
COMMAND_GET_QR_CODE = "get.device.qrcode" # ok
COMMAND_GET_RECORD_ALARM_INFO = "get.record.alarmrecord"
COMMAND_GET_RECORD_CONFIG = "get.record.config"
COMMAND_GET_RECORD_MESSAGE = "get.record.message"
COMMAND_GET_RECORD_SESSION = "get.record.session"
COMMAND_GET_SHAPE_MIRROR = "get.shape.mirror"
COMMAND_GET_SMART_LIGHT_INFO = "get.smart.lightinfo"
COMMAND_GET_SOUNDANDLIGHT_STATE = "get.soundandlight.state"
COMMAND_GET_STORAGE_INFO = "get.hdd.base"
COMMAND_GET_SYSTEM_ABILITY = "get.system.ability"
COMMAND_GET_SYSTEM_GENERAL = "get.system.general"
COMMAND_GET_TF_CARD_INFO = "get.tfcard.info" # ok
COMMAND_GET_TIME_ZONE = "get.product.time" # ok
COMMAND_GET_VIDEO_CONFIG_BITRATELIST_INFO = "get.encode.bitratelist"
COMMAND_GET_VIDEO_CONFIG_INFO = "get.encode"
COMMAND_GET_VIDEO_SWITCH = "get.videoswitch.vionoff"
COMMAND_GET_VIDEO_TIME_TITLE = "get.video.timetitle"
COMMAND_GET_WIFI_LIST = "get.wifi.list"
COMMAND_CHECK_UNLOCK_PASSWORD = "set.opendoor.checkpassword"
COMMAND_GET_DEVICE_UNLOCK = "set.device.opendoor"
COMMAND_MODIFY_VERIFICATION_CODE = "set.seurity.verifycode"
COMMAND_OPEN_LOCK = "set.device.opendoor"
COMMAND_SET_ALARM_CRYDETECTION = "set.alarm.crydetection"
COMMAND_SET_ALARM_HUMANDETECTION = "set.alarm.humandetection"
COMMAND_SET_ALARM_INPUT = "set.alarm.alarmin"
COMMAND_SET_ALARM_MOTION_DETECTION = "set.alarm.motiondetection"
COMMAND_SET_ALARM_VIDEO_LOST = "set.alarm.videolost"
COMMAND_SET_ALARM_VIDEO_SHELTER = "set.alarm.videoshelter"
COMMAND_SET_DEBUG_SYNC_TIME = "set.debug.synctime"
COMMAND_SET_DEVICE_ALARM_ALARMIN_SCHEDULE = "set.alarm.alarmin.schedule"
COMMAND_SET_DEVICE_ALARM_CHANNELLIST = "set.encode.channelname"
COMMAND_SET_DEVICE_ALARM_MOTIONDETECTION_SCHEDULE = "set.alarm.motiondetection.schedule"
COMMAND_SET_DEVICE_ALARM_VIDEOLOST_SCHEDULE = "set.alarm.videolost.schedule"
COMMAND_SET_DEVICE_ALARM_VIDEOSHELTER_SCHEDULE = "set.alarm.videoshelter.schedule"
COMMAND_SET_DEVICE_UPGRADE = "set.system.upgrade"
COMMAND_SET_F1_STATE = "set.device.f1function.enable"
COMMAND_SET_FPS = "set.encode.fps"
COMMAND_SET_HUMANTRACE_INFO = "set.humantrace.info"
COMMAND_SET_MOTION_DETECTION = "set.motiondetection.info"
COMMAND_SET_MOVEDETECTION_INFO = "set.movedetection.info"
COMMAND_SET_NETWORK_BASE = "set.network.base"
COMMAND_SET_NETWORK_CONFIG = "set.network.config"
COMMAND_SET_NETWORK_WORKMODE = "set.network.workmode"
COMMAND_SET_PAN_TILT_CONTROL_POSITION = "set.ptz.position"
COMMAND_SET_PTZ_PRESET = "set.ptz.preset"
COMMAND_SET_PTZ_PRESET_CLEAR = "set.ptz.preset.clear"
COMMAND_SET_PTZ_PRESET_GOTO = "ctrl.ptz.preset.goto"
COMMAND_SET_RECORD_CONFIG = "set.record.config"
COMMAND_SET_SHAPE_MIRROR = "set.shape.mirror"
COMMAND_SET_SMART_LIGHT_INFO = "set.smart.lightinfo"
COMMAND_SET_SMART_LIGHT_MODE = "set.smart.lightmode"
COMMAND_SET_SOUNDANDLIGHT_STATE = "set.soundandlight.state"
COMMAND_SET_SUMMER_TIME = "set.system.summertime"
COMMAND_SET_SYSTEM_GENERAL = "set.system.general"
COMMAND_SET_TF_CARD_FORMAT = "set.tfcard.format"
COMMAND_SET_TIME_ZONE = "set.product.time"
COMMAND_SET_UNLOCK_PASSWORD = "set.opendoor.password"
COMMAND_SET_VIDEO_CONFIG_INFO = "set.encode"
COMMAND_SET_VIDEO_SWITCH = "set.videoswitch.vionoff"
COMMAND_SET_WIFI_INFO = "set.wifi.info"

m = hashlib.sha256()
m.update(args.password.encode('utf-8'))
passwordencode = m.hexdigest()

def send_command(command, payload, debug = False):

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
      if debug:
          print (response.text)

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

    payload = "<?xml version='1.0' encoding='utf-8'?>\n<envelope><header><security>username</security><username>%s</username><password>%s</password></header><body><command>%s</command><content></content></body></envelope>" % (username, passwordencode, command)
    print ("SOFTWARE VERSION:",send_command(command, payload)["envelope"]["body"]["content"]["info"]["version"])

    command = "get.product.time"
    payload = "<?xml version='1.0' encoding='utf-8'?>\n<envelope><header><security>username</security><username>%s</username><password>%s</password></header><body><command>%s</command><content></content></body></envelope>" % (username, passwordencode, command)
    print ("TIMEZONE:",send_command(command, payload)["envelope"]["body"]["content"]["time"]["timezone"])


    command = "get.device.status"
    payload = "<?xml version='1.0' encoding='utf-8'?>\n<envelope><header><security>username</security><username>%s</username><password>%s</password></header><body><command>%s</command><content></content></body></envelope>" % (username, passwordencode, command)
    send_command(command, payload)

#    command = "set.opendoor.checkpassword"
#    payload = "<?xml version='1.0' encoding='utf-8'?>\n<envelope><header><security>username</security><username>%s</username><password>%s</password></header><body><command>%s</command><content><password>%s</password></content></body></envelope>" % (username, passwordencode, command, passwordencode)
#    send_command(command, payload)

    #1/2 camera 1/camera2
    #1/2 lock/gate
    command = "set.device.opendoor"
    payload = "<?xml version='1.0' encoding='utf-8'?>\n<envelope><header><security>username</security><username>%s</username><password>%s</password></header><body><command>%s</command><content><door>%d</door><locknumber>%d</locknumber><password>%s</password></content></body></envelope>" % (username, passwordencode, command, 1, 1, passwordencode)
    send_command(command, payload)
