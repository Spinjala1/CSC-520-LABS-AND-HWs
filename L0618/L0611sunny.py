import utils
from utils import rf
import universal
import oddEven

def alterYesToOddEven(inString):
    # Use universal Turing machine to simulate progString on inString
    halts = universal(progString, inString)  # Determine if progString halts on inString

    if halts:
        # Return an output whose length is odd
        return "a"  # Example output of odd length
    else:
        # Return an output whose length is even
        return ""  # Example output of even length

def yesViaOddEven(progString, inString):
    # Invoke alterYesToOddEven to get the modified output
    result = alterYesToOddEven(inString)

    # Check against the properties specified by OddEven
    if len(inString) % 2 == 0:  # |I| is even
        expected_len = 1  # Odd length for output
    else:  # |I| is odd
        expected_len = 0  # Even length for output

    if len(result) == expected_len:
        return 'yes'
    else:
        return 'no'
'''
** L0611 - Explain why your code shows that OddEven is undecidable.
alterYesToOddEven uses universal to determine if progString halts on inString. 
It then produces outputs of different lengths based on whether progString halts or not, thus satisfying the conditions of OddEven.
yesViaOddEven checks if alterYesToOddEven behaves correctly according to OddEven for a given progString and inString.
By constructing alterYesToOddEven in this manner, we effectively demonstrate that deciding OddEven would require solving the Halting Problem, 
which is impossible. 
Therefore, OddEven is undecidable. This completes the proof of undecidability for the OddEven problem.
'''