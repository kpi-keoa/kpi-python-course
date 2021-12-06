#!/usr/bin/env python3

import requests as req 
from sys import argv

param_dict = {'-s': 'group_url', '-o': 'group_okr', '-t': 'group_type'}

def sel_param(param):
	return param_dict.get(param)

def get_group(group_name="дк-81"):
	return req.get(f"https://api.rozklad.org.ua/v2/groups/{group_name}").json()

def get_spec_info(group_name, *args):
	summary = [group_name]
	for i in args:
		summary.append(get_group(group_name).get('data').get(sel_param(i)))
	return summary

def get_key_info(**kwargs):
	return [kwargs['name'], get_group(kwargs['name']).get('data').get(sel_param(kwargs['param']))]

def get_day_lessons(group_name, lessons_week, /, lessons_day):
	filter_list = {'day_number': lessons_day, 'lesson_week': lessons_week}
	return req.get(f"http://api.rozklad.org.ua/v2/groups/{group_name}/lessons?filter={filter_list}").json()

def print_day_lessons(group_name, lessons_week=1, *, lessons_day=1):
	filter_list = {'day_number': lessons_day, 'lesson_week': lessons_week}
	print(req.get(f"http://api.rozklad.org.ua/v2/groups/{group_name}/lessons?filter={filter_list}").text)

#print(get_group())

print(get_spec_info(argv[1], argv[2], argv[3]))
print(get_key_info(name=argv[1], param=argv[3]))	
print(get_day_lessons(argv[1], argv[2], argv[3]))
print_day_lessons(argv[1], argv[3], lessons_day=argv[2])