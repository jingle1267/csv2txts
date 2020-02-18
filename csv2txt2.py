#! /usr/bin/env python3
# coding=utf-8
import os
import sys

import ExtractFromCsv

file_counter = 0
output_dir = 'output'
csv_file_name = ''
output_file_tail = 'txt'


# 第一个参数是csv 文件的名称
# 第二个参数是抽去的数据的名称的表头
# 第三个参数是抽取的数据的数据字段的表头
def process(args):
	print('开始执行')
	global file_counter
	global output_dir
	global csv_file_name
	global output_file_tail
	file_counter = 0
	args_len = len(args)
	if args_len < 2:
		print('Missing parameters! Please read readme first, and follow the guide.')
		return

	csv_file_name = args[1]

	if args_len >= 3:
		title_name = args[2]
	else:
		title_name = 'name'

	if args_len >= 4:
		content_name = args[3]
	else:
		content_name = 'content'

	if args_len >= 5:
		output_dir = args[4]

	if args_len >= 6:
		output_file_tail = args[5]

	print('Source file name:\'{0}\' , extract columns : \'{1}\' \'{2}\' , output folder name : \'{3}\''
				.format(csv_file_name, title_name, content_name, output_dir))

	ExtractFromCsv.process(csv_file_name, title_name, content_name, csv_row_callback)
	print_str = "共生成 %d 个文件" % file_counter
	print("\033[0;32m%s\033[0m" % print_str)


def csv_row_callback(file_name, file_content):
	global file_counter
	file_counter += 1

	txt_dir = generate_dir()

	category = pinyin2hanzi(csv_file_name.replace('./test/zgjm-', '').replace('.csv', ''))

	# file_txt_content = ('title: {0}\n'.format(file_name) + 'date: 2020-02-13 17:58:22\n' + 'tags: {0}\n'.format(category)
	# 										+ 'categories: {0}\n'.format(category)
	# 										+ '---\n\n' + file_content)

	file_txt_content = ('---\ntitle: {0}\n'.format(file_name) + 'date: 2020-02-15T20:54:12+08:00\n'
											+ 'draft: false\n'
											+ '---\n\n' + file_content)

	print('txt_dir:{0}, file_name:{1}'.format(txt_dir, file_name))

	with open('{0}/{1}.{2}'.format(txt_dir, file_name, output_file_tail), 'w') as f:
		f.write(file_txt_content)


def pinyin2hanzi(pinyin_category):
	if pinyin_category == 'dongwu':
		return '动物'
	elif pinyin_category == 'guishen':
		return '鬼神'
	elif pinyin_category == 'jianzhu':
		return '建筑'
	elif pinyin_category == 'qinggan':
		return '情感'
	elif pinyin_category == 'renwu':
		return '任务'
	elif pinyin_category == 'shenghuo':
		return '生活'
	elif pinyin_category == 'shenti':
		return '身体'
	elif pinyin_category == 'wupin':
		return '物品'
	elif pinyin_category == 'yunfu':
		return '孕妇'
	elif pinyin_category == 'zhiwu':
		return '植物'
	elif pinyin_category == 'ziran':
		return '自然'
	else:
		return pinyin_category


def generate_dir():
	base = os.path.basename(csv_file_name)
	target_dir = os.path.splitext(base)[0]

	output_dir.replace('zgjm-', '')

	target_dir = output_dir + "/" + target_dir

	print('target_dir = ' + target_dir)

	if not os.path.exists(target_dir):
		os.makedirs(target_dir)

	return target_dir


if __name__ == '__main__':
	# print('start ： ' + os.path.abspath('.'))
	process(sys.argv)

# process(sys.argv)
