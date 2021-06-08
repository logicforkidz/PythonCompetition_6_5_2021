def evaluate_string(input_expression):
    # initializations
    value = 0
    mylist = []
    last_was_operator = False
    last_was_digit = False
    valid_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    valid_operators = ['+', '-']

    # if input expresssion is empty string return 0
    if len(input_expression) == 0:
        return 0

    #parse and error check
    for c in input_expression:
        #ERROR-CHECK: if it is one the characters we expect
        if not c.isdigit() and c not in valid_operators and c != ' ':
            return None

        #skip all spaces
        if c == ' ':
            continue

        # digits and operators must alternate
        if c.isdigit():
            #ERROR-check - two consequetive digits?
            if last_was_digit:
                return None
            #push digit on the list
            mylist.append(c)
            last_was_digit = True
        else:
            #ERROR-check: two consequtive operators?
            if not last_was_digit:
                return None
            #push operator on the list
            mylist.append(c)
            last_was_digit = False

    # ERROR-check first and last element should be a digit
    if not mylist[0].isdigit() or not mylist[-1].isdigit():
        return None

    """
    evalute the list.
        we are using op1 to store our result.
        We will start with storing the first element in op1.
        then we will pop one element at a time from the list until all elements have been popped. 
        when the poped element is a + or - we will also pop the next element from the list which and store in op2
        we will then perform the operation on op1 and op2 and store the result back in op1. 
        Finally we will return op1 to the caller as it has the final result. 
    """
    op1 = int(mylist.pop(0))
    while len(mylist):
        op = mylist.pop(0)
        if op in valid_operators:
            op2 = int(mylist.pop(0))
            if op == '+':
                interim_result = op1 + op2
            elif op == '-':
                interim_result = op1 - op2
            #store interim result in op1.
            op1 = interim_result
        else:
            print ("ERROR {op}")
            return None

    # we are done evaluating, op1 has the final result.
    return op1

if __name__ == '__main__':
    s = input ("Enter your expression:")
    ret = evaluate_string(s)
    if ret == None:
        print ("Invalid Input")
    else:
        print ("Ans is: ", ret)