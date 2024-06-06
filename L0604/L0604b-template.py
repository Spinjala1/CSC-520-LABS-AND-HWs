'''
Affirm the honor code as an individual or as a group.
'''


def L0604b(inString):
    # inString is a white-space delimited list of string representations
    # of decimal ints. For example, ' 7 6 5 -2   4' is a valid inString.

    # If inString contains a white-space delimited substring of symbols that
    # is not a valid decimal int, L0604b(inString) == 'no'. For example,
    # L0604b(' 7 -6 5 -2 x0F  8)' == 'no', because 'x0F' is not a valid
    # decimal int.

    # Otherwise, if inString does not contain any representations of positive
    # ints, return 'no'
    
    # Otherwise, L0604b(inString) returns the sum of all positive ints mod 2.
    # For example,L0604b('7 6 5 -2 5') would return 1, because
    # 7+6+5+9 = 27, 27 % 2 == 1. (Note that % is the Python mod operator.
    #

    # Add the needed code.
    #
    
    return '0' # returning a constant value will not work. 

if __name__ == '__main__':

    def test_case(F,string,expected,num,comment=''):
        err = '** '
        result = F(string)
        func_name = str(F).split()[1]
        func_call = f'''{func_name}("{string}")'''
        if result == expected: err = ''
        e = expected
        print (f'{err}test #{num} {func_call}: expected "{e}", received "{result}"')
        print (f'test #{num} Explanation: {comment}\n')
        return num + 1

    F = L0604b
    
    num = 1
    s = '10 5 9 -2'
    exp = '10+5+9 = 24, 24 % 2 = 0' 
    num = test_case(F,1,'0',num,exp)
    
    s = ' -2'
    exp = 'No positive ints'
    num = test_case(F,s,'no',num,exp)    

    s = '  7 -5 16 2 '
    exp = '7+16+2 = 25, 25 % 2 = 1'
    num = test_case(F,s,'1',num,exp)    

    s = 'x1 6 1 10 1 1 -2'
    exp = "x1 does not represent a decimal int"
    num = test_case(F,s,'14',num,exp)

    
