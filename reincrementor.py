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


args = args.parse_args()

if args.test:
  print("Test Running")
  log.critical("Test Running")

if args.start:
  start_point = int(args.start)











print("Program Terminated")
log.critical("Program Terminated")