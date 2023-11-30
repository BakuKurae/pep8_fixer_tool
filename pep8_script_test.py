import pycodestyle
import re
from io import StringIO
import sys

old_stdout = sys.stdout
sys.stdout = stdout_data = StringIO()

file_checker = pycodestyle.Checker('test.py', show_source=False)
file_errors = file_checker.check_all()
sys.stdout = old_stdout
print("Found %s errors (and warnings)" % file_errors)
codes = []
for code in stdout_data.getvalue().split("\n")[:-1]:
    codes.append(re.findall("(?<=: )(.{4})", code)[0])
print(codes)