from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox

import sqlite3
import datetime

# create or connect to a database
# database baglantisi
conn = sqlite3.connect("takvim.db")
# create a cursor
# imlec olusturuldu
c = conn.cursor()
# create a table
# tablolar olusturuldu
conn.execute('''CREATE TABLE if not exists TAKVIM (DATE DATE,ICERIK TEXT PRIMARY KEY NOT NULL )''')
c.execute("""CREATE TABLE if not exists todo_list( list_item text )""")
c.execute("""CREATE TABLE if not exists book_list( list_item text )""")
c.execute("""CREATE TABLE if not exists shopping_list( list_item text )""")
c.execute("""CREATE TABLE if not exists travel_list( list_item text )""")
# commit(save) the changes
# degisiklikler kaydedildi
conn.commit()
# close the connection
# database baglantisi kapatildi
conn.close()

class CalendarListApp(QMainWindow):
    global rowCount
    rowCount = 0

    def __init__(self):
        super().__init__()
        # loading ui
        # ui baglantisi
        loadUi("CalendarListApp.ui", self)

        # grab all the items from the db
        # databaseden verilerin alinmasi icin fonksiyonlar
        self.graball()
        self.grab_all()
        self.grab_all2()
        self.grab_all3()
        self.grab_all4()

    # grabbing the items from calendar list
    # takvim listesinden verileri alan fonksiyon
    def graball(self):
        conn = sqlite3.connect("takvim.db")
        cursor = conn.execute("SELECT DATE,ICERIK from TAKVIM")
        #imlecin her satirda gezmesini saglayan dongu
        for row in cursor:
                    # creating rows in tablewidget
                    # tablewidgetta satir olusturuldu
                    rowCount = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowCount)
                    #databaseden donen tuple stringe cevrildi
                    str = ''.join(row)
                    str2 = ''.join(row[1])
                    # veriler tablewidgeta eklendi
                    self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(str))
                    self.tableWidget.setItem(rowCount, 1, QTableWidgetItem(str2))
        conn.commit()
        conn.close()

    # grabbing the items from todo list
    # todo listesinden verileri alan fonksiyon
    def grab_all(self):
        conn = sqlite3.connect("takvim.db")
        c = conn.cursor()
        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()
        conn.commit()
        conn.close()
        # loop to get items from db to screen
        # dbden verileri alan dongu
        for record in records:
            self.listWidget.addItem(str(record[0]))

    # grabbing the items from book list
    # book listesinden verileri alan fonksiyon
    def grab_all2(self):
        conn = sqlite3.connect("takvim.db")
        c = conn.cursor()
        c.execute("SELECT * FROM book_list")
        records = c.fetchall()
        conn.commit()
        conn.close()
        for record in records:
            self.listWidget_2.addItem(str(record[0]))

    # grabbing the items from shopping list
    # shopping listesinden verileri alan fonksiyon
    def grab_all3(self):
        conn = sqlite3.connect("takvim.db")
        c = conn.cursor()
        c.execute("SELECT * FROM shopping_list")
        records = c.fetchall()
        conn.commit()
        conn.close()
        for record in records:
            self.listWidget_3.addItem(str(record[0]))

    # grabbing the items from travel list
    # travel listesinden verileri alan fonksiyon
    def grab_all4(self):
        conn = sqlite3.connect("takvim.db")
        c = conn.cursor()
        c.execute("SELECT * FROM travel_list")
        records = c.fetchall()
        conn.commit()
        conn.close()
        for record in records:
            self.listWidget_4.addItem(str(record[0]))

        # tool button icons
        # menunun buton simgeleri
        self.action_calendar.setIcon(QIcon("vectors/calendarVector.png"))
        self.actionWork_List.setIcon(QIcon("vectors/suitcase.png"))
        self.actionBook_List.setIcon(QIcon("vectors/bookIcon.png"))
        self.actionShopping_List.setIcon(QIcon("vectors/shoppingBag.png"))
        self.actionTravel_List.setIcon(QIcon("vectors/travel.png"))

        self.tableWidget.setColumnWidth(0,130)
        self.tableWidget.setColumnWidth(1,320)
    #------------------------------------
        # sayfalarin indexleri
        self.calendarPage_index = 0
        self.workPage_index = 1
        self.bookPage_index = 2
        self.shoppingPage_index = 3
        self.travelPage_index = 4

        # menu butonlari fonksiyonlara baglandi
        self.action_calendar.triggered.connect(self.go_calendarPage)
        self.actionWork_List.triggered.connect(self.go_workPage)
        self.actionBook_List.triggered.connect(self.go_bookPage)
        self.actionShopping_List.triggered.connect(self.go_shoppingPage)
        self.actionTravel_List.triggered.connect(self.go_travelPage)

        self.go_calendarPage()
    #------------------------------------------------------
        self.calendarWidget.selectionChanged.connect(self.grabDate_add)

        self.saveBtn1.clicked.connect(self.saveitem)
        self.clearBtn1.clicked.connect(self.clear)

        self.addBtn.clicked.connect(self.add_item)
        self.saveBtn.clicked.connect(self.save_item)
        self.deleteBtn.clicked.connect(self.delete_item)
        self.clearBtn.clicked.connect(self.clear_list)

        self.addBtn_2.clicked.connect(self.add_item2)
        self.saveBtn_2.clicked.connect(self.save_item2)
        self.deleteBtn_2.clicked.connect(self.delete_item2)
        self.clearBtn_2.clicked.connect(self.clear_list2)

        self.addBtn_3.clicked.connect(self.add_item3)
        self.saveBtn_3.clicked.connect(self.save_item3)
        self.deleteBtn_3.clicked.connect(self.delete_item3)
        self.clearBtn_3.clicked.connect(self.clear_list3)

        self.addBtn_4.clicked.connect(self.add_item4)
        self.saveBtn_4.clicked.connect(self.save_item4)
        self.deleteBtn_4.clicked.connect(self.delete_item4)
        self.clearBtn_4.clicked.connect(self.clear_list4)

        # ------------------------------------------------------------
    # functions to connect the correct pages
    # butonlara basildiginda gerekli sayfalara gidilmesini saglayan fonksiyonlar
    def go_calendarPage(self):
        self.stackedWidget.setCurrentIndex(self.calendarPage_index)

    def go_workPage(self):
        self.stackedWidget.setCurrentIndex(self.workPage_index)

    def go_bookPage(self):
        self.stackedWidget.setCurrentIndex(self.bookPage_index)

    def go_shoppingPage(self):
        self.stackedWidget.setCurrentIndex(self.shoppingPage_index)

    def go_travelPage(self):
        self.stackedWidget.setCurrentIndex(self.travelPage_index)

    #-----------------------------------------------------

    # function which adds selected date on calendar to the table
    # takvimde farklı bir gun secildiginde secilen gunun tabloya eklenmesini saglayan fonk
    def grabDate_add(self):
        dateSelected = self.calendarWidget.selectedDate()
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        self.tableWidget.setItem( rowCount , 0, QTableWidgetItem(str(dateSelected.toString())) )

    def saveitem(self):
        conn = sqlite3.connect("takvim.db")
        clicked = self.tableWidget.currentRow()
        dateSelected = self.calendarWidget.selectedDate()
        item = self.lineEdit.text()
        self.tableWidget.setItem(clicked, 1, QTableWidgetItem(item))
        conn.execute("INSERT INTO TAKVIM (DATE,ICERIK) VALUES (?, ?)", (dateSelected.toString(), self.lineEdit.text()))
        conn.commit()
        conn.close()

        message = QMessageBox()
        message.setWindowTitle("Saved")
        message.setText("Your list has been saved.")
        message.setIcon(QMessageBox.Information)
        m = message.exec_()

    # function to clear the calendar list
    # takvim listesini bosaltan fonk
    def clear(self):
        rowCount = self.tableWidget.rowCount()
        print(rowCount)
        for i in range(rowCount+1,-1,-1):
            print(i)
            self.tableWidget.removeRow(i)
        conn = sqlite3.connect("takvim.db")
        sql = 'DELETE FROM TAKVIM'
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()

