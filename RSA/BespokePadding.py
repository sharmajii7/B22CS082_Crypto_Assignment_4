from Crypto.Util.number import bytes_to_long, long_to_bytes
import telnetlib
import json
from sage.all import *
    
def binomial_coef(pad, p, e):
    coef = []
    R = Integers(p)
    
    a = R(pad[0])
    b = R(pad[1])
    
    for i in range(e+1):
        c = binomial(e,i)
        c = R(c)
        c = c*(a**i)*(b**(e-i))
        coef.append(c)
        
    return coef
    
HOST = "socket.cryptohack.org"
PORT = 13386

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

result = []
coef = []

readline()

for i in range(12):
    stri = '''{"option" : "get_flag"}'''
    json_send(json.loads(stri))
    
    temp = json_recv()
    
    flag = temp["encrypted_flag"]
    p = temp["modulus"]
    pad = temp["padding"]
    
    coef.append(binomial_coef(pad,p,11))
    result.append(flag)
    
m_result = matrix(Integers(p), 12, 1, result)
m_coef = matrix(Integers(p), 12, 12, coef)

m_message = (~m_coef)*m_result
R = Integers(p)

x = 754659823705280937426684693543545157731789888997963325308215810880829655843345426301
print(long_to_bytes(x))