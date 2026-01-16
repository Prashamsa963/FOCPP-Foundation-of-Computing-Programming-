Introduction to Programming – Week 4

Lab Logbook Summary

Overview

This lab focused on functions in Python. Functions help organise code, reduce repetition, and make programs easier to read and maintain. The lab covered importing functions, creating custom functions, using arguments, returning values, and writing short lambda functions.

Using Functions and Modules

Python has many built-in functions like print() and input(). Extra functions are stored in modules and must be imported before use.

Common import methods:

import module_name
from module_name import function_name
The math module was used to perform mathematical operations such as square roots and logarithms.

Defining Functions

Functions are created using the def keyword.

A function has a name and parameters
The code inside the function runs when it is called
Variables inside a function are local and only work within the function
Functions allow code to be reused and make programs more organised.

Docstrings

Functions can include docstrings to explain what they do.

Written using triple quotes
Help other users understand the function
Can be viewed using help()
Good documentation improves code quality.

Returning Values

Functions can send results back using return.

return ends the function
Returned values can be stored in variables
If no value is returned, the function returns None
Default Arguments

Functions can have default values for parameters.

Makes function calls easier
Default parameters must come after required ones
If no value is provided, the default is used
Keyword Arguments

Functions can be called using parameter names.

Order does not matter
Makes code clearer
Required arguments must still be given
Variable-Length Arguments

Functions can accept any number of arguments using *args.

Arguments are stored in a tuple
Useful when the number of inputs is unknown
Lambda Expressions

Lambda functions are small, one-line functions.

Written using the lambda keyword
Used for short and simple operations
Do not need a function name
Key Terms Learned

Function
Parameter
Argument
Return
Docstring
Module
Lambda
Conclusion

This lab improved understanding of functions and modular programming in Python. Using functions makes programs cleaner, reusable, and easier to maintain, which is important for larger programs.