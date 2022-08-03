# !/usr/bin/python

import os.path
from pathlib import Path

in_file = "conti_scal.prj"

out_dir = os.path.join(os.getcwd(), ".\json\\")
out_file = "testcases_scc_full.json"
out_file_path = out_dir + out_file

if os.path.exists(in_file):
    conti_scal = open(out_file_path, 'r')
    print(conti_scal)

if not os.path.exists(out_dir):
    print("Creating directory...")
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    print("Creating json file...")
    testcases_scc_full = open(out_file_path, 'w')
else:
    if not os.path.exists(out_file_path):
        print("Creating json file...")
        testcases_scc_full = open(out_file_path, 'w')
