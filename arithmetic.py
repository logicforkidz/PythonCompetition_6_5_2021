

"""
You ask the user to give a string of single digit numbers and + / - operators. The string can be of any length.
Your job is to evaluate the string as a calculator does and output the result.
For example: If the user entered "2 +3-1" then you should output 4.
There can be one or more spaces between the digits and you should be able to handle them.
You should also ignore any leading or trailing spaces.

Examples of valid input
-----------------------
(a) " 7 - 2 + 3"  => 8
(b) "3 -1 + 3" => 5
(c) " 4 +3+2+2+1+9    -1" => 20
(d) " 5 -5 +5 -5-5-5 +5+5 +5 -2-3+2+3-5" => 0

Handling of Invalid input
--------------------------
You are expected to validate the input to check for errors.
If there are any errors in INPUT then return None  from your function.
Look for the following errors:
1. Leading + or -  i.e the input is like "+2 +3 -1". Here the string is starting with a +
2. Trailing + or -  i.e the input is like "2 +3 -1-". Here the string is ending with a -
3. unexpected characters: if the input has any character that is not a digit or + or - it is invalid input.
4. more than one contiguous digit i.e if the input is "1+32 - 2" it is invalid because 32 has two digits without an operator in between.
5. more than one contiguous operator i.e if the input is "1++3 - 2" it is invalid because there is ++ in it.
6. digits without an operator between them i.e if the input is " 1 3 + 2" it is invalid because 1 and 3 does not have any operator between them.
"""


# Function to evaluate an expression string
#
# takes the string input expression.
#   returns the calculated number if input_expression is valid
#   returns None if input_expression is Invalid.
#
def evaluate_string(input_expression):
    #
    # Write your code here
    #
    return None


if __name__ == '__main__':
    s = input ("Enter your expression:")
    ret = evaluate_string(s)
    if ret == None:
        print ("Invalid Input")
    else:
        print ("Ans is: ", ret)