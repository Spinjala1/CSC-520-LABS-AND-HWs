from lenMinus1 import lenMinus1

def weirdLen(progString):
    if progString == rf('weirdLen.py'):
        return lenMinus1(progString)
    else:
        return str(len(progString))