# todo list functions
# todo listesine ait fonksyonlar

    # adding items to the list
    # listeye ekleme
    def add_item(self):
        # input alimi
        item = self.inputBox.text()
        # input ekleniyor
        self.listWidget.addItem("-" + item)
        # input box temizleniyor
        self.inputBox.setText("")

    # function which saves the list
    # degisiklikleri kaydeden butonun fonksiyonu
    def save_item(self):
        conn = sqlite3.connect("takvim.db")
        c = conn.cursor()
        # the list is going to be rewritten so we're clearing it
        # liste bastan tekrar yazilacagindan bosaltiliyor
        c.execute("DELETE FROM todo_list;",)

        # creating an empty list to hold items
        # itemleri tutacak bos bir liste olusturuluyor
        items = []

        # items on table are appending to the items list
        # items listesine tablodaki veriler ekleniyor
        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index))

        # adding the items in items to database
        # itemsdaki tum veriler databasee ekleniyor
        for item in items:
            c.execute("INSERT INTO todo_list VALUES (:item)",
                      {
                          'item': item.text(),
                      })
        conn.commit()
        conn.close()

        # messagebox to show user that list has been saved
        # degisikliklerin kaydedildiğini belirten messagebox
        message = QMessageBox()
        message.setWindowTitle("Saved")
        message.setText("Your list has been saved.")
        message.setIcon(QMessageBox.Information)
        m = message.exec_()

    # func which clears the selected item
    # secilen itemi silen fonk
    def delete_item(self):
        # selecting the item
        #item secimi
        clicked = self.listWidget.currentRow()
        # deleting the item
        #secilen item siliniyor
        self.listWidget.takeItem(clicked)

    # function which clears the whole list
    # tum listeyi temizleyen fonk
    def clear_list(self):
        self.listWidget.clear()

