'''
Affirm an individual or group honor code by replacing <name> or <names>.
`
For individual submissions: I, <name>, have neither given or recived inappropriate help with this lab assignment.

For group submissions: We, <names>, have neither given or recived inappropriate help with this lab assignment. All group members participated in this work, and all concur with this submission.
'''

# Turn diagnostics on/off by setting VERBOSE True/False. 
VERBOSE = True 


def L4(inString):
    parts = inString.split()
    
    positive_mod_count = 0
    last_negative = None
    
    for part in parts:
        try:
            num = int(part)
            
            if num < 0:
                last_negative = num
            elif num > 0 and num % 3 == 2:
                positive_mod_count += 1
        except ValueError:
            return 'no'  # Return 'no' if any part is not a valid integer
    
    if last_negative is None:
        return 'no'  # Return 'no' if there are no negative integers
    
    # Check if count of positive integers equal to 2 mod 3 matches absolute value of last negative integer
    if positive_mod_count != abs(last_negative):
        return 'no'
    
    return 'yes'

# Test harness function
def test_case(F, string, expected, num, comment=''):
    err = '**'
    result = F(string)
    func_name = str(F).split()[1]
    func_call = f'{func_name}("{string}")'
    
    if result == expected:
        err = ''
    
    e = expected
    print(f'{err}{func_call}: expected "{e}", received "{result}"')
    print(f'test #{num} Explanation: {comment}')
    return num + 1

# Test cases
num = 1
s = '7 -6 5 -2 8'
exp = '2 positive ints = 2 mod 3, -2 is the last negative int'
num = test_case(L4, s, 'yes', num, exp)

s = '-1 1 -2 3 -5 8'
exp = 'Only one positive int equal to 2 mod 3, not 5'
num = test_case(L4, s, 'no', num, exp)

s = '1 1 2 3 5 8'
exp = 'no negative ints'
num = test_case(L4, s, 'no', num, exp)

s = '7 -6 5 -2 x0F 8'
exp = 'x0F is not a valid representation of a decimal int'
num = test_case(L4, s, 'no', num, exp)
    
