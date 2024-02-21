import os

for file in os.listdir():
    if (file.endswith(".csv")):
        content = open(file, "r").read()
        print(type(content))
        if content[0] != 'Serial,':
            content = "Serial," + content
        open(file, "w").write(content)
