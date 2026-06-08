from random import randint
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsEllipseItem,
    QGridLayout,
    QVBoxLayout,
    QWidget
)
from PyQt6.QtGui import QBrush
from PyQt6.QtCore import Qt

app = QApplication([])

class MainWindow(QWidget):
    def grid(self):
        node_lst = []
        for _ in range(0,30):
            break_con = False
            while break_con != True:
                new_node_coords = (randint(15, 485), randint(15, 405))
                accept_cnt = 0
                for old_node_coords in node_lst:
                    if ((new_node_coords[0]-old_node_coords[0])**2 + (new_node_coords[1]-old_node_coords[1])**2)**0.5 >= 25:
                        accept_cnt += 1
                if accept_cnt == len(node_lst):
                    node_lst.append(new_node_coords)
                    break_con = True
        print(node_lst)
        return node_lst

    def __init__(self):
        super().__init__()
        node_lst = self.grid()
        self.setWindowTitle("The Earth Is Flat")
        self.setFixedSize(800, 450)

        scene = QGraphicsScene(0, 0, 500, 420)

        for coords in node_lst:
            ellipsis = QGraphicsEllipseItem(0, 0, 12.5, 12.5)
            ellipsis.setPos(coords[0], coords[1])
            brush = QBrush(Qt.GlobalColor.blue)
            ellipsis.setBrush(brush)
            scene.addItem(ellipsis)

        """
        column width (125px)
        row width (105px)
        = grid size 750px * 420px
        """
        view = QGraphicsView(scene)
        
        layout = QGridLayout()
        self.setLayout(layout)

        stack = QWidget()
        stack_layout = QVBoxLayout()
        stack.setLayout(stack_layout)

        layout.addWidget(stack, 0, 4, 2, 4)
        layout.addWidget(view, 0, 0, 4, 4)

        # add stack widgets here



window = MainWindow()
window.show()

app.exec()