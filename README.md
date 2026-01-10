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
- `--help`: (Optional) Lists all program arguments
- `--test`: (Optional) Declair if the application should run in test mode [0 -> production (default) | 1 -> test mode].
- `--start`: (Optional) Declair start value for reincrementing.
- `--file`: (Optional) Declair a specific file type to be reincremented. Default all files.
- `--numeric`: (Optional) Declair if the application should only work on files containing exclusively integers [0 -> all characters allowed (default) | 1 -> integer only].
- `--digits`: (Optional) Declair how many digits the file name should have. Default 1. Example: 3 -> `008.file`
- `--prefix`: (Optional) Declair if the reincremented files should have a prefix in front of the number (`--space` automatically added after). Default \"\". Example: pre -> `pre 008.file`
- `--suffix`: (Optional) Declair if the reincremented files should have a suffix after the number (`--space` automatically added before). Default \"\". Example: suf -> `008 suf.file`
- `--space`: (Optional) Defines what the `space` symbol should be in reincremented file name. Default \"\". Works with --prefix and/or --suffix. Example: `_` -> `008_suf.file`

---
### Test Settings:
python reincrementor.py -t 1 -st 5 -f txt -d 3 -p pre -sf suf -sp _ -n 1
