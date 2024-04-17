import hashlib
m = hashlib.sha256()
m.update('1'.encode('utf-8'))
pw = m.hexdigest()
print(pw)

m.update('1'.encode('utf-8'))
pw = m.hexdigest()
print(pw)