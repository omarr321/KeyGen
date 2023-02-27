#!/usr/bin/env python3

import sys
import os

import KeyGen


class Key:
    def start(self):
        keyCurr = KeyGen.KeyGen()
        keyCurr.genNewKey()
        print(keyCurr.getKey())


if __name__ == "__main__":
    program = Key()
    program.start()