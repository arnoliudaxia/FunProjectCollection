from Crypto.Cipher import AES
import base64
import time
import gzip
from hashlib import md5
import sys
import io

id=7
priv_key='TfpPfagH/?fa*gl01'
prefix = str(id) + str(int(time.time()))
pub_key = prefix + md5(bytes(prefix + priv_key, 'utf8')).hexdigest()
print('恭喜通过第%d关,通关公钥:%s' % (id, pub_key))