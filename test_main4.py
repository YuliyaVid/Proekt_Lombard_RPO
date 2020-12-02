import pytest
from PyQt5    import  QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton
import main
@pytest.fixture
def app(qtbot):
	test_app = main.Worker_app('name')
	qtbot.addWidget(test_app)

	return test_app

def test_close_app(app, qtbot):
	with pytest.raises(SystemExit):
		app.exit_app()


