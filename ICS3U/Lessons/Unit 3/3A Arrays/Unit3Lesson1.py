# Original string
progname = "Python"

# Prediction A: print(progname)
# Output: Python
print(progname)

# Prediction B: print(progname[0])
# Output: P (first character at index 0)
print(progname[0])

# Prediction C: Loop through each character and print it without newline or separator
for c in progname:
    print(c, sep="", end="")  # D: Purpose of sep="" and end="" is to print all characters on the same line without spaces or newlines
print()  # E: Empty print() outputs a newline to move cursor to the next line after the loop

# Prediction F: Loop through indices and print index and corresponding character
for c in range(len(progname)):
    print(c, progname[c])
