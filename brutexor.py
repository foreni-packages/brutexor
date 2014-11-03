#!/usr/bin/python
##
# Nicolas THIBAUT
# http://www.dev2lead.com
##

import sys

LEN=int(1024)

class XORFORCE:
    def __init__(self, file, model):
        self.file = open(file, "r+")
        self.model = open(model, "r+")
    def __del__(self):
        self.file.close()
        self.model.close()
    def execute(self):
        global LEN

        buffer = self.file.read()
        list = self.model.read()
        stack = []
        for index in range(0, LEN):
            for key in range(0, 256):
                if chr(ord(buffer[index]) ^ key) == list[index]:
                    stack.append(key)
        for index in range(0, len(buffer)):
            self.file.seek(index)
            self.file.write(chr(ord(buffer[index]) ^ stack[index % len(stack)]))
        return 0

def main():
    global LEN

    if "--len" in sys.argv:
        LEN = int(sys.argv[sys.argv.index("--len") + 1])
    if "--file" and "--model" in sys.argv:
        XORFORCE(sys.argv[sys.argv.index("--file") + 1], sys.argv[sys.argv.index("--model") + 1]).execute()
    return 0

if __name__ == "__main__":
    main()
