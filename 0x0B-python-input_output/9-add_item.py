#!/usr/bin/python3
""" adds all arguments to a list, and then save them to a file """
import sys
import os
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = 'add_item.json'

if os.path.isfile(filename):
    argument_list = load_from_json_file(filename)
else:
    argument_list = []

for argument in range(1, len(sys.argv)):
    argument_list.append(sys.argv[argument])

save_to_json_file(argument_list, filename)
