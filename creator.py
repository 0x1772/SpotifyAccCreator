from sys import stdout
from requests import post
from os import system, _exit, path
from random import choice, randint
from colors import green, red, reset
from time import time, sleep, strftime, gmtime
from threading import Thread, Lock, active_count
from string import ascii_letters, ascii_lowercase, digits

system('cls && title [Spotify Account Creator] - Main Menu')
headers = {'User-agent': 'S4A/2.0.15 (com.spotify.s4a; build:201500080; iOS 13.4.0) Alamofire/4.9.0', 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'Accept': 'application/json, text/plain;q=0.2, */*;q=0.1', 'App-Platform': 'IOS', 'Spotify-App': 'S4A', 'Accept-Language': 'en-TZ;q=1.0', 'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5', 'Spotify-App-Version': '2.0.15'}
domains = ['gmail.com', 'protonmail.com', 'yahoo.com', 'hotmail.com', 'hotmail.co.uk', 'hotmail.fr', 'outlook.com', 'icloud.com', 'mail.com', 'live.com', 'yahoo.it', 'yahoo.ca', 'yahoo.in', 'live.se', 'orange.fr', 'msn.com', 'mail.ru', 'mac.com']
lock = Lock()

class Main:
    def __init__(self):
        self.variables = {
            'proxies': [],
            'proxy_num': 0,
            'created': 0,
            'retries': 0,
            'cpm': 0,
            'unlimited': False
        }
