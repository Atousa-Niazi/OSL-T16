#Atousa Niazi Abkoh - 98440127 - python - OSLab - contact
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *
import sqlite3
import qdarkstyle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        loader = QUiLoader()
        self.ui = loader.load("design.ui")
        self.ui.show()
        

        self.ui.btn_create.clicked.connect(self.creat)
        self.ui.btn_reload.clicked.connect(self.reload)
        self.ui.btn_del.clicked.connect(self.delete)
        self.ui.btn_delall.clicked.connect(self.delete_all)
        self.ui.btn_theme.clicked.connect(self.theme)

        
        self.conn = sqlite3.connect("contact.db")
        self.my_cursor = self.conn.cursor()
        self.load_data()

    def load_data(self):
        self.my_cursor.execute("select * from person")
        result = self.my_cursor.fetchall()

        for item in result:
            label = QLabel()
            try:
                label.setText(item[1] + " " + item[2] + ": " + item[4])
            except:
                label.setText(item[1] + ": " + item [4])
            self.ui.verticalLayout.addWidget(label)

        self.ui.message.setText("data loaded successfuly!")

    def reload(self):
        for i in reversed(range(self.ui.verticalLayout.count())): 
            self.ui.verticalLayout.itemAt(i).widget().setParent(None)
        self.load_data()

    def creat(self):
        self.my_cursor.execute("INSERT INTO Person (name,family,mobile_number,phone_number,email)VALUES (?,?,?,?,?)",(self.ui.btn_name.text(),self.ui.btn_L_name.text(),self.ui.btn_p_number.text(),self.ui.btn_m_number.text(),self.ui.btn_email.text(),))
        self.conn.commit()
        self.ui.message.setText("add successfuly!")
        self.ui.btn_name.setText("")
        self.ui.btn_L_name.setText("")
        self.ui.btn_p_number.setText("")
        self.ui.btn_m_number.setText("")
        self.ui.btn_email.setText("")

    def delete(self):
        self.ui.message.setText("type in name boxe to find a special record.")
        self.my_cursor.execute("DELETE FROM Person WHERE name = ?",(self.ui.btn_name.text(),))
        self.conn.commit()   
        self.ui.btn_name.setText("")
        self.ui.message.setText("delete successfuly!")

    def delete_all(self):
        self.my_cursor.execute("DELETE FROM Person;",)
        self.ui.message.setText("delete all ",self.my_cursor.rowcount, " rows successfuly!")
        
    def theme(self):
        #i also tried  https://material.io/resources/color/#!/?view.left=0&view.right=0&secondary.color=7B1FA2&secondary.text.color=FAFAFA&primary.color=7B1FA2 ,  QDarkStyle and  https://pypi.org/project/qt-material/ but they didnt turn out well so i see this in youtube 
        app.setStyleSheet(qdarkstyle.load_stylesheet())
        self.ui.message.setText("please read code for more information")
        # i wasnt able to chang text color after theme changing 
        # i found other ways to have color theme but none were for pyside6 and i didnt want to use pyside2 oy pyqt5-4 
        # i make a colore xml but the text color wasnt satisfying to use  

app = QApplication()
main_window = MainWindow()
app.exec()