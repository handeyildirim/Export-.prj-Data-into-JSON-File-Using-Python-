# !/usr/bin/python

import os.path
import re
from pathlib import Path
import time

timeout_close = 10


def get_required_contents_for_json_file(contents: str) -> str:
    data = re.findall('<PACKAGE-PATH xsi:type="string">(.+)</PACKAGE-PATH>', contents)
    output_entries = ''
    file_content = '{\n    "testcases":\n    [\n%s    ]\n}'
    rp_tests = re.compile(r"\S+[G|S]\d\d\d\d.*\.pkg$")
    num_labels = 0
    for label in data:
        if rp_tests.search(label):
            num_labels += 1
            output_entries += '	    {"name": "%s", "label": ""},\n' % label.replace("\\", "/")
    file_content = file_content % output_entries
    # print(file_content)
    print("==============================\nNumber of labels found: %d" % num_labels)
    return file_content


def export_data_into_json_file(out_file_path: str, file_content: str):
    file = open(out_file_path, 'w')
    file.write(file_content)
    print("Exported JSON to: %s" % out_file_path)
    file.close()
    print("Window will close in %d seconds...\n==============================" % timeout_close)
    time.sleep(timeout_close)


def create_json_file_for_outputs(out_file_path: str):
    print("Creating json file...")
    open(out_file_path, 'w')
    print("JSON file was created to: %s " % out_file_path)


def create_folder_for_outputs(out_dir_path: str):
    print("Creating directory...")
    Path(out_dir_path).mkdir(parents=True, exist_ok=True)
    print("Directory was created to: %s " % out_dir_path)


def create_an_output_file(output_dir: str, out_file_name: str) -> str:
    out_dir_path = os.path.join(os.getcwd(), output_dir)
    out_file_path = out_dir_path + out_file_name
    if not os.path.exists(out_dir_path):
        create_folder_for_outputs(out_dir_path)
        create_json_file_for_outputs(out_file_path)
    else:
        if not os.path.exists(out_file_path):
            create_json_file_for_outputs(out_file_path)
    return out_file_path


def get_inputs_from_prj_file(input_file_name: str):
    if os.path.exists(input_file_name):
        with open(input_file_name, 'r', encoding='utf-8-sig') as f:
            inputs = f.read()
            return inputs


def convert_prj_to_json(input_file: str, output_dir: str, output_file: str):
    """

    :param input_file: Name of the input file
    :param output_dir: Path of the directory which contains output file
    :param output_file: Name of the output file
    :return:
    """
    inputs = get_inputs_from_prj_file(input_file)
    out_file_path = create_an_output_file(output_dir, output_file)
    contents = get_required_contents_for_json_file(inputs)
    export_data_into_json_file(out_file_path, contents)


if __name__ == '__main__':
    convert_prj_to_json("conti_scal.prj", "json\\", "testcases_scc_full.json")
