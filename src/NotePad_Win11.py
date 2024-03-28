##################################################################
# 패키지 경로 설정(현재 디렉토리의 상위 디렉토리 경로를 환경변수로 추가)
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
##################################################################

from PyQt5.QtWidgets import QApplication
# 기존 내 코드 패키지
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QTextEdit, QVBoxLayout, QWidget, QPushButton, QFileDialog, QToolBar, QAction, QMenuBar, QMenu, QTreeView, QFileSystemModel, QVBoxLayout, QSplitter

# 외부 라이브러리 용
from lib.Simple_PySide_Base_master.uis_src.main_ui import *
from PySide2 import QtGui

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())



"""
# app_function으로 이동
class TabbedNotepad(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabbed Notepad")
        self.setGeometry(100, 100, 800, 600)

        # 파일 탐색기 생성
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath(os.getcwd())
        self.file_tree = QTreeView()
        self.file_tree.setModel(self.file_system_model)
        self.file_tree.setRootIndex(self.file_system_model.index(""))

        # 탭 위젯 생성
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)  # 탭 닫기 활성화
        self.tab_widget.tabCloseRequested.connect(self.close_tab)

        # 탭 및 파일 탐색기를 감싸는 레이아웃
        splitter = QSplitter()
        splitter.addWidget(self.file_tree)
        splitter.addWidget(self.tab_widget)

        # 도구 모음 생성
        self.tool_bar = QToolBar()
        self.addToolBar(self.tool_bar)

        # 메뉴 바 생성
        self.menu_bar = self.menuBar()

        # 메뉴 생성
        file_menu = self.menu_bar.addMenu("File")

        # 액션 생성
        new_tab_action = QAction("New Tab", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)

        # 액션에 대한 동작 연결
        new_tab_action.triggered.connect(self.add_tab)
        open_action.triggered.connect(self.open_file)
        save_action.triggered.connect(self.save_file)
        exit_action.triggered.connect(self.close)

        # 메뉴에 액션 추가
        file_menu.addAction(new_tab_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(splitter)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 초기 파일 탐색 위치 설정
        self.file_system_model.setRootPath("")  # 기본 위치는 현재 작업 디렉토리입니다.

    def add_tab(self):
        # 새로운 탭 추가
        tab = QWidget()
        text_editor = QTextEdit()
        tab_layout = QVBoxLayout()
        tab_layout.addWidget(text_editor)
        tab.setLayout(tab_layout)

        self.tab_widget.addTab(tab, "Untitled")

    def open_file(self):
        # 파일 열기 다이얼로그
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text files (*.txt);;All files (*)")

        if file_path:
            # 파일 내용 읽어오기
            with open(file_path, "r") as file:
                content = file.read()

            # 현재 선택된 탭에 내용 채우기
            current_tab = self.tab_widget.currentWidget()
            text_editor = current_tab.findChild(QTextEdit)
            text_editor.setPlainText(content)

            # 탭 이름 설정
            self.tab_widget.setTabText(self.tab_widget.indexOf(current_tab), file_path)

    def save_file(self):
        # 파일 저장 다이얼로그
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text files (*.txt);;All files (*)")

        if file_path:
            # 현재 선택된 탭의 내용 가져오기
            current_tab = self.tab_widget.currentWidget()
            text_editor = current_tab.findChild(QTextEdit)
            content = text_editor.toPlainText()

            # 파일에 내용 저장
            with open(file_path, "w") as file:
                file.write(content)

            # 탭 이름 설정
            self.tab_widget.setTabText(self.tab_widget.indexOf(current_tab), file_path)

    def close_tab(self, index):
        # 탭 닫기 기능
        self.tab_widget.removeTab(index)"""


"""
################################
 초기 테스트 버전
###############################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabbedNotepad()
    window.show()
    sys.exit(app.exec_())
"""
