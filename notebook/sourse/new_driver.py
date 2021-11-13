from PyQt5.QtCore import QRegExp as QRE
from PyQt5.QtGui import QRegExpValidator as QREVal
from new_template import TempForm
from database import *


class NewDriver(TempForm):
    def __init__(self, parent=None):
        self.status_ = True
        self.conf = Ini(self)
        ui_file = self.conf.get_ui("new_driver")
        super(NewDriver, self).__init__(ui_file, parent, "drivers")
        if self.parent.db.init_list(self.cb_select, "*", self.table, people=True) == ERR:
            self.status_ = False
            return
        self.list_ui = [self.family, self.name, self.surname, self.d_birthday, self.passport, self.adr]

    def init_mask(self):
        symbols = QREVal(QRE("[а-яА-Я 0-9]{9}"))
        for item in self.list_ui:
            item.setValidator(symbols)

    def _select(self, text):
        return True