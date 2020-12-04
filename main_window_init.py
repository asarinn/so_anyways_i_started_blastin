# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.inspire_courage_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.inspire_courage_check_box.setChecked(False)
        self.inspire_courage_check_box.setObjectName("inspire_courage_check_box")
        self.verticalLayout_4.addWidget(self.inspire_courage_check_box)
        self.haste_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.haste_check_box.setObjectName("haste_check_box")
        self.verticalLayout_4.addWidget(self.haste_check_box)
        self.two_weapon_fighting_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.two_weapon_fighting_check_box.setObjectName("two_weapon_fighting_check_box")
        self.verticalLayout_4.addWidget(self.two_weapon_fighting_check_box)
        self.deadly_aim_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.deadly_aim_check_box.setObjectName("deadly_aim_check_box")
        self.verticalLayout_4.addWidget(self.deadly_aim_check_box)
        self.point_blank_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.point_blank_check_box.setObjectName("point_blank_check_box")
        self.verticalLayout_4.addWidget(self.point_blank_check_box)
        self.improved_point_blank_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.improved_point_blank_check_box.setObjectName("improved_point_blank_check_box")
        self.verticalLayout_4.addWidget(self.improved_point_blank_check_box)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.close_and_deadly_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.close_and_deadly_check_box.setObjectName("close_and_deadly_check_box")
        self.horizontalLayout_2.addWidget(self.close_and_deadly_check_box)
        self.up_close_and_deadly_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        self.up_close_and_deadly_spin_box.setEnabled(False)
        self.up_close_and_deadly_spin_box.setMinimum(1)
        self.up_close_and_deadly_spin_box.setObjectName("up_close_and_deadly_spin_box")
        self.horizontalLayout_2.addWidget(self.up_close_and_deadly_spin_box)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.rapid_shot_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.rapid_shot_check_box.setObjectName("rapid_shot_check_box")
        self.verticalLayout_4.addWidget(self.rapid_shot_check_box)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.grit_pool_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        self.grit_pool_spin_box.setObjectName("grit_pool_spin_box")
        self.horizontalLayout_4.addWidget(self.grit_pool_spin_box)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.attack_bonus_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.attack_bonus_label.setFont(font)
        self.attack_bonus_label.setFrameShape(QtWidgets.QFrame.Box)
        self.attack_bonus_label.setObjectName("attack_bonus_label")
        self.horizontalLayout.addWidget(self.attack_bonus_label)
        self.num_hits_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        self.num_hits_spin_box.setMinimum(1)
        self.num_hits_spin_box.setObjectName("num_hits_spin_box")
        self.horizontalLayout.addWidget(self.num_hits_spin_box)
        self.damage_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.damage_label.setFont(font)
        self.damage_label.setFrameShape(QtWidgets.QFrame.Box)
        self.damage_label.setObjectName("damage_label")
        self.horizontalLayout.addWidget(self.damage_label)
        self.crit_multiplier_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        self.crit_multiplier_spin_box.setMinimum(2)
        self.crit_multiplier_spin_box.setMaximum(4)
        self.crit_multiplier_spin_box.setObjectName("crit_multiplier_spin_box")
        self.horizontalLayout.addWidget(self.crit_multiplier_spin_box)
        self.crit_damage_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.crit_damage_label.setFont(font)
        self.crit_damage_label.setFrameShape(QtWidgets.QFrame.Box)
        self.crit_damage_label.setObjectName("crit_damage_label")
        self.horizontalLayout.addWidget(self.crit_damage_label)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(4, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Blastin\'"))
        self.label.setText(_translate("MainWindow", "So Anyways I Started Blastin"))
        self.label_2.setText(_translate("MainWindow", "Buffs and ability modifiers:"))
        self.inspire_courage_check_box.setText(_translate("MainWindow", "Insipre Courage (Bard playing)"))
        self.haste_check_box.setText(_translate("MainWindow", "Haste"))
        self.two_weapon_fighting_check_box.setText(_translate("MainWindow", "Two Weapon Fighting"))
        self.deadly_aim_check_box.setText(_translate("MainWindow", "Deadly Aim"))
        self.point_blank_check_box.setText(_translate("MainWindow", "Point Blank Shot (30ft or closer)"))
        self.improved_point_blank_check_box.setText(_translate("MainWindow", "Improved Point Blank Shot (15ft or closer)"))
        self.close_and_deadly_check_box.setText(_translate("MainWindow", "Up Close and Deadly"))
        self.rapid_shot_check_box.setText(_translate("MainWindow", "Rapid Shot"))
        self.label_3.setText(_translate("MainWindow", "Tracked resources:"))
        self.label_4.setText(_translate("MainWindow", "Grit Pool:"))
        self.attack_bonus_label.setText(_translate("MainWindow", "Attack Bonus:"))
        self.num_hits_spin_box.setToolTip(_translate("MainWindow", "Number of Hits"))
        self.damage_label.setText(_translate("MainWindow", "Damage:"))
        self.crit_multiplier_spin_box.setToolTip(_translate("MainWindow", "Crit Multiplier"))
        self.crit_damage_label.setText(_translate("MainWindow", "Critical Damage:"))
