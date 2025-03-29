# fonts.py
import os
from PyQt6.QtGui import QFont, QFontDatabase

def apply_fonts(elements_font1, elements_font2):
    # Путь к файлам шрифтов
    font_directory = os.path.join(os.path.dirname(__file__), "fonts")
    font_path = os.path.join(font_directory, "arialroundedmtbold.ttf")
    another_font_path = os.path.join(font_directory, "Widock TRIAL Bold.otf")

    # Добавляем шрифты
    font_id = QFontDatabase.addApplicationFont(font_path)
    another_font_id = QFontDatabase.addApplicationFont(another_font_path)

    if font_id != -1 and another_font_id != -1:  # Проверяем, успешно ли добавлены оба шрифта
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        another_font_family = QFontDatabase.applicationFontFamilies(another_font_id)[0]

        # Применяем первый шрифт
        for element in elements_font1:
            element.setFont(QFont(font_family, 16, QFont.Weight.Bold))

        # Применяем второй шрифт
        for element in elements_font2:
            element.setFont(QFont(another_font_family, 16, QFont.Weight.Bold))
    else:
        # Если не удалось загрузить шрифты, использовать запасной Arial
        for element in elements_font1 + elements_font2:
            element.setFont(QFont("Arial", 16, QFont.Weight.Bold))