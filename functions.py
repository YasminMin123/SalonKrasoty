import json
import re

with open('raspisanie.json') as f: # Открытие файла
	data_json = json.load(f) # Получаем данные из файла

with open('fio_info.json') as f: # Открытие файла
	data_json2 = json.load(f) # Получаем данные из файла

with open('spisok_proc_with_fam.json') as f: # Открытие файла
	data_json3 = json.load(f) # Получаем данные из файла

def show_history_of_visiting():
	with open('history_of_visiting.txt', 'r') as f_in:
		lines = list(line for line in (l.strip() for l in f_in) if line)
		return '\n'.join(lines)


def show_last_date():
	f_read = open("history_of_visiting.txt", "r")
	last_line = f_read.readlines()[-1]
	return last_line.split(':')[0]


def show_history_of_paying(name):
	f_read = open("Anna-paid_procedures.txt",'r').name
	if name in f_read:
		with open('Anna-paid_procedures.txt', 'r') as f_in:
			data = list(line for line in (l.strip() for l in f_in) if line)
			res = '\n'.join(data)
		return f"Процедуры оплаченные пользователем {name}:\n{res}"
	else:
		return 'Данных для такого пользователя не найдено!'

sp = []
def show_raspisanie():
	for x in data_json.items():
		print(x[0] + '   :  ' + x[1])


sp1 = []
def show_about_me():
	kto = input()
	if kto in data_json2.keys():
		for i in data_json2[kto].keys():
			sp1.append(data_json2[kto].get(i))
		return ' : '.join(sp1)
	else:
		return 'Not found!'


#--------------------------#
l =[]
def get_proc():
	for i in data_json3.items():
		l.append(','.join(i[1]))
		print(i[0]+':: '+''.join(l))

def find_visiter():
	who = input()
	with open("visiters.txt","r") as fin:
		for s in fin.readlines():
			if s.find(who) > -1:
				print(s.strip())


def show_proc():
	with open("proc.txt","r") as f_in:
		lines = list(line for line in (l.strip() for l in f_in) if line)
		return '\n'.join(lines)

data_txt1 = {}
count2 = []
def time_proc():
	with open("proc.txt","r") as file:
		for line in file:
			key, value, cena = line.strip().split(':')
			data_txt1[key] = value, cena
	for i in data_txt1.items():
		count2.append(f'\n{i[0]} - {i[1][0]}')
	result = '{}'.format(' '.join(list(count2)))


data_txt2= {}
count2 = []
def buy_proc():	
	with open("proc.txt","r") as file:
		for line in file:
			key, value, cena = line.strip().split(':')
			data_txt2[key] = value, cena
	for i in data_txt2.items():
		count2.append(f'\n{i[0]} - {i[1][1]}')
	result = '{}'.format(' '.join(list(count2)))
	answer = input(f'Что хотите купить?\n{result} => ')
	with open('paid_proc.txt', 'r+') as f:
		f.write(f'{answer.title().replace(" ","")}\n')

data_txt3 = {}
count3 = []
def find_proc():
	proc = input('Что хотите найти? ')
	with open("all_proc.txt","r") as file:
		for s in file.readlines():
			if s.find(proc) > -1:
				print(s.strip())
				for line in file:
					key, cena, kol = line.strip().split(':')
					data_txt3[key] = cena, kol
				for i in data_txt3.items():
					count3.append(f'\n{i[0]} - {i[1][0]} - {i[1][1]}')
				result = '{}'.format(' '.join(list(count3)))
				return result


#-------------#
def show_list_of_visiters():
    with open('list_of_visitors.txt', 'r') as f_in:
        lines = list(line for line in (l.strip() for l in f_in) if line)
        return '\n'.join(lines)

def number_of_visitors():
    with open('list_of_visitors.txt') as f:
        count = sum(1 for line in f if line.strip())
    return count

data_txt4 = {}
count4 = []
def find_client():
	who = input('Пожалуйста наберите имя посетителя: ')
	with open("troubles_of_clients.txt","r") as file:
		for s in file.readlines():
			if s.find(who) > -1:
				print(s.strip())
				for line in file:
					key, diag = line.strip().split(':')
					data_txt4[key] = key, diag
				for i in data_txt4.items():
					count4.append(f'\n{i[0]} - {i[1][0]}')
				result = '{}'.format(' '.join(list(count4)))
				return result