1) хочу чтобы на рабочем столе периодично отображались курсы доллара. заходим в центральный банк  смотрим курс валют, просмотрим тег. зацепимся именно за знак доллара, он один на этой странице. у него тег ins, и цепляюсь за него, потом есть родительский тег tr и забираю последний элемент td

2) создаем файл-script ruble.py:

29)#!/usr/bin/python3
1) импортирую бибилиотеку, так как она будет отвечать за отправку запросов
1) import requests
11) from bs4 import BeautifulSoup
26) отвечает за взаимодействие с ОС
26) import os
6) создаем фугкцию которая отправляет запрос
6) def get_html():
7)	url='http://www.cbr.ru/'
8) delaem zapros na server
8)	r=requests.get(url)
9) функция возвращает свойство text, уоторая содержит информацию об html
9)	return r.text
10) def get_dollar_rate(html):
12)	soup = BeatifulSoup(html, 'lxml')
13) ищем ins в теге tr
#13)	t = soup.find('ins', text='$')
17) обратимся к его родительскому контейнеру tr
#17) 	t = soup.find('ins', text='$').find_parent('tr')
18) получем тег tr
19) 	t = soup.find('ins', text='$').find_parent('tr').find_all('td')[-1].text
20) получим текст элемента
#14) 	print(t)
21) указываем до какого числа нуно пропустить инфу (>) и какой элемент нам нужен (-1)
21) 	result=t.split('>')[-1]
#22)	print(result)
22) получи число курс
23) 	return result
24) хотим выводить это число на экран
24)def send_message(message):
25) 	title='dollar SHA:'
#26)	os.system('notify-send "title" "message"')
26)	os.system('notify-send "{}" "{}"'.format(title, message))
4)def main():
#5)	pass
15) в качестве аргумента выдаю результаты getсh_tml
#15) 	get_dollar_rate(get_html())
27) поулчаем курс доллара
27) 	rate=get_dollar_rate(get_html())
28) 	send_message(rate)
16) сохраняем и запускаем скрипт, выведет <ins>$</ins>
2) if __name__ == '__main__':
3)	main()

3) смотрим какие права есть у нашего файла
david@VirtualBox:~$ ls -l

4) ВИДИМ ЧТО ПРАВА ТОЛЬко на чтение из запись
david@VirtualBox:~$ chmod a+x ruble.py
david@VirtualBox:~$ ls -l

5) теперь у всех есть права на исполнение
crontav -e
* * * * * export DISPLAY=:0 && cd /home/david/Destop && ./ruble.py

6) отображается окно
