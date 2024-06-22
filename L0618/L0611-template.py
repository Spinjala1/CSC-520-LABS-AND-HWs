import utils
from utils import rf
import universal
import oddEven  # Oracle function

def alterYesToOddEven(inString):
    ## ** L0611 Add code needed before the call to universal **
    progString, newInString = utils.DESS(inString)
    halts = universal(progString, newInString)

    ## ** L0611 Add code needed after the call to universal **
    if halts:
        # Return a string with odd length.
        return "a"
    else:
        # Return a string with even length.
        return "ab"

def yesViaOddEven(progString, inString):
    ## ** L0611 - Add code needed before the call to computesLen
    # Add a second parameter only if needed.
    result = oddEven(rf('alterYesToOddEven.py'), inString)

    ## ** L0611 - Add code needed after the call to computesLen
    # Check expected parity of the output length
    if len(inString) % 2 == 0:
        # Expecting odd length for output.
        expected_parity = 1
    else:
        # Expecting even length for output.
        expected_parity = 0

    # Check if the length of the result equals expected parity.
    if len(result) % 2 == expected_parity:
        return 'yes'
    else:
        return 'no'
