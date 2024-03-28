################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

##################################################################
# 패키지 경로 설정(현재 디렉토리의 상위 디렉토리 경로를 환경변수로 추가)
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
##################################################################
print(sys.path)
# GUI FILE
from uis_graphic import ui_main

# IMPORT QSS CUSTOM
from uis_graphic import ui_styles

# IMPORT FUNCTIONS
from uis_graphic import ui_functions

## ==> APP FUNCTIONS
from app_functions import Functions
