"""
Description: Program runs through a given folder and reincrements the files contained within to not have any gaps in the numbering system.
"""

import os, argparse, math, shutil
import logging as log
from os import walk
from operator import itemgetter

path = os.path.dirname(os.path.abspath(__file__)) + '\\Log\\template.log'

log.basicConfig(
    filename= path,
    level=log.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# log.debug("debug message")
# log.info("info message")
# log.warning("warning message")
# log.error("error message")
# log.critical("critical message")

log.critical("### ### ### V Program Starts V ### ### ###")

# List of any files (ends) that should not be automatically edited
blacklist = [".empty", ".gitignore", ".md"]

test_mode = False
start_point = 1
file_type = ""
numeric = 0
digits = 0
prefix = ""
suffix = ""
space = " "

args = argparse.ArgumentParser()
args.add_argument(
  "-t",
  "--test",
  type=int,
  help="(Optional) Declair if the application should run in test mode [0 -> production (default) | 1 -> test mode]."
)
args.add_argument(
  "-st",
  "--start",
  type=int,
  help="(Optional) Declair start value for reincrementing."
)
args.add_argument(
  "-f",
  "--file",
  type=str,
  help="(Optional) Declair a specific file type to be reincremented. Default all files."
)
args.add_argument(
  "-n",
  "--numeric",
  type=int,
  help="(Optional) Declair if the application should only work on files containing exclusively integers [0 -> all characters allowed (default) | 1 -> integer only]."
)
args.add_argument(
  "-d",
  "--digits",
  type=int,
  help="(Optional) Declair how many digits the file name should have. Default 1. Example: 3 -> `008.file`"
)
args.add_argument(
  "-pf",
  "--prefix",
  type=str,
  help="(Optional) Declair if the reincremented files should have a prefix in front of the number (`--space` automatically added after). Default \"\". Example: pre -> `pre 008.file`"
)
args.add_argument(
  "-sf",
  "--suffix",
  type=str,
  help="(Optional) Declair if the reincremented files should have a suffix after the number (`--space` automatically added before). Default \"\". Example: suf -> `008 suf.file`"
)
args.add_argument(
  "-sp",
  "--space",
  type=str,
  help="(Optional) Defines what the `space` symbol should be in reincremented file name. Default \"\". Works with --prefix and/or --suffix. Example: `_` -> `008_suf.file`"
)


args = args.parse_args()

if args.test:
  print("Test Running")
  log.critical("Test Running")
  test_mode = True

if args.start:
  start_point = int(args.start)
start_point = abs(start_point)

if args.file:
  file_type = args.file

if args.numeric:
  numeric = args.numeric

if args.digits:
  digits = args.digits

if args.prefix:
  prefix = args.prefix

if args.suffix:
  suffix = args.suffix

if args.space:
  space = args.space

if (len(prefix) <= 0) and (len(suffix) <= 0):
  space = ""



print(f"Arguments: Test: {test_mode} | Start Point: {start_point} | File Type: `{file_type}` | Digits: {digits} | Prefix: {prefix} | Suffix: {suffix} | Space: `{space}`")
log.critical(f"Arguments: Test: {test_mode} | Start Point: {start_point} | File Type: `{file_type}` | Digits: {digits} | Prefix: {prefix} | Suffix: {suffix} | Space: `{space}`")


run_location = "./"
if test_mode:
  run_location = "./Execute"

# searches through run location for files that can be reincremented
# files = [{'original': "og", 'new': "nw"}]
files = []
for (dirpath, dirnames, filenames) in walk(run_location):
  for file in filenames:
    files.append({'original': file, 'new': file})
  break
# print(files)


# Removes any Blacklisted files from `files`
n_files = []

for file in files:
  blacklisted = False
  for black in blacklist:
    if black in file['new']:
      blacklisted = True
  if not blacklisted:
    n_files.append(file)
  else:
    file['new'] = ""
    n_files.append(file)

files = n_files
# print(files)


# Checks `files` list for specified file_type
if file_type:
  n_files = []

  for file in files:
    # whitelisted files
    if file['new'].endswith(file_type):
      n_files.append(file)

    # non-whitelisted files
    else:
      file['new'] = ""
      n_files.append(file)

  files = n_files
# print(files)


# Removes any files in `files` list that contain a non-integer value in the name
if numeric > 0:
  n_files = []

  for file in files:
    try:
      file['new'] = str(int(file['new'].split(".")[0]))
      n_files.append(file)
    except:
      file['new'] = ""
      n_files.append(file)

  files = n_files
# print(files)


for file in files:
  # Adds file extension to each `file`
  file['extension'] = file['original'].split('.')[-1]
# print(files)


# identifies the longest file name in `files` so that each file can be preceded with 0's. This will help with sorting.
depth = 1
for l in files:
  if len(l['new'].split(".")[0]) > depth:
    depth = len(l['new'].split(".")[0])
# print(digits)


# renames files in `files` so that they can be accurately sorted
for z in range(len(files)):
  if files[z]['new'] != "":
    files[z]['new'] = files[z]['new'].split(".")[0].zfill(digits)


# Sorts files by name
files = sorted(files, key=itemgetter('new'))


# If user did not assign a value for `digits`
if digits == 0:
  digits = math.ceil(len(files) / 10)


# prevents leading or trailing spaces
if prefix:
  prefix = prefix + space
if suffix:
  suffix = space + suffix
# print(files)


# Creates temporary folder to store renamed files to prevent naming collisions with yet to be named files in initial folder
# path made to be as unlikely as possible to have a collision
if test_mode:
  temp_path = "Execute/llltemplll"
else:
  temp_path = "llltemplll"
if not os.path.exists("./" + temp_path):
  os.makedirs("./" + temp_path)


# value of `start_point` is consistantly too high
start_point = start_point - 1


i = 0
while i < len(files):
  if len(files[i]['new']) > 0:
    # Prints output file name without saving or modifying file system
    # print("./" + temp_path + "/" + prefix + "{:0{leading}d}".format(start_point, leading=digits) + suffix + "." + files[i]['extension'])
    
    if test_mode:
      os.rename('./Execute/' + files[i]['original'], './' + temp_path + "/" + prefix + "{:0{leading}d}".format(start_point, leading=digits) + suffix + "." + files[i]['extension'])
    else:
      os.rename('./' + files[i]['original'], './' + temp_path + "/" + prefix + "{:0{leading}d}".format(start_point, leading=digits) + suffix + "." + files[i]['extension'])

  start_point += 1
  i += 1

# Moves renamed files from temp directory back into parent directory
file_names = os.listdir("./" + temp_path)
for file_name in file_names:
    if test_mode:
      shutil.move(os.path.join("./" + temp_path, file_name), "./Execute")
    else:
      shutil.move(os.path.join("./" + temp_path, file_name), "./")


# Removes temp folder after program finishes
try:
  shutil.rmtree("./" + temp_path)
  log.info("Temp folder successfully deleted.")
except Exception as e:
  # print("ERROR: " + str(e))
  log.error("ERROR: " + str(e))

print(str(len(files)) + " Files Have Been Renamed.")
log.info(str(len(files)) + " Files Have Been Renamed.")

print("Program Terminated")
log.critical("Program Terminated")