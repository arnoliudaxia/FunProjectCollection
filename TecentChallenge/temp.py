from Crypto.Cipher import AES
import base64
import time
import gzip
from hashlib import md5
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)

print('计算第8关密钥中,时间可能非常长...')
stack = []
ins_len = [1] * 5 + [2] * 9 + [9, 1]
reg = [0] * 16
code = base64.b64decode('zyLpMs8CL9Oy/3QDdRlURZRGFHQHdRhURZFGIL/lv+MiNi+70AXRBtMD1wfYCNkJ5v3/iV14RWMB0n+/xgk=')
while True:
    ins, r0 = code[reg[15]] >> 4, code[reg[15]] & 15
    length = ins_len[ins]
    if length > 1:
        arg = code[reg[15] + 1: reg[15] + length]
        if length == 2: r1 = arg[0] >> 4; r2 = arg[0] & 15
    reg[15] += length
    if 0 == ins:
        break
    elif 1 == ins:
        stack.append(reg[r0])
    elif 2 == ins:
        reg[r0] = stack.pop()
    elif 3 == ins:
        if not reg[r0]: reg[15] += ins_len[code[reg[15]] >> 4]
    elif 4 == ins:
        reg[r0] = 0 if reg[r0] else 1
    elif 5 == ins:
        reg[r0] = reg[r1] + reg[r2]
    elif 6 == ins:
        reg[r0] = reg[r1] - reg[r2]
    elif 7 == ins:
        reg[r0] = reg[r1] * reg[r2]
    elif 8 == ins:
        reg[r0] = reg[r1] / reg[r2]
    elif 9 == ins:
        reg[r0] = reg[r1] % reg[r2]
    elif 10 == ins:
        reg[r0] = 1 if reg[r1] < reg[r2] else 0
    elif 11 == ins:
        stack.append(reg[r0]); reg[r0] += int.from_bytes(arg, byteorder='little', signed=True)
    elif 12 == ins:
        reg[r0] += int.from_bytes(arg, byteorder='little', signed=True)
    elif ins in (13, 14):
        reg[r0] = int.from_bytes(arg, byteorder='little', signed=True)
    print(reg[15])
key = str(reg[0]) + str(reg[1])

