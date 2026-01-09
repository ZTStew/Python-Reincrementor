"""
Description:
"""

import os, argparse
import logging as log
from os import walk

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


blacklist = [".empty"]

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
  "-p",
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


print(f"Arguments: Test: {test_mode} | Start Point: {start_point} | File Type: {file_type} | Digits: {digits} | Prefix: {prefix} | Suffix: {suffix} | Space: `{space}`")
log.critical(f"Arguments: Test: {test_mode} | Start Point: {start_point} | File Type: {file_type} | Digits: {digits} | Prefix: {prefix} | Suffix: {suffix} | Space: `{space}`")


run_location = "./"
if test_mode:
  run_location = "./Execute"

# searches through run location for files that can be reincremented
files = []
for (dirpath, dirnames, filenames) in walk(run_location):
  files.extend(filenames)
  break
# print(files)

# Removes any Blacklisted files from `files`
n_files = []

for file in files:
  for black in blacklist:
    if not file.endswith(black):
      n_files.append(file)

files = n_files
# print(files)

# Checks `files` list for specified file_type
if file_type:
  n_files = []

  for file in files:
    if file.endswith(file_type):
      n_files.append(file)

  files = n_files
# print(files)

# Removes any files in `files` list that contain a non-integer value in the name
if numeric > 0:
  n_files = []

  for file in files:
    try:
      n_files.append(str(int(file.split(".")[0])))
    except:
      pass

  files = n_files
# print(files)


# identifies the longest file name in `files` so that each file can be preceded with 0's. This will help with sorting.
depth = 1
for l in files:
  if len(l.split(".")[0]) > depth:
    depth = len(l.split(".")[0])

if digits == 0:
  digits = depth
elif digits < depth:
  digits = depth

# print(digits)


# renames files in `files` so that they can be accurately sorted
for z in range(len(files)):
  files[z] = files[z].split(".")[0].zfill(digits)
  print(files[z])

# sorts files
files.sort()

# print(files)




print("Program Terminated")
log.critical("Program Terminated")