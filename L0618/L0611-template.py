'''
On our honor, as SFSU students, we, Sripranav Pinjala, Annison Van, John King, and Subhan Khan,
did not give or receive inappropriate help with this assignment. All group members contributed
to this work, and all concur with the submission. We understand that we will be asked to redo
the assignment in person if this work presents any question of an honor code violation.
'''

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

'''
This program demonstrates the undecidability of the OddEven problem. OddEven problem shows
if the given program produces outputs of the correct length parity (odd or even) based on
input length parity. The function alterYesToOddEven determines whether a given program such
as progString stops on a specific input which is newInString and returns a string based on
the condition. YesViaOddEven function is used to determine if OddEven condition holds for 
the given progString and inString values. This program uses undecidability of the Halting
Problem to prove that the OddEven problem is undecidable as well. This shows no algorithm
is really able to decide OddEven problem, showing its undecidability. 

'''
