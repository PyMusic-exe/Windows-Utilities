import sys
import os
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QLabel #,QWidget
from PyQt6.QtGui import QIcon
from BlurWindow.blurWindow import blur
#from PyQt6.QtCore import Qt, QPropertyAnimation

# import from my modules --
from fonts import apply_fonts  # Импортируем функцию из fonts.py
from buttons import setup_buttons  # Импортируем функцию из buttons.py


class WU_mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        blur(self.winId())
        self.setWindowTitle("W I N D O W S   -   U T I L I T I E S")
        self.setGeometry(100, 100, 1200, 600)  # Размер окна
        self.setStyleSheet("""
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, 
                                stop: 0 #6f1fe0, stop: 1 #a911ee); 
                    border-radius: 0px;
                """)
        self.setWindowIcon(QIcon('icon/WU-Icon.ico')) #иконка
        self.setMaximumSize(1200, 600)
        self.setMinimumSize(1200, 600)

        # контейнер с кнопками
        container = QFrame(self)
        container.setGeometry(-10, -10, 400, 700)

        # стиль контейнера
        container.setStyleSheet("""
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 black, stop: 1 black); 
                    border-radius: 10px;
                """)

        # добавляем заголовок в контейнер

        self.S_u = QLabel("SYSTEM UTILITIES", self)
        self.S_u.setGeometry(48, 30, 300, 50) # расположение
        self.S_u.setStyleSheet(
            "color: white;"
            "font-size: 24px;"
            "background-color: black"
        )

        # Загружаем кнопки (buttons.py)
        self.buttons = setup_buttons(self)

        # Загружаем шрифты (fonts.py)
        main_elements = self.buttons
        another_elements = [self.S_u, self.buttons[-1]]
        apply_fonts(main_elements, another_elements)

    def open_cmd(self):
        # Получаем букву диска пользователя
        user_drive = os.path.splitdrive(os.environ['USERPROFILE'])[0]
        subprocess.Popen(f"start cmd.exe /K cd {user_drive}\\", shell=True)
        # Выполнение действия
    def open_PowerShell(self):
        # Получаем букву диска пользователя
        user_drive = os.path.splitdrive(os.environ['USERPROFILE'])[0]
        # Выполнение действия
        subprocess.Popen(f"start powershell.exe -NoExit -Command Set-Location '{user_drive}\\'", shell=True)

    def open_RegEdit(self):
        subprocess.Popen("regedit.exe", shell=True)

    def open_TaskMgr(self):
        subprocess.Popen("taskmgr.exe", shell=True)

    def open_DevMgr(self):
        subprocess.Popen("devmgmt.msc", shell=True)

    def open_WinSettings(self):
        subprocess.Popen("start ms-settings:", shell=True)

    def open_ResMon(self):
        subprocess.Popen("ResMon", shell=True)

    def open_DiskMgr(self):
        subprocess.Popen("diskmgmt.msc", shell=True)

    def open_WinInfo(self):
        subprocess.Popen("msinfo32", shell=True)

    def open_Taskschd(self):
        subprocess.Popen("Taskschd.msc", shell=True)

    def open_CleanMgr(self):
        subprocess.Popen("CleanMgr", shell=True)

    def open_NetConnect(self):
        subprocess.Popen("ncpa.cpl", shell=True)

    def go_to_util_But_function(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WU_mainWindow()
    window.show()
    sys.exit(app.exec())