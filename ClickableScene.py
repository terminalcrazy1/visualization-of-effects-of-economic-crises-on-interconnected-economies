from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsSceneMouseEvent
from typing import Any, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from GridPoint import GridPoint
    from MainWindow import MainWindow

class ClickableScene(QGraphicsScene):
    def __init__(self, parent_window: 'MainWindow', *args: Any) -> None:
        super().__init__(*args)
        self.window: 'MainWindow' = parent_window
        self.last_point: Optional['GridPoint'] = None
    
    def get_pt_at(self, event: QGraphicsSceneMouseEvent) -> Optional['GridPoint']:
        pos = event.scenePos()
        for pt in self.window.pts:
            if abs(pt.coords[0] - pos.x()) < 10 and abs(pt.coords[1] - pos.y()) < 10:
                return pt
        return None

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        pt = self.get_pt_at(event)
        if not pt: return

        if event.button() == Qt.MouseButton.LeftButton:
            if self.last_point:
                pt2 = pt
                pt1 = self.last_point
                pt1.addLink(pt2)
                pt2.addLink(pt1)
                line = self.addLine(pt1.coords[0]+5, pt1.coords[1]+5, pt2.coords[0]+5, pt2.coords[1]+5)
                pt1.lines.append(line)
                pt2.lines.append(line)
                self.last_point = None
            else:
                self.last_point = pt
                
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.window.load_indicator.setText("Load: " + str(pt.load))
            
        elif event.button() == Qt.MouseButton.RightButton:
            self.window.origin = self.window.pts.index(pt)