import hashlib
in_var = "bgvyzdsv"
zeros = 5
i = 0

while hashlib.md5((in_var+str(i)).encode()).hexdigest()[0:zeros] != "0"*zeros:
    i += 1
print("MD5 hash: " + hashlib.md5((in_var+str(i)).encode()).hexdigest())
print("Answer: " + i)
