# buttons.py
from PyQt6.QtWidgets import QPushButton

def create_button(text, geometry, callback, parent):
    button = QPushButton(text, parent)
    button.setGeometry(*geometry)  # unpacking for geometry
    button.clicked.connect(callback)  # Подключаем действие кнопки
    return button

def set_button_style(button, is_utilities_button=False):
    if is_utilities_button:
        button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                stop:0 black, stop:1 black);
                color: white;
                border: 1px solid white;
                border-radius: 10px;
                padding: 15px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                stop:0 white, stop:1 white);
                color: black;
                border: 1px solid white;
            }
        """)
    else:
        button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                stop:0 #6f1fe0, stop:1 #a911ee);
                color: white;
                border: none;
                border-radius: 10px;
                padding: 15px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                stop:0 white, stop:1 white);
                color: #a911ee;
            }
        """)

def setup_buttons(parent):
    buttons = []
    buttons_data = [
        ("CMD", (20, 90, 170, 55), parent.open_cmd),
        ("PowerShell", (20, 160, 170, 55), parent.open_PowerShell),
        ("RegEdit", (20, 230, 170, 55), parent.open_RegEdit),
        ("TaskMgr", (200, 90, 170, 55), parent.open_TaskMgr),
        ("DevMgr", (200, 160, 170, 55), parent.open_DevMgr),
        ("Win-Settings", (200, 230, 170, 55), parent.open_WinSettings),
        ("ResMon", (20, 300, 170, 55), parent.open_ResMon),
        ("DiskMgr", (200, 300, 170, 55), parent.open_DiskMgr),
        ("Win-Info", (20, 370, 170, 55), parent.open_WinInfo),
        ("Taskschd", (200, 370, 170, 55), parent.open_Taskschd),
        ("CleanMgr", (20, 440, 170, 55), parent.open_CleanMgr),
        ("NetConnect", (200, 440, 170, 55), parent.open_NetConnect),
        ("TYPE OF UTILITIES", (20, 520, 350, 55), parent.go_to_util_But_function)
    ]

    for text, geometry, callback in buttons_data:
        button = create_button(text, geometry, callback, parent)
        buttons.append(button)  # Сохраняем кнопку в список
        is_utilities_button = text == "TYPE OF UTILITIES"
        set_button_style(button, is_utilities_button)  # Устанавливаем стиль для каждой кнопки

    return buttons #список кнопок