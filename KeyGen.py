#!/usr/bin/env python3
import random
import KeyLookUp

class KeyGen:
    __currKey = None
    __keyLookUp = KeyLookUp.KeyLookUp()

    def __init__(self):
        pass

    def genNewKey(self):
        while (True):
            totalAdd = 0
            secondBit = "1000"
            while (True):
                secondBit = str(random.randint(1000, 9999))
                currAdd = 0
                currMuti = 1
                flag = True
                for x in map(int, secondBit):
                    currAdd = currAdd + x
                    currMuti = currMuti * x
                    if (x == 0):
                        flag = False
                if (flag):
                    if (currAdd % 2) == 0:
                        if (currMuti % 5) == 0:
                            totalAdd = totalAdd + currAdd
                            break

            thirdBit = "100000"

            while (True):
                thirdBit = str(random.randint(100000, 999999))
                currAdd = 0
                currMuti = 1
                flag = True
                for x in map(int, thirdBit):
                    currAdd = currAdd + x
                    currMuti = currMuti * x
                    if (x == 0):
                        flag = False
                if (flag):
                    if (currAdd % 2) == 1:
                        if (currMuti % 7) == 0:
                            totalAdd = totalAdd + currAdd
                            break

            forthBit = "100000"

            while (True):
                forthBit = str(random.randint(100000, 999999))
                currAdd = 0
                currMuti = 1
                flag = True
                for x in map(int, forthBit):
                    currAdd = currAdd + x
                    currMuti = currMuti * x
                    if (x == 0):
                        flag = False
                if (flag):
                    if (currAdd % 2) == 1:
                        if (currMuti % 12) == 0:
                            totalAdd = totalAdd + currAdd
                            break

            while(len(str(totalAdd)) != 1):
                temp = str(totalAdd)
                currAdd = 0
                for x in map(int, temp):
                    currAdd = currAdd + x
                totalAdd = currAdd

            keyStr = str(totalAdd) + "-" + str(secondBit) + "-" + str(thirdBit) + "-" + str(forthBit)
            self.__currKey = keyStr

            if (not(self.checkSavedKey())):
                break

    def getKey(self):
        return self.__currKey

    def setKey(self, key):
        self.__currKey = key

    def saveKey(self):
        self.__keyLookUp.saveKey(self.getKey())

    def checkSavedKey(self):
        return self.__keyLookUp.checkSavedKey(self.getKey())

    def checkGenKey(self, bitOne, bitTwo, bitThree, BitFour):
        isVaild = True
        addBit = bitOne
        totalAdd = 0

        secondBit = bitTwo
        currAdd = 0
        currMuti = 1
        flag = True
        for x in map(int, secondBit):
            currAdd = currAdd + x
            currMuti = currMuti * x
            if (x == 0):
                flag = False
        if (flag):
            if (currAdd % 2) != 0:
                    if (currMuti % 5) != 0:
                        isVaild = False
        else:
            isVaild = False
        totalAdd = totalAdd + currAdd

        thirdBit = bitThree
        currAdd = 0
        currMuti = 1
        flag = True
        for x in map(int, thirdBit):
            currAdd = currAdd + x
            currMuti = currMuti * x
            if (x == 0):
                flag = False
        if (flag):
            if (currAdd % 2) != 1:
                if (currMuti % 7) != 0:
                    isValid = False
        else:
            isVaild = False
        totalAdd = totalAdd + currAdd

        forthBit = BitFour
        currAdd = 0
        currMuti = 1
        flag = True
        for x in map(int, forthBit):
            currAdd = currAdd + x
            currMuti = currMuti * x
            if (x == 0):
                flag = False
        if (flag):
            if (currAdd % 2) != 1:
                if (currMuti % 12) != 0:
                    isValid = False
        else:
            isVaild = False
        totalAdd = totalAdd + currAdd

        while(len(str(totalAdd)) != 1):
            temp = str(totalAdd)
            currAdd = 0
            for x in map(int, temp):
                currAdd = currAdd + x
            totalAdd = currAdd
        if addBit != currAdd:
            isVaild = False

        return isVaild

if __name__ == "__main__":
    raise Exception("Class can not be run as main. Must be imported!")