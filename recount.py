"""
Description:
  Program is intended to, when called, take all files of a specified type and rename them based on their pre-existing
  alphabetical order in the form of 1, 2, 3...

Arguments:
  file (str) -> file type that is being reincremented 
  start (int) -> the point for the reincrement to start | default 0
"""

import os, argparse
import logging as log

log.basicConfig(
    filename=os.path.dirname(os.path.abspath(__file__)) + '\\log\\recount.log',
    level=log.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# log.debug("debug message")
# log.info("info message")
# log.warning("warning message")
# log.error("error message")
# log.critical("critical message")


log.critical("### ### ### V Program Starts V ### ### ###")

args = argparse.ArgumentParser()
args.add_argument(
  "-f",
  "--file",
  type=str,
  help="Specify the file type."
)
args.add_argument(
  "-s",
  "--start",
  type=int,
  help="Specify the starting value of the recounted files."
)
args.add_argument(
  "-p",
  "--padding",
  type=int,
  help="Specify the zero-padding depth of the recounted file names. (default) 1 = 2 | 2 = 02 | 3 = 002"
)

args.add_argument(
  "-t",
  "--test",
  type=int,
  help="Declair if the application should run in test mode [0 -> production (default) | 1 -> test mode]."
)

args = args.parse_args()
file_type = args.file
start = args.start

if not file_type:
  file_type = "*"

if not start:
  start = 0
else:
  try:
    start = int(start)
  except:
    log.error("ERROR: Invalid starting point")
    print("ERROR: Invalid starting point")

print(file_type)
print(start)

if args.test:
  log.critical("Test Running")

# gets a list of all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]
# must sort the array of files as according to a computer's file system '10' comes before '2'
# print(files)
# identifies the longest file name in `files` so that each file can be preceded with 0's. This will help with sorting.
depth = 1
for l in files:
  if len(l.split(".")[0]) > depth:
    depth = len(l.split(".")[0])

# renames files in `files` so that they can be accurately sorted
for z in range(len(files)):
  files[z] = files[z].split(".")[0].zfill(depth)

# sorts files
files.sort()

print(files)




