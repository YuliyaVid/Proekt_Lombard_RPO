import pytest
from PyQt5    import  QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton
import sqlite3
import main
conn = sqlite3.connect(r'db/db.db') # подключение к базе данных
cur = conn.cursor() # создание курсора
@pytest.fixture
def app(qtbot):
	test_app = main.Client_add()
	qtbot.addWidget(test_app)

	return test_app

def test_data_base(app, qtbot):
	test_list = ['Морозов' , 'Олег', 'Константинович', '1975-05-12', '4510', '873534', 'площадь пушкина', '9852648504']
	app.lineEdit_2.setText(test_list[0]) 
	app.lineEdit_3.setText(test_list[1]) 
	app.lineEdit_4.setText(test_list[2]) 
	app.lineEdit_5.setText(test_list[3]) 
	app.lineEdit_6.setText(test_list[4]) 
	app.lineEdit_7.setText(test_list[5]) 
	app.lineEdit_8.setText(test_list[6]) 
	app.lineEdit_8.setText(test_list[7]) 
	qtbot.mouseClick(app.Add_client_f, QtCore.Qt.LeftButton)

	cur.execute('SELECT id FROM workers')
	c_id = len(cur.fetchall())+1
	cur.execute(f"SELECT * from clients where id= {c_id}")
	full_info_of_c = cur.fetchone()
	assert full_info_of_c[1] == test_list[0] # здесь сравниваем разные индексы так как функционал программы
	assert full_info_of_c[2] == test_list[1] # предусматривает предустановленный самой программой ID

	assert app.close() == True # проверяем закрылась ли программа

	




'''
Данный тест проверяет корректность ввода данных в базу! с помощью функции программы 
Добавить клиента
'''