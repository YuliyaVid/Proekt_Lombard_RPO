import pytest
from PyQt5    import  QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton
import sqlite3
import main
conn = sqlite3.connect(r'db/db.db') # подключение к базе данных
cur = conn.cursor() # создание курсора
@pytest.fixture
def app(qtbot):
	test_app = main.Add_c_2(['1', 'Морозов' , 'Олег', 'Константинович', '1975-05-12', '4510', '873534', 'площадь пушкина', '9852648504'])
	qtbot.addWidget(test_app)

	return test_app

def test_lied_texts(app, qtbot):
	test_list = ['1', 'Морозов' , 'Олег', 'Константинович', '1975-05-12', '4510', '873534', 'площадь пушкина', '9852648504']
	assert app.lineEdit.text() == test_list[0]

def test_lied_texts_2(app, qtbot):
	test_list = ['1', 'Морозов' , 'Олег', 'Константинович', '1975-05-12', '4510', '873534', 'площадь пушкина', '9852648504']
	assert app.lineEdit_2.text() == test_list[1]

def test_lied_texts_3(app, qtbot):
	test_list = ['1', 'Морозов' , 'Олег', 'Константинович', '1975-05-12', '4510', '873534', 'площадь пушкина', '9852648504']
	assert app.lineEdit_3.text() == test_list[2]

def test_database(app, qtbot):
	test_list = ['1', 'Морозов' , 'Олег', 'Константинович', '1975-05-12', '4510', '873534', 'площадь пушкина', '9852648504']
	qtbot.mouseClick(app.Add_client_f, QtCore.Qt.LeftButton)
	cur.execute("SELECT * from clients where id= 1")
	full_info_of_c = cur.fetchone()
	assert full_info_of_c[1] == test_list[1]
	assert full_info_of_c[2] == test_list[2]



