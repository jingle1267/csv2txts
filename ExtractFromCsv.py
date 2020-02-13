#! /usr/bin/env python3
# coding=utf-8

import csv


def get_file_and_content(row, title, content, callback):
	file_name = row[title]
	content = row[content]
	if content == "null" or content == "":
		return
	callback(file_name, content)


def extract_csv_data(filename, title, content, callback):
	# print("importing data from %s" % filename)

	# check whether csv file has utf-8 bom char at the beginning
	skip_utf8_seek = 0
	with open(filename, "rb") as csv_file:
		csv_start = csv_file.read(3)
		if csv_start == b'\xef\xbb\xbf':
			skip_utf8_seek = 3

	with open(filename, "rU") as csv_file:

		# remove ut-8 bon sig
		csv_file.seek(skip_utf8_seek)

		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			get_file_and_content(row, title, content, callback)


def process(file_name, title, content, callback):
	extract_csv_data(file_name, title, content, callback)

# def process(args):
#     # filename passde through args
#     if len(args) >= 2:
#         csv_filename = args[1]
#         extract_csv_data(csv_filename, 'title', 'indexcontent')
#         logging.info("image download completed")
#
#     else:
#         logging.warning("no input file found")
#
#     time.sleep(10)

# process(sys.argv)
