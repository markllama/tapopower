#!/usr/bin/env python3

import argparse
import json
import requests

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email")
    parser.add_argument("-p", "--password")

    return parser.parse_args()


#Old Functions to get device list from tplinkcloud
def getToken(email, password):
    URL = "https://eu-wap.tplinkcloud.com"
    Payload = {
        "method": "login",
        "params": {
            "appType": "Tapo_Ios",
            "cloudUserName": email,
            "cloudPassword": password,
            "terminalUUID": "0C950402-7224-46EB-A450-7362CDB90FF3"
        }
    }
    
    response = requests.post(URL, json=Payload).json()
    print(response)
    
    return response['result']['token']

def getDeviceList(email, password):
	URL = "https://eu-wap.tplinkcloud.com?token=" + getToken(email, password)
	Payload = {
		"method": "getDeviceList",
	}

	return requests.post(URL, json=Payload).json()

if __name__ == "__main__":

    #print("hello")

    opts = parse_args()

    devices = getDeviceList(opts.email, opts.password)
    print(json.dumps(devices))
    
