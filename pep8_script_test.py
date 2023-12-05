import pycodestyle
import re
from io import StringIO
import sys
import autopep8
import unittest

# old_stdout = sys.stdout
# sys.stdout = stdout_data = StringIO()

# file_checker = pycodestyle.Checker('test.py', show_source=False)
# file_errors = file_checker.check_all()
# sys.stdout = old_stdout
# print("Found %s errors (and warnings)" % file_errors)
# codes = []
# for code in stdout_data.getvalue().split("\n")[:-1]:
#     codes.append(re.findall("(?<=: )(.{4})", code)[0])
# print(codes)
# Fixer
file_data = open("OLD_pep8_fixer_tool.py", "r")
data = file_data.read()
opt = autopep8.parse_args(['--ignore', 'E111'])
print("pre-process")
fixed_data = autopep8.fix_code(data, options={'ignore': ['E']})
print("test")
prefix = "fixed_"
fixed_file = open(f"{prefix}test.py", "w")
fixed_file.write(fixed_data)
fixed_file.close()