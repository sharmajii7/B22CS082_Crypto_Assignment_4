from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util import number
import gmpy2

grps = {'n':[],'c':[],'e':[]}
for i in range(1, 51):
    key = RSA.importKey(open(f"keys_and_messages/{i}.pem", 'r').read())
    cipher = open(f"keys_and_messages/{i}.ciphertext", 'r').read()
    cipher = number.bytes_to_long(bytes.fromhex(cipher))
    grps['n'].append(key.n)
    grps['c'].append(cipher)
    grps['e'].append(key.e)

N = 0
for i in range(len(grps['n'])):
    for j in range(i+1, len(grps['n'])):
        if i == j: continue
        gcd = gmpy2.gcd(grps['n'][i], grps['n'][j])
        if gcd != 1:
            print(i, j, gcd)
            N = int(gcd)
            ind = i

e = grps['e'][ind]
p = N
q = grps['n'][ind]//N
phi = (p-1)*(q-1)
d = number.inverse(e, phi)

key = RSA.construct((grps['n'][ind], e, d))
cipher = PKCS1_OAEP.new(key)
flag = number.long_to_bytes(grps['c'][ind])
flag = cipher.decrypt(flag)
print(flag)