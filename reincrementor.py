"""
Description:
"""

import os, argparse
import logging as log

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

start_point = 1
file_type = "*"
digits = 1

args = argparse.ArgumentParser()
args.add_argument(
  "-t",
  "--test",
  type=int,
  help="Declair if the application should run in test mode [0 -> production (default) | 1 -> test mode]."
)
args.add_argument(
  "-s",
  "--start",
  type=int,
  help="Declair start value for reincrementing."
)
args.add_argument(
  "-f",
  "--file",
  type=str,
  help="Declair a specific file type to be reincremented. Default all files."
)
args.add_argument(
  "-f",
  "--file",
  type=str,
  help="Declair a specific file type to be reincremented. Default all files."
)
args.add_argument(
  "-d",
  "--digits",
  type=int,
  help="Declair how many digits the file name should have. Default 1. Example: 3 -> `008.file`"
)
args.add_argument(
  "-p",
  "--prefix",
  type=str,
  help="Declair if the reincremented files should have a prefix in front of the number ([space] automatically added after). Example: pre -> `pre 008.file`"
)
args.add_argument(
  "-s",
  "--suffix",
  type=str,
  help="Declair if the reincremented files should have a suffix after the number ([space] automatically added before). Example: suf -> `008 suf.file`"
)
args.add_argument(
  "-sp",
  "--space",
  type=str,
  help="Defines what the `space` symbol should be in reincremented file name. Default ` `. Works with --prefix and/or --suffix. Example: `_` -> `008_suf.file`"
)




args = args.parse_args()

if args.test:
  print("Test Running")
  log.critical("Test Running")

if args.start:
  start_point = int(args.start)

# NOTE need to format around `.`
if args.file:
  file_type = args.file

if args.digits:
  digits = args.digits








print("Program Terminated")
log.critical("Program Terminated")