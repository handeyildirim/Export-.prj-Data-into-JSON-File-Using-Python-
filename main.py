# !/usr/bin/python

import os.path
import re
from pathlib import Path

file_data = {}


def check_input_file():
    in_file = "conti_scal.prj"
    if os.path.exists(in_file):
        conti_scal = open(in_file, 'r')
        print(conti_scal)


def create_a_json_file_for_outputs(out_file_path):
    print("Creating json file...")
    testcases_scc_full = open(out_file_path, 'w')


def create_a_folder_for_output_files(out_dir):
    print("Creating directory...")
    Path(out_dir).mkdir(parents=True, exist_ok=True)


def check_output_file():
    check_input_file()
    out_dir = os.path.join(os.getcwd(), ".\json\\")
    out_file = "testcases_scc_full.json"
    out_file_path = out_dir + out_file
    if not os.path.exists(out_dir):
        create_a_folder_for_output_files(out_dir)
        create_a_json_file_for_outputs(out_file_path)
    else:
        if not os.path.exists(out_file_path):
            create_a_json_file_for_outputs(out_file_path)


check_output_file()
