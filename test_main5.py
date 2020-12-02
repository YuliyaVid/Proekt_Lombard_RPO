import pytest
from PyQt5    import  QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton
import main
@pytest.fixture
def app(qtbot):
	test_app = main.Worker_app('name')
	qtbot.addWidget(test_app)

	return test_app

def test_open_next_window(app, qtbot):
	app.Add_client_click()
	assert app.next1.show() == None
	assert app.next1.close() == True

	# почему None  ? потому что запуск окна не имеет булевого состояния
	# как ни странно тот же close() можно проверить True / False
	# если бы окно не открылось тест выдал бы ошибку о том что у класса Worker_app нет
	# также то что окно открывалось нам свидетельствует app.next1.close() == True который проходит тест


