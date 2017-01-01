import csv

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex as rgb
TABLE_COLUMNS = 18
TABLE_ROWS = 10
ELEMENTS = []
ELEMENT_COLOR_MAP = {
    "Metalloids": rgb('77DD88'),
    "Nonmetals": rgb('22FF22'),
    "Halogens": rgb('22EECC'),
    "Noble gases": rgb('77CCFF'),
    "Alkali metals": rgb('FFCC33'),
    "Alkaline earth metals": rgb('FFFF44'),
    "Lanthanoids": rgb('FFBB99'),
    "Transition metals": rgb('DDBBBB'),
    "Post-transition metals": rgb('99DDCC'),
    "Actinoids": rgb('EEBBDD'),
}


def load_element_info():
    with open('element_properties.csv', 'r', encoding="ISO-8859-1") as f:
        elem_dict = csv.DictReader(f)
        list_elem_dict = list(elem_dict)
    return list_elem_dict


class Element(Button):
    def __init__(self, info, **kwargs):
        super(Element, self).__init__(**kwargs)
        self.info = info
        self.background_color = ELEMENT_COLOR_MAP[info["Element_Category"]]

    def get_info(self):
        r = ["{}: {}".format(k, v) for k, v in self.info.items()]
        return "\n".join(r)


class ElementDetailPage(Widget):
    pass


class MainWidget(Widget):
    pass


class PeriodicTableApp(App):
    def build(self):
        self.main_widget = MainWidget()
        self.main_widget.table_layout.cols = TABLE_COLUMNS
        self.main_widget.table_layout.rows = TABLE_ROWS

        for i_cell in range(TABLE_ROWS * TABLE_COLUMNS):
            row = int(i_cell / TABLE_COLUMNS) + 1
            col = i_cell % TABLE_COLUMNS + 1
            self.main_widget.table_layout.add_widget(self.create_cell(row, col))
        return self.main_widget

    @staticmethod
    def create_cell(row, col):
        for elem in ELEMENTS:
            if int(elem['table_row']) == row and int(elem['table_col']) == col:
                return Element(info=elem, text=elem['Symbol'])
        return Label()

if __name__ == '__main__':
    ELEMENTS = load_element_info()
    PeriodicTableApp().run()
