import os

file = input("File of URLS: ")
f = open(file)
t = f.read()
f.close()

urls = t.split("\n")

for url in urls:
    os.system("git clone " + url)
