"""Comparing two strings or numbers"""
VARA = input("Enter the string1:")
VARB = input("Enter the string2:")
if (VARA.isnumeric() and VARB.isnumeric()):
    print("Strings not involved")
    if int(VARA) > int(VARB):
        print("bigger")
    elif int(VARA) == int(VARB):
        print("equal")
    elif int(VARA) < int(VARB):
        print("smaller")
else:
    print("string involved")
    if len(VARA) > len(VARB):
        print("bigger")
    if len(VARA) == len(VARB):
        print("equal")
    if len(VARA) < len(VARB):
        print("smaller")
