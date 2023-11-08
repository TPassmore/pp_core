from PySide6 import QtWidgets, QtCore, QtGui
from pp_core.pp_system import pp_file
from pp_core import pp_util



class Image_push_button(QtWidgets.QPushButton):

    def __init__(self, icon_path):

        super().__init__()     
        self.set_icon_from_file(icon_path)
        self.setStyleSheet("""
                           QPushButton {border: none; padding: 0; background-color: transparent; border-radius: 5px;}
                           QPushButton:Hover {background-color: rgba(105, 105, 255, 80)}
                           QPushButton:Pressed {background-color: rgba(45, 67, 179, 80)}
                           """)
        self.setIconSize(QtCore.QSize(24, 24))

    def set_icon_from_file(self, icon_path):
        try: pp_file.find_in_path(icon_path)
        except FileNotFoundError as e: 
            pp_util.print_error(f'cannot find icon: {icon_path}')
            return False
        self.setIcon(QtGui.QIcon(icon_path))