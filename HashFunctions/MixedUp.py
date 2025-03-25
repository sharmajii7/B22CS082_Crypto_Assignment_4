from Crypto.Util.number import long_to_bytes
import telnetlib
import json
from sage.all import *
from hashlib import sha256

def check(val, flag_len):
    for i in range(256):
        if (val) == (sha256(bytes([i]*flag_len)).hexdigest()):
            return True
    return False
        

HOST = "socket.cryptohack.org"
PORT = 13402

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline().decode()
    st = line[line.find('{'):]
    return json.loads(st)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

tn = telnetlib.Telnet(HOST, PORT)
print(readline())
flag_length = 0
for i in range(1,50):
    data = [0]*i
    to_send = json.loads(json.dumps({"option" : "mix", "data" : bytes(data).hex()}))
    json_send(to_send)

    val = json_recv()["mixed"]
    if check(val, i):
        flag_length = i
        print("gg flag_length ==", i)

data = [0]*flag_length
flag = 0
for i in range(8*flag_length):
    data[flag_length - (i//8) - 1] = 1<<(i%8)
    to_send = json.loads(json.dumps({"option" : "mix", "data" : bytes(data).hex()}))
    json_send(to_send)

    val = json_recv()["mixed"]
    if not check(val, flag_length):
        flag += (1<<i)
    data[flag_length - (i//8) - 1] = 0
print(long_to_bytes(flag))