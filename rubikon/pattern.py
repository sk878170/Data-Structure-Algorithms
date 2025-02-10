# *
# **
# ***
# ****

rows=int(input("Enter the no of rows for the pattern: "))
for i in range(1,rows+1):
    print("*"*i)

#    *
#   **
#  ***
# ****
rows=5
for i in range(0,rows+1):
    print(" "*(rows-i)+"*"*i)

# ****
# ***
# **
# *

rows=int(input("Enter the no of rows for the pattern: "))
for i in range (1,rows+1):
    print('*'*(rows-i))


# ****
#  ***
#   **
#    *
rows=int(input("Enter the no of rows for the pattern: "))
for i in range (0,rows+1):
    print(' '*i+'*'*(rows-i))


#   *
#  ***
# *****
rows=int(input("Enter the no of rows for the pattern: "))
for i in range(1,rows+1):
    print(" "*(rows-i)," *"*(i))

# *****
#  ***
#   *

rows=int(input("Enter the no of rows for the pattern: "))
for i in range(0,rows+1):
    print(" "*i,' *'*(rows-i))

# *****
#  ***
#   *
#   *
#  ***
# *****

rows=int(input("Enter the no of rows for the pattern: "))
for i in range(1,rows):
    print(" "*i,' *'*(rows-i))

for i in range(1,rows):
    print(" "*(rows-i)," *"*(i))

#   *
#  ***
# *****
#  ***
#   *

rows=int(input("Enter the no of rows for the pattern: "))
for i in range(1,rows):
    print(" "*(rows-i)," *"*(i))
for i in range(0,rows):
    print(" "*i,' *'*(rows-i))

# *     *
# **   **
# *** ***
# *******
# *** ***
# **   **
# *     *


rows=int(input("Enter the no of rows for the pattern: "))
for i in range(1,rows+1):
    print("*"*i+" "*(rows-i)+" "+" "*(rows-i)+"*"*i)
for i in range(rows-1,0,-1):
    print("*"*i+" "*(rows-i)+" "+" "*(rows-i)+"*"*i)


# *****
# ** **
# *   *
# ** **
# *****

rows=int(input("Enter the no of rows for the pattern: "))
for i in range(0,rows):
    print("*"*(rows-i)+" "*i+" "*i+"*"*(rows-i))
for i in range(rows-1,-1,-1):
    print("*"*(rows-i)+" "*i+" "*i+"*"*(rows-i))

#    *
#   ***
#  *****
# *******
# *** ***
#  *   *


rows=int(input("Enter the no of rows for the pattern: "))
for i in range(1,rows+1):
    print(" "*(rows-i)+" *"*(i))
for i in range(0,rows):
    print("*"*(rows-i)+" "*i+" "*i+"*"*(rows-i))

#   *
#  ***
# *****
# ****
# ***
# **
# *
rows=int(input("Enter the no of rows for the pattern: "))
for i in range(1,rows+1):
    print(" "*(rows-i)+" *"*(i))
for i in range (1,rows+1):
    print(' *'*(rows-i))

#    ****
#   ****
#  ****
# ****
rows=int(input("Enter the no of rows for the pattern: "))
for i in range(0,rows+1):
    print(" "*(rows-i)+"*"*rows)









