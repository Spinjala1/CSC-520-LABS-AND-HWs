'''
On our honor, as SFSU students, we, Sripranav Pinjala, Annison Van,and Subhan Khan, did
not give or receive inappropriate help with this assignment. All group members contributed
to this work, and all concur with the submission.We understand that we will be asked to
redo the assignment in person if this work presents any question of an honor code violation.
'''


def L0604b(inString):
    # Split the input string into individual elements
    elements = inString.split()
    
    # Initialize variables to keep track of positive integers and the sum
    positive_int_sum = 0
    has_positive_int = False

    # Iterate through each element in the input string
    for element in elements:
        try:
            num = int(element)
            if num > 0:
                positive_int_sum += num
                has_positive_int = True
        except ValueError:
            return 'no'  # If any element is not a valid integer, return 'no'

    if not has_positive_int:
        return 'no'  # If no positive integers are found, return 'no'

    return str(positive_int_sum % 2)  # Return the sum of positive integers modulo 2 

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
    num = test_case(F,s,'0',num,exp)
    
    s = ' -2'
    exp = 'No positive ints'
    num = test_case(F,s,'no',num,exp)    

    s = '  7 -5 16 2 '
    exp = '7+16+2 = 25, 25 % 2 = 1'
    num = test_case(F,s,'1',num,exp)

    s = 'x7 -5 16 2'
    exp = "x7 does not represent a decimal int"
    num = test_case(F, s, 'no', num, exp)

    
