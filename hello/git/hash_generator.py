import hashlib 
with open("hello/git/firmware.bin","rb") as file:
    data = file.read()
hash_value=hashlib.sha256(data).hexdigest()
print(hash_value)