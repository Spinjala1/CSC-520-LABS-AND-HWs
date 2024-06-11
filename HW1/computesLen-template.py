
import utils; from utils import rf
import universal
import computesLen # Oracle function

## ** H1 - Do not define any functions besides alterYesToLen and yesViaLen,
## ** and do not modify alterYesToLen to return another function.

def alterYesToLen(inString):
    ## ** H1 Add code needed before the call to universal ** 
    originalOutput = universal('{progString}', inString)
    if originalOutput == 'yes':
        return str(len(inString))
    return originalOutput

   val = universal(progString,newInString)

    ## ** H1 Add code needed after the call to universal ** 


def yesViaLen(progString,inString):
    ## ** H1 - Add code needed before the call to computesLen

    # Add 2nd parameter if needed
    result = computesLen(rf('alterYesToLen.py'), … )

    ## ** H1 - Add code needed after the call to computesLen


'''
** H1 - Explain why your code shows that computesLen is undecidable.


'''

