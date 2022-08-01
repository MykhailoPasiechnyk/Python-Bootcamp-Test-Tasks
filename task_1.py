import hashlib

s = "Python Bootcamp"


def hash_string(value):
    b_string = bytearray(value, 'utf-8')
    return hashlib.sha256(b_string).hexdigest()


print(hash_string(s))
