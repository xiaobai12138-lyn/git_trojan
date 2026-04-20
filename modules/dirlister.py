import os

def run():
    print "[*] In dirlister module."
    # 列出当前目录文件
    return str(os.listdir('.'))
