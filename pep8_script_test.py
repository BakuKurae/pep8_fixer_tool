import pycodestyle
import re
from io import StringIO
import sys

old_stdout = sys.stdout
sys.stdout = my_stdout = StringIO()

fchecker = pycodestyle.Checker('test.py', show_source=False)
file_errors = fchecker.check_all()
sys.stdout = old_stdout
print("Found %s errors (and warnings)" % file_errors)
# print(my_stdout.getvalue().split("\n")[:-1])
codes = []
for code in my_stdout.getvalue().split("\n")[:-1]:
    codes.append(re.findall("(?<=: )(.{4})", code)[0])
print(codes)