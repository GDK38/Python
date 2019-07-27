#!/usr/bin/python3.7
import requests #1 импортирую бибилиотеку, так как она будет отвечать за отправку запросов
from bs4 import BeautifulSoup
import os #26 отвечает за взаимодействие с ОС
def get_html(): #6 создаем фугкцию которая отправляет запрос
	url='http://www.cbr.ru/'
	r=requests.get(url) #8 делаем запрос на сервер
	return r.text #9 функция возвращает свойство text, уоторая содержит информацию об html
def get_dollar_rate(html): 
	soup = BeatifulSoup(html, 'lxml')
	# t = soup.find('ins', text='$') #13 ищем ins в теге tr 
	# t = soup.find('ins', text='$').find_parent('tr') #17 обратимся к его родительскому контейнеру tr
 	t = soup.find('ins', text='$').find_parent('tr').find_all('td')[-1].text #19 получим тег tr
	result=t.split('>')[-1] #21 указываем до какого числа нуно пропустить инфу (>) и какой элемент нам нужен (-1)
 	return result #23 получим число курс
def send_message(message): #24 хотим выводить это число на экран
 	title='dollar SHA:'
	#26 os.system('notify-send "title" "message"')
	os.system('notify-send "{}" "{}"'.format(title, message)) 
def main():
 	rate=get_dollar_rate(get_html()) #27 получаем курс доллара
 	send_message(rate)
if __name__ == '__main__':
	main()
