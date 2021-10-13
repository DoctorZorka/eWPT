#!/usr/bin/python3

import requests


fd = open("xss-payloads.txt", "r")
url = "http://3.challenge.xss.site/search.php"



while True:
    #read each line from xss-payloads.txt
    payload = fd.readline()
    #check EOF
    if payload == "":
        break
    
    response = requests.get(url,params={'term': payload})
    #check if XSS is found on webpage
    if resp.text.find(payload) != -1:
        print("Possible XSS : " + payload)
