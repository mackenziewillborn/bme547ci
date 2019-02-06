# bme547ci
Tachycardia Assignment 

### Background
With the transition towards electronic medical records, many paper records are
being scanned into a digital format.  [Optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition)
(OCR) is used so that the scanned text is searchable.  Depending on the 
quality of the paper records (often derived from faxes), the quality of the 
OCR result may not be perfect.  Therefore, any code that is looking to 
interpret the scanned results needs to be flexible enough to read results that
may be slightly off.  This assignment simulates a small example of such a
problem.  

Tachycardia is a heart rate that exceeds the normal resting heart rate.  In
this assignment, you will be writing a function that could be used to
interpret whether a string obtained from OCR of medical records contains the 
word "tachycardic". 

### Function Specifications
* Should be named `is_tachycardic` and located in a module called 
`tachycardia.py`
* It should take a string argument as input.
* This string will only contain a single word, but there is no guarantee
whether the word will be upper case, lower case, mixed case, or have leading /
trailing spaces or punctuation.
* If the string contains the word "tachycardic," regardless of capitalization,
the function should return a value of `True`
* Otherwise, the function should return a value of `False`.
* Function must follow the PEP-8 style guide.

### Approach
* Create a public GitHub repository in your account with `bme547ci` somewhere 
in the name
* Clone this repository to your local computer
* Develop code on a feature branch
* Develop appropriate unit tests, including PEP-8 style check.
* Enable and use TravisCI in this repository
* Push code to GitHub
* Generate Pull Request on GitHub to merge your feature branch into the master
branch only after Travis CI reports a passing status.
* Tag final submission on the master branch as `v1.0.0`


### Grading Criteria
* Good git workflow usage (good commit messages and frequency, use of branches,
pull requests, etc.)
* Meeting the functional specifications above
* Presence of comprehensive unit testing to ensure that the appropriate range 
of possible string inputs are successfully identified or rejected
* The use of `@pytest.mark.parametrize` for at least one unit test
* Appropriate naming and syntax for unit tests
* Implementation of Travis CI
* Appropriate use of virtual environments

### Small Bonus:
Make your `is_tachycardic` function more tolerant to close representations of
the word `tachycardic`.  For example, it should be able to tolerate 1 to 2
missing letters (ex. `tachycrdic`) and/or 1 to 2 misspelled letters
(ex. `tachycard1c`)
