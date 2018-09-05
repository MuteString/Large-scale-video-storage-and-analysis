# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mianwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from Video_Retrieval import GetFeatures, Search_Process
import sys
import cv2 as cv
import os


class Ui_MainWindow(QtWidgets.QMainWindow):
    SAMPLE_PATH = ''
    SAMPLE_NAME = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("视频搜索Demo")
        MainWindow.resize(797, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 110, 771, 441))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 756, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 2, 160, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filepath_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.filepath_label.setLineWidth(0)
        self.filepath_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filepath_label.setOpenExternalLinks(False)
        self.filepath_label.setObjectName("filepath_label")
        self.horizontalLayout.addWidget(self.filepath_label)
        self.filepath_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.filepath_lineEdit.setObjectName("filepath_lineEdit")
        self.horizontalLayout.addWidget(self.filepath_lineEdit)
        self.choosefile_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.choosefile_btn.setObjectName("choosefile_btn")
        self.horizontalLayout.addWidget(self.choosefile_btn)
        self.confirm_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.confirm_btn.setObjectName("confirm_btn")
        self.horizontalLayout.addWidget(self.confirm_btn)
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 23))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_about = QtWidgets.QMenu(self.menubar)
        self.menu_about.setObjectName("menu_about")
        self.menu_set = QtWidgets.QMenu(self.menubar)
        self.menu_set.setObjectName("menu")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.actionopen_file = QtWidgets.QAction(MainWindow)
        self.actionopen_file.setIconText("打开文件")
        self.actionopen_file.setIconVisibleInMenu(True)
        self.actionopen_file.setObjectName("actionopen_file")
        self.actionsetwindow = QtWidgets.QAction(MainWindow)
        self.actionsetwindow.setObjectName("action")
        self.menu_file.addAction(self.actionopen_file)
        self.menu_set.addAction(self.actionsetwindow)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_set.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())

        self.choosefile_btn.clicked.connect(self.OpenFile)
        self.confirm_btn.clicked.connect(self.SearchVideo)
        self.actionopen_file.triggered.connect(self.OpenFile)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "视频检索"))
        self.filepath_label.setText(_translate("MainWidd20.ndow", "样例视频："))
        self.choosefile_btn.setText(_translate("MainWindow", "浏览"))
        self.confirm_btn.setText(_translate("MainWindow", "搜索"))
        self.menu_file.setTitle(_translate("MainWindow", "文件"))
        self.menu_about.setTitle(_translate("MainWindow", "关于"))
        self.menu_set.setTitle(_translate("MainWindow", "设置"))
        self.actionopen_file.setText(_translate("MainWindow", "选择样例视频"))
        self.actionsetwindow.setText(_translate("MainWindow", "系统设置"))

    def OpenFile(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, '打开文件', '.', "视频文件(*.avi *.mp4)")
        self.SAMPLE_PATH = filepath
        self.SAMPLE_NAME = filepath.split('/')[-1]
        self.filepath_lineEdit.setText(self.SAMPLE_NAME)

    def SearchVideo(self):
        if self.SAMPLE_PATH != '':
            print(self.SAMPLE_PATH)
            result_list = Search_Process.search_process(20, self.SAMPLE_PATH)
            root_dir = '../Videos4Retrieval/'
            thumb_dir = '../Videos4Retrieval/thumbs/'
            # for i in range(len(result_list)):
            for i in range(50):
                video_name = result_list[i][0].split('.')[0]
                starttime = result_list[i][1][1]
                img = thumb_dir + video_name + '.jpg'
                video_path = root_dir + video_name + '.avi'
                a = i / 4
                b = i % 4
                pos = (a, b)
                self.AddPictures(video_name, img, video_path, pos, starttime)
                self.scrollAreaWidgetContents.setLayout(self.gridLayout)
        else:
            QtWidgets.QMessageBox.information(self, "未选择样例视频", "请先选择需要进行搜索的样例视频。")

    def AddPictures(self, name, image, path, pos, start):
        image_p = cv.imread(image)
        height = image_p.shape[0]/2
        width = image_p.shape[1]/2
        pic_button = QtWidgets.QToolButton()
        pic_button.setText(name)
        pic_button.setIcon(QtGui.QIcon(image))
        pic_button.setIconSize(QtCore.QSize(width, height))
        pic_button.setAutoRaise(True)
        pic_button.setToolButtonStyle(Qt.Qt.ToolButtonTextUnderIcon)
        pic_button.clicked.connect(lambda: self.PlayVideo(path, start))

        self.gridLayout.addWidget(pic_button, *pos)

    def PlayVideo(self, path, start):
        os.system('mpv ' + path + ' --start=' + start)     # play video use mpv on ubuntu
        pass


class Ui_SetWindow(QtWidgets.QFrame):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setEnabled(True)
        Frame.resize(502, 369)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.groupBox = QtWidgets.QGroupBox(Frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 481, 211))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 461, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_btn.setObjectName("add_btn")
        self.verticalLayout.addWidget(self.add_btn)
        self.delete_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.delete_btn.setObjectName("delete_btn")
        self.verticalLayout.addWidget(self.delete_btn)
        self.choiceall_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.choiceall_btn.setObjectName("choiceall_btn")
        self.verticalLayout.addWidget(self.choiceall_btn)
        self.dechoiceall_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.dechoiceall_btn.setObjectName("dechoiceall_btn")
        self.verticalLayout.addWidget(self.dechoiceall_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(178)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Frame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 250, 481, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 441, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.sure_btn = QtWidgets.QPushButton(Frame)
        self.sure_btn.setGeometry(QtCore.QRect(320, 330, 75, 23))
        self.sure_btn.setObjectName("sure_btn")
        self.cancel_btn = QtWidgets.QPushButton(Frame)
        self.cancel_btn.setGeometry(QtCore.QRect(410, 330, 75, 23))
        self.cancel_btn.setObjectName("cancel_btn")

        # self.cancel_btn.clicked.connect(self.handle_close)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "系统设置"))
        self.groupBox.setTitle(_translate("Frame", "需要检索的数据库"))
        self.add_btn.setText(_translate("Frame", "添加"))
        self.delete_btn.setText(_translate("Frame", "删除"))
        self.choiceall_btn.setText(_translate("Frame", "全选"))
        self.dechoiceall_btn.setText(_translate("Frame", "全不选"))
        self.groupBox_2.setTitle(_translate("Frame", "计算方式"))
        self.radioButton_3.setText(_translate("Frame", "自动选择（推荐）"))
        self.radioButton_2.setText(_translate("Frame", "Spark分布式计算"))
        self.radioButton.setText(_translate("Frame", "单节点计算"))
        self.sure_btn.setText(_translate("Frame", "确定"))
        self.cancel_btn.setText(_translate("Frame", "取消"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    frame = QtWidgets.QFrame()
    setwindow = Ui_SetWindow()
    setwindow.setupUi(frame)
    widget.show()
    ui.actionsetwindow.triggered.connect(frame.show)
    setwindow.cancel_btn.clicked.connect(frame.close)
    sys.exit(app.exec_())
