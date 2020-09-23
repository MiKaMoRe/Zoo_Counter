import sys, pyowm, random, pickle
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from Test import Ui_MainWindow
from Dialog import Ui_Dialog



app = QtWidgets.QApplication(sys.argv)
window = QMainWindow()
window2 = QDialog()

dialog = Ui_Dialog()
dialog.setupUi(window2)

ui = Ui_MainWindow()
ui.setupUi(window)


window.setWindowTitle("Zoo Counter")
window2.setWindowTitle("ATENTION!")
# Есть необходимость установить хотя бы 1 стиль к header в таблице, ибо без этого не работают стили, установленные в qt designer. Хз почему.
ui.tableWidget.horizontalHeader().setStyleSheet("QTableWidget QHeaderView::section{color: #fff;}")
ui.tableWidget.verticalHeader().setStyleSheet("QTableWidget QHeaderView::section{color: #fff;}")
#


# Set table only for read 
ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers);

# variables
zoo = []
tag_list = []
select = 0




#hook logic

# class Animal for create data about animals
class Animal:
	def __init__(self, tag, name, kind, status, place):
		self.tag = tag
		self.name = name
		self.kind = kind
		self.status = status
		self.place = place

# create new animal
def add_member():
	if (ui.input_name.text() == "" or ui.input_kind.text() == "" or ui.input_status.text() == "" or ui.input_place.text() == ""):
		ui.label.setText("Невозможно добавить неполную строку. Пожалуйста, заполните все данные.")
	else:
		ui.label.setText("")
		
		name = ui.input_name.text()
		kind = ui.input_kind.text()
		status = ui.input_status.text()
		place = ui.input_place.text()
		tag = tag_counter(None)
		zoo.append(Animal(tag, name, kind, status, place))
		
		draw_all()

# Fill tabel
def draw_all():
	global zoo

	ui.tableWidget.setRowCount(len(zoo))
	i = 0
	while i < len(zoo):
		ui.tableWidget.setItem(i, 0, QTableWidgetItem(zoo[i].name))
		ui.tableWidget.setItem(i, 1, QTableWidgetItem(zoo[i].kind))
		ui.tableWidget.setItem(i, 2, QTableWidgetItem(zoo[i].status))
		ui.tableWidget.setItem(i, 3, QTableWidgetItem(zoo[i].place))
		ui.tableWidget.verticalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
		i +=1


# Set tags for objects
def tag_counter(tag):
	while tag == None:
		number = []
		randCode = ""
		i = 5
		while i > 0:
			i -=1
			number.append(random.randint(0,9))
		for x in number:
			randCode = randCode + str(x);
		if randCode in tag_list:
			continue
		else:
			tag = "T" + randCode
			tag_list.append(randCode)
			return tag

# Loads, saves and clear
def load_all():
	global zoo
	global tag_list

	zoo = load_obj("animals")
	tag_list = load_obj("tag_list")
	draw_all()

def save_all():
	global zoo
	global tag_list

	save_obj(zoo, "animals")
	save_obj(tag_list, "tag_list")

def save_obj(obj, name ):
	with open('obj/'+ name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
	with open('obj/' + name + '.pkl', 'rb') as f:
		return pickle.load(f)

def clear_all():
	global zoo
	global tag_list
	zoo = []
	tag_list = []
	save_all()
	load_all()
	dialog_close()
	draw_all()

def select_cell(row, column):
	global select
	select = row
	return select

def clear_cell():
	global select
	global zoo

	zoo.pop(select)
	draw_all()



def dialog_open():
	window2.show()
def dialog_close():
	window2.hide()


# buttons main window
ui.add_member_button.clicked.connect(add_member)		# button for add new member
ui.load_button.clicked.connect(load_all)				# button for load data from /obj/.
ui.save_button.clicked.connect(save_all)				# button for save data in /obj/.
ui.clear_all_button.clicked.connect(dialog_open)		# button for click on "Clear Data" 

ui.clearCell.clicked.connect(clear_cell)				# button for delete info in selected row
ui.tableWidget.cellClicked.connect(select_cell)			# tracking selected cell/row.

#buttons dialog window
dialog.accept.clicked.connect(clear_all)				# button "Yes" on click in dialog window 
dialog.reject.clicked.connect(dialog_close)				# button "No" on click in dialog window


# Main loop
window.show()
sys.exit(app.exec_())





