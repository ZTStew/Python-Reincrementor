"""
Description:
  Program creates files to be reincremented
"""

# first value of files being created
i = 1

while(i < 20):
  # creates only even files so that `recount.py` has something to reorder 
  if i % 2 == 0:
    f = open("./Execute/" + str(i) + ".txt", "a")
    f.write(str(i))
    f.close()

  i += 1


