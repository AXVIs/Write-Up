from Crypto.Util.number import *
e = 1
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083
print(f"Flag: {long_to_bytes(pow(c,e,n)).decode()}")