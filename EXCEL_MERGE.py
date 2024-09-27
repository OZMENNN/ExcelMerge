# noinspection PyUnresolvedReferences
# -*- coding: utf-8 -*-


import pandas as pd
import os
import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer


def greet():
    print("Excel dosyaları başarıyla birleştirildi! Bu pencere 5 saniye sonra kapanacak.")
    # search
    folder_path = r'C:\Users\MT\PycharmProjects\excelMerge'

    # new DataFrame
    combined_df = pd.DataFrame()

    # check
    for filename in os.listdir(folder_path):
        if filename.endswith('.xls') or filename.endswith('.xls'):
            file_path = os.path.join(folder_path, filename)

            # read
            df = pd.read_excel(file_path)

            # DataFrame merge
            combined_df = pd.concat([combined_df, df], ignore_index=True)

    # write
    combined_df.to_excel('combined_output.xlsx', index=False)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("")
layout = QVBoxLayout()
label = QLabel("Excel Dosyalarını Birleştir")
layout.addWidget(label)
button = QPushButton("BİRLEŞTİREK İÇİN TIKLA.")
button.clicked.connect(greet)
layout.addWidget(button)

window.setLayout(layout)
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        QTimer.singleShot(5000, self.close)  # Make sure this line is aligned correctly

# Pencereyi göster
window.show()
sys.exit(app.exec_())















