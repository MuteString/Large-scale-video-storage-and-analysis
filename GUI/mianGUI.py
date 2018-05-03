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


class Ui_MainWindow(QtWidgets.QMainWindow):
    SAMPLE_PATH = ''
    SAMPLE_NAME = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 31))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_about = QtWidgets.QMenu(self.menubar)
        self.menu_about.setObjectName("menu_about")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.actionopen_file = QtWidgets.QAction(MainWindow)
        self.actionopen_file.setIconText("打开文件")
        self.actionopen_file.setIconVisibleInMenu(True)
        self.actionopen_file.setObjectName("actionopen_file")
        self.menu_file.addAction(self.actionopen_file)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())

        self.choosefile_btn.clicked.connect(self.OpenFile)
        self.confirm_btn.clicked.connect(self.SearchVideo)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filepath_label.setText(_translate("MainWindow", "文件路径："))
        self.choosefile_btn.setText(_translate("MainWindow", "浏览"))
        self.confirm_btn.setText(_translate("MainWindow", "搜索"))
        self.menu_file.setTitle(_translate("MainWindow", "文件"))
        self.menu_about.setTitle(_translate("MainWindow", "关于"))
        self.actionopen_file.setText(_translate("MainWindow", "打开文件"))

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
            for i in range(len(result_list)):
                video_name = result_list[i][0].split('.')[0]
                img = thumb_dir + video_name + '.jpg'
                video_path = root_dir + video_name + '.avi'
                a = i / 3
                b = i % 3
                pos = (a, b)
                self.AddPictures(video_name, img, video_path, pos)
                self.scrollAreaWidgetContents.setLayout(self.gridLayout)
        else:
            unselect_message = QtWidgets.QMessageBox.information(self, "未选择样例视频", "请先选择需要进行搜索的样例视频。")

    def AddPictures(self, name, image, path, pos):
        image_p = cv.imread(image)
        height = image_p.shape[0]
        width = image_p.shape[1]
        pic_button = QtWidgets.QToolButton()
        pic_button.setText(name)
        pic_button.setIcon(QtGui.QIcon(image))
        pic_button.setIconSize(QtCore.QSize(height, width))
        pic_button.setAutoRaise(True)
        pic_button.setToolButtonStyle(Qt.Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(pic_button, *pos)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
