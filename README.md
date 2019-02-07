# bme547ci
Tachycardia Assignment 

### Background
Tachycardia is a heart rate that exceeds the normal resting heart rate.  In
this assignment, I have written a function that could be used to
interpret whether a string obtained from OCR of medical records contains the 
word "tachycardic". 

### Function Specifications
* Function is named `is_tachycardic` and located in a module called 
`tachycardia.py`
* Function takes a string argument as input.
* This string can only contain a single word, but there is no guarantee
whether the word will be upper case, lower case, mixed case, or have leading /
trailing spaces or punctuation.
* If the string contains the word "tachycardic," regardless of capitalization,
the function will return a value of `True`
* Otherwise, the function will return a value of `False`.
* Function follows the PEP-8 style guide.

### Unit Testing 
* The test_tachycardia.py file contains unit tests for the tachycardia.py function 
* There is a test to make sure the function can catch False cases 
* There is also a parametrized test to test mulitple different input cases 
