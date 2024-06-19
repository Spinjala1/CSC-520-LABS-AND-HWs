from utils import rf
import universal
import oddEven # Oracle function

def alterYesToOddEven(progString):
    ## ** L0611 Add code needed before the call to universal **
    modifiedProgString = "definition P(I): return " + progString
    newInput = "I"
    ## ** L0611 Add code needed after the call to universal **
    result = universal(modifiedProgString, newInput)
    if result:
        return "yes"
    else:
        return "no"

def yesViaOddEven(progString, inString):
    ## ** L0611 - Add code needed before the call to computesLen
    oddEvenResult = oddEven(rf('alterYesToOddEven.py'), progString)
    ## ** L0611 - Add code needed after the call to computesLen
    if oddEvenResult == "yes":
        return True
    else:
        return False


'''
** L0611 - Explain why your code shows that OddEven is undecidable.

'''