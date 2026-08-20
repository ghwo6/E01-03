from user_input import int_select,one_line_input,mat_input
from config import user_input_mat_size

user_input_mat_size = 3

class Simulation():

    def __init__(self):
        self.exit_key_press = False


    def menu(self):
        print("=== ","Mini NPU Simulator", " ===")
        print()
        print("[모드 선택]")
        print()
        print("1. 사용자 입력 (3x3)")
        print("2. data.json 분석")
        select = int_select("> ",1,3)
        match select:

            case 1:
                one_line_input("숫자 3개 ㄱ")
                self.menu_1()


    def menu_1(self):
        mat_input
