import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Wordpad(QMainWindow):
    def __init__(self):
        super(Wordpad, self).__init__()
        self.editor = QTextEdit()
        self.editor.setFontPointSize(20)
        self.setCentralWidget(self.editor)
        self.showMaximized()
        self.setWindowTitle("Wordpad")
        self.create_tool_bar()


    def create_tool_bar(self):
        tool_bar = QToolBar()


        undo_action = QAction(QIcon("undo.png"), "undo", self)
        undo_action.triggered.connect(self.editor.undo)
        tool_bar.addAction(undo_action)

        redo_action = QAction(QIcon("redo.png"), "redo", self)
        redo_action.triggered.connect(self.editor.redo)
        tool_bar.addAction(redo_action)

        tool_bar.addSeparator()
        tool_bar.addSeparator()


        cut_action = QAction(QIcon("cut.png"), "cut", self)
        cut_action.triggered.connect(self.editor.cut)
        tool_bar.addAction(cut_action)

        copy_action = QAction(QIcon("copy.png"), "copy", self)
        copy_action.triggered.connect(self.editor.copy)
        tool_bar.addAction(copy_action)

        paste_action = QAction(QIcon("paste.png"), "paste", self)
        paste_action.triggered.connect(self.editor.paste)
        tool_bar.addAction(paste_action)

        tool_bar.addSeparator()
        tool_bar.addSeparator()



        self.addToolBar(tool_bar)



app = QApplication(sys.argv) 
window = Wordpad() 
window.show() 
sys.exit(app.exec_())