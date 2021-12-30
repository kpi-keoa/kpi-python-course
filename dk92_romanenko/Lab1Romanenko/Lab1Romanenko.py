#!/usr/bin/env python3
import sys
import requests as req

from sys import argv

"""This module created for using KPI API in console, demo version
demonstrate how use functions. All args contributes like console parameters.

Example:
	$ python Lab1Romanenko.py <arg1> <arg2> <arg3> ...
	
Attributes:
	param_dict <dict>: contains	parameters which used for choose 
	words from API's request 	
	
"""

param_dict = {'-s': 'group_url', '-o': 'group_okr', '-t': 'group_type'}


def sel_param(param):
	"""Use for choose key in param_dict
	
	Args:
		param: parameter for comand line 

	Returns:
		Key form dictionary 
	"""
	return param_dict.get(param)


def get_group(group_name="дк-91"):
	"""Use for choose key in param_dict
	
	Args:
		group_name: group_name for request  

	Returns:
		json file whith request 
	"""
	return req.get(f"https://api.rozklad.org.ua/v2/groups/{group_name}").json()


def get_spec_info(group_name, *args):
	"""Use for choose key in param_dict
	
	Args:
		grop_name: group_name for request
		args: unlimited parameter's number  

	Returns:
		dict with key's request 
	"""
	summary = [group_name]
	for i in args:
		summary.append(get_group(group_name).get('data').get(sel_param(i)))
	return summary


def get_key_info(**kwargs):
	"""Use for choose key in param_dict
	
	Args:
		kwagrs: function contains 'name', 'data', 'param'
			- name: group_name for request
			- data: data for request
			- para: key for request 

	Returns:
		dict with key's request 
	"""
	return [
		kwargs['name'],
		get_group(kwargs['name']).get('data').get(sel_param(kwargs['param']))
	]


def get_day_lessons(group_name, lessons_week, /, lessons_day):
	"""Use for choose key in param_dict
	
	Args:
		group_name: group_name for request
		lessons_week: study week of selected group
		lessons_day: study day of selected group

	Returns:
		json file of request 
	"""
	filter_list = {
		'day_number': lessons_day, 'lesson_week': lessons_week
	}
	return req.get(
		f"http://api.rozklad.org.ua/v2/groups/{group_name}/lessons?filter={filter_list}"
	).json()


def print_day_lessons(group_name, *, lessons_week=1, lessons_day=1):
	"""Use for choose key in param_dict
	
	Args:
		group_name: group_name for request
		lessons_week: study week of selected group
		lessons_day: study day of selected group

	Returns:
		none 
	"""
	filter_list = {'day_number': lessons_day, 'lesson_week': lessons_week}
	print(
		req.get(
			f"http://api.rozklad.org.ua/v2/groups/{group_name}/lessons?filter={filter_list}"
		).text
	)


print(get_group())

try:
	print(get_spec_info(argv[1], argv[2], argv[3]))
except Exception as e:
	print(f"(task: get_spec_info): Ooooops! {e}", file=sys.stderr)

try:
	print(get_key_info(name=argv[1], param=argv[3]))	
except Exception as e:
	print(f"(task: get_key_info): {e}", file=sys.stderr)

try:
	print(get_day_lessons(argv[1], argv[2], argv[3]))
except Exception as e:
	print(f"(task: get_day_lessons): Something gona bad! {e}", file=sys.stderr)

try:
	print_day_lessons(group_name=argv[1], lessons_day=argv[3])
except Exception as e:
	print(f"(task: get_key_info): Naaah! {e}", file=sys.stderr)