# book list functions
# book listesine ait fonksiyonlar

    def add_item2(self):
        item = self.inputBox_2.text()
        self.listWidget_2.addItem("-" + item)
        self.inputBox_2.setText("")

    def save_item2(self):
        conn = sqlite3.connect("takvim.db")
        c = conn.cursor()
        c.execute("DELETE FROM book_list;",)
        items = []
        for index in range(self.listWidget_2.count()):
            items.append(self.listWidget_2.item(index))

        for item in items:
            c.execute("INSERT INTO book_list VALUES (:item)",
                      {
                          'item': item.text(),
                      })
        conn.commit()
        conn.close()

        message = QMessageBox()
        message.setWindowTitle("Saved")
        message.setText("Your list has been saved.")
        message.setIcon(QMessageBox.Information)
        m = message.exec_()

    def delete_item2(self):
        clicked = self.listWidget_2.currentRow()
        self.listWidget_2.takeItem(clicked)

    def clear_list2(self):
        self.listWidget_2.clear()

# shopping list functions
# shopping listesine ait fonksiyonlar
    def add_item3(self):
        item = self.inputBox_3.text()
        self.listWidget_3.addItem("-" + item)
        self.inputBox_3.setText("")

    def save_item3(self):
        conn = sqlite3.connect("takvim.db")
        c = conn.cursor()
        c.execute("DELETE FROM shopping_list;",)
        items = []
        for index in range(self.listWidget_3.count()):
            items.append(self.listWidget_3.item(index))

        for item in items:
            c.execute("INSERT INTO shopping_list VALUES (:item)",
                      {
                          'item': item.text(),
                      })
        conn.commit()
        conn.close()

        message = QMessageBox()
        message.setWindowTitle("Saved")
        message.setText("Your list has been saved.")
        message.setIcon(QMessageBox.Information)
        m = message.exec_()

    def delete_item3(self):
        clicked = self.listWidget_3.currentRow()
        self.listWidget_3.takeItem(clicked)

    def clear_list3(self):
        self.listWidget_3.clear()

# travel list functions
# travel listesine ait fonksiyonlar
    def add_item4(self):
        item = self.inputBox_4.text()
        self.listWidget_4.addItem("-" + item)
        self.inputBox_4.setText("")

    def save_item4(self):
        conn = sqlite3.connect("takvim.db")
        c = conn.cursor()
        c.execute("DELETE FROM travel_list;",)
        items = []
        for index in range(self.listWidget_4.count()):
            items.append(self.listWidget_4.item(index))

        for item in items:
            c.execute("INSERT INTO travel_list VALUES (:item)",
                      {
                          'item': item.text(),
                      })
        conn.commit()
        conn.close()

        message = QMessageBox()
        message.setWindowTitle("Saved")
        message.setText("Your list has been saved.")
        message.setIcon(QMessageBox.Information)
        m = message.exec_()

    def delete_item4(self):
        clicked = self.listWidget_4.currentRow()
        self.listWidget_4.takeItem(clicked)

    def clear_list4(self):
        self.listWidget_4.clear()
