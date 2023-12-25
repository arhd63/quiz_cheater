# quiz_cheater
The script uses Windows notifications to display the answers to a quiz. Questions and answers should be prepared in advance. The following libraries are used: pytesseract, PIL, win10toast, and fuzzywuzzy.

It is recommended to use Greenshot for the following actions: 
- Press "PrtSc" to highlight the question region.
- Press "Shift + PrtSc" to copy the previous region to the clipboard.

A "Right answer" line ends with ✓, and a separator line for questions begins with ❌. Don't forget to change the file_path! 
Here's an example:
```
file_path = '.../data.txt'
```
The contents of data.txt are structured as follows:
```
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
```
