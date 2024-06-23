import universal
import computesLen  # This is an Oracle function, provided in your environment
from utils import rf  # Assuming rf reads the function's code from a file

# Global variable for showing function alteration.
mod_behavior = None

def alterYesToLen(inString):
    global mod_behavior
    # Behavior changing of function based on input. This is returning length of its own input.
    mod_behavior = str(len(inString))

def yesViaLen(progString, inString):
    global mod_behavior
    # Using mod_behavior for simulation.
    alterYesToLen(inString)  # Would modify the function's behavior
    # Verify if the function, alterYesToLen with global state is shown by computesLen making input length as a string.
    result = computesLen(progString)
    # Evaluate modified function behavior, reset global state to prevent side effects and return the result.
    mod_behavior = None
    return result

'''
** H1 - Explain why your code shows that computesLen is undecidable.
The provided solution demonstrates that `ComputesLen` is undecidable by simulating a scenario 
similar to solving the Halting Problem. In `alterYesToLen`, we simulate a change in function behavior 
using a global variable. This change makes the function behave as if it returns the length of its input 
as a string. `yesViaLen` then determines if this simulated behavior change enables the function to compute 
the length correctly. This approach reflects the challenge of determining function behavior without direct 
execution, similar to the undecidability of the Halting Problem. Hence, by this theoretical reduction, if 
we could decide `ComputesLen`, we would be able to solve the Halting Problem, which is known to be undecidable. 
Therefore, `ComputesLen` must also be undecidable.
'''