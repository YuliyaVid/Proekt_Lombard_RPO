import pytest
from PyQt5    import  QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton

import main

@pytest.fixture
def app(qtbot):
	test_app = main.Login_app()
	qtbot.addWidget(test_app)

	return test_app
# данные 2 теста нужны чтобы проверить работу системы
def test_label(app):   
	assert app.label.text() == 'Логин' # этот тест должна пройти программа

def test_label2(app):
	assert app.label.text() == 'Лоин' 
'''
Этот тест должен выдать ошибку 

E    AssertionError: assert 'Логин' == 'Лоин'
E      - Лоин
E      + Логин
E      ?   +

'''

def test_label_after_wrong_login(app, qtbot):
	qtbot.mouseClick(app.Login_button, QtCore.Qt.LeftButton)
	assert app.label_3.text() == 'Попытка 1 из 3'
	qtbot.mouseClick(app.Login_button, QtCore.Qt.LeftButton)
	assert app.label_3.text() == 'Попытка 3 из 3'  # этот тест тоже вызвали чтобы сделать ошибку
	'''
	Данный тест необходим для проверки работы счетчика 

	'''




