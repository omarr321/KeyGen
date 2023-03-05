#!/usr/bin/env python3
import os

class KeyLookUp:
    
    def __init__(self):
        pass

    def saveKey(self, key):
        currWorkDir = os.path.dirname(__file__)
        f = open(os.path.join(currWorkDir, "keys.txt"), "a+")
        f.write(str(key) + "\n")
        f.close()

    def checkSavedKey(self, key):
        exists = False
        currWorkDir = os.path.dirname(__file__)
        f = open(os.path.join(currWorkDir, "keys.txt"), "r+")
        for x in  f.readlines():
            if (x == key):
                exists = True
        return exists

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")