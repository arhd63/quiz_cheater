# quiz_cheater
Script uses windows notification to display the answers to quiz. Questions and answers should be prepared ahead.

Used libs: pytesseract, PIL, win10toast, fuzzywuzzy

Recommend to use Greenshot:
  1. PrtSc -> Highlight question region
  2. Shift + PrtSc -> Copy in Clipboard previous region

"Right answer" line ends with ✓.

Separator line for questions begins with ❌.

Do not forget to change file_path!

Example:

file_path='.../data.txt'.

data.txt:

  Question 1 (must be in one line)
  
  1 Wrong answer
  
  2 Wrong answer
  
  Right answer✓
  
  3 Wrong answer
  
  ....
  
  ❌
  
  Question 2 ...
  
  ....
  
  Right answer✓
  
  ....
  
  ❌
