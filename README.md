# Python Reincrementor
---
## Description:  
Program runs through a given folder and reincrements the files contained within to not have any gaps in the numbering system.

Example:
1, 4, 5, 6, 9 -> 1, 2, 3, 4, 5

Program allows the starting point to be set by the user with the default being `1`

Program determines reincrement order based on current file order


---
### Other Ideas:
- Allow reincrementor to work on non-number files?
- Set reincrementor to run in all sub-directories of current one instead of just the current directory

---
### Usage:
(explanation of how to use the program)
1. Navigate to desired folder in terminal
2. Run `reincrement` or `recount`
3. *Files get automatically renamed*

---
### Arguments:


---
### Test Settings:
python reincrementor.py -t 1 -st 5 -f txt -d 3 -p pre -sf suf -sp _ -n 1
