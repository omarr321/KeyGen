#!/usr/bin/env python3

import sys
import os

import KeyGen


class Key:
    def start(self):
        keyCurr = KeyGen.KeyGen()
        currSwitchNumber = 0
        while(True):
            match currSwitchNumber:
                case 0:
                    print("WELCOME TO\n _________________________________________________________ \n(( ┏┓┏━┓━━━━━━━━━━━━━┏━━━┓━━━━━━━━━━━━┏━━━┓┏━━━┓┏━━━┓┏┓  ))\n ))┃┃┃┏┛━━━━━━━━━━━━━┃┏━┓┃━━━━━━━━━━━━┃┏━┓┃┃┏━┓┃┃┏━┓┃┃┃ (( \n(( ┃┗┛┛━┏━━┓┏┓━┏┓━━━━┃┃━┗┛┏━━┓┏━┓━━━━━┃┗━┛┃┃┗━┛┃┃┃━┃┃┃┃  ))\n ))┃┏┓┃━┃┏┓┃┃┃━┃┃━━━━┃┃┏━┓┃┏┓┃┃┏┓┓━━━━┃┏━━┛┃┏┓┏┛┃┃━┃┃┗┛ (( \n(( ┃┃┃┗┓┃┃━┫┃┗━┛┃━━━━┃┗┻━┃┃┃━┫┃┃┃┃━━━━┃┃━━━┃┃┃┗┓┃┗━┛┃┏┓  ))\n ))┗┛┗━┛┗━━┛┗━┓┏┛━━━━┗━━━┛┗━━┛┗┛┗┛━━━━┗┛━━━┗┛┗━┛┗━━━┛┗┛ (( \n(( ━━━━━━━━━┏━┛┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ))\n ))━━━━━━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ (( \n((-------------------------------------------------------))")
                    print("\nWhat would you like to do?")
                    print("1 | Generate a new key")
                    print("2 | Check an existing key")
                    print("3 | Credits")
                    print("4 | Quit")
                    while (True):
                        selector = input(">>>")
                        try:
                            selector = int(selector)
                            if (selector < 1 or selector > 4):
                                print("Error: The number must be between 1 and 4!")
                            else:
                                break
                        except:
                            print("Error: Input is not a number!")
                    currSwitchNumber = selector
                case 1:
                    keyCurr.genNewKey()
                    print("\nKey: " + keyCurr.getKey() + "\n")
                    print("Would you like to save the key to the database?")
                    print("1 | Yes")
                    print("2 | No")
                    while (True):
                        selector = input(">>>")
                        try:
                            selector = int(selector)
                            if (selector < 1 or selector > 2):
                                print("Error: The number must be between 1 and 2!")
                            else:
                                break
                        except:
                            print("Error: Input is not a number!")
                    if (selector == 1):
                        keyCurr.saveKey()
                    currSwitchNumber = 0
                case 2:
                    loadedKey = ""
                    loadedKeySplit = ""
                    print("Please type in the key including the dashs:")
                    while(True):
                        try:
                            currInput = input(">>>")
                            currInput = str(currInput)
                            tempInput = currInput.split("-")
                            isCorrect = True
                            if (len(tempInput[0]) != 1):
                                print(tempInput[0])
                                isCorrect = False
                            if (len(tempInput[1]) != 4):
                                print(tempInput[1])
                                isCorrect = False
                            if (len(tempInput[2]) != 6):
                                print(tempInput[2])
                                isCorrect = False
                            if (len(tempInput[3]) != 6):
                                print(tempInput[3])
                                isCorrect = False

                            if (isCorrect):
                                loadedKeySplit = tempInput
                                loadedKey = currInput
                                break
                        except IndexError:
                            pass
                        print("Error: The key is not in the correct format!")

                    if (keyCurr.checkGenKey(loadedKeySplit[0], loadedKeySplit[1], loadedKeySplit[2], loadedKeySplit[3])):
                        print("Key is vaild")
                    else:
                        print("Key is invaild")
                        
                case 3:
                    print("\nCredits:")
                    print("Omar Radwan - Programmer & Designer")
                    print("\nTYPE ANYTHING TO CONTINUE")
                    input(">>>")
                    currSwitchNumber = 0
                case 4:
                    print ("\nGood Bye!")
                    break

if __name__ == "__main__":
    program = Key()
    program.start()