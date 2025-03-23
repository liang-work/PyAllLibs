import hashlib

def md5_text(t:str):
    h = hashlib.md5()
    h.update(t.encode("utf-8"))
    return h.hexdigest()

def sha256_text(t:str):
    h = hashlib.sha256()
    h.update(t.encode("utf-8"))
    return h.hexdigest()

def md5_file(path):
    with open(path, 'rb') as file:
        t = file.read()
    h = hashlib.md5()
    h.update(t.encode("utf-8"))
    return h.hexdigest()

def sha256_file(path):
    with open(path, 'rb') as file:
        t = file.read()
    h = hashlib.sha256()
    h.update(t.encode("utf-8"))
    return h.hexdigest()

def check_file(file_path,hash_md5,hash_sha256):
    return md5_file(path=file_path) == hash_md5 and sha256_file(path=file_path) == hash_sha256