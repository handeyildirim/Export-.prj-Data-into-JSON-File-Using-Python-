# !/usr/bin/python

import os
import re
import stat
import time

file_content = '{\n    "testcases":\n    [\n%s    ]\n}'
test_entries = ''
file_path = os.path.join(os.getcwd(), "../json/testcases_scc_full.json")
timeout_close = 10

os.chdir("../conny")
rp_tests = re.compile(r"\S+[G|S]\d\d\d\d.*\.pkg$")
num_tests = 0
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if rp_tests.search(name):
            num_tests += 1
            test_entries += '	    {"name": "%s", "label": ""},\n' % (os.path.join(root, name).replace("\\", "/"))
            print(os.path.join(root, name))

file_content = file_content % test_entries

os.chmod(file_path, stat.S_IWOTH | stat.S_IRWXU)

fh = open(file_path, 'w')
fh.write(file_content)
fh.close()

print("==============================\nNumber of tests found: %d" % num_tests)
print("Exported JSON to: %s" % file_path)
print("Window will close in %d seconds...\n==============================" % timeout_close)
time.sleep(timeout_close)

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
