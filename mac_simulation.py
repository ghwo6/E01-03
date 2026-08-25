from user_input import int_select,pat_fil_input
from config import user_input_mat_size
from mac import mac_2d


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
                self.menu_1()


    def menu_1(self):

        u_filter_A = pat_fil_input("필터","A")
        u_filter_B = pat_fil_input("필터","B")

        u_pattern = pat_fil_input("패턴")

        print("filter_A")
        print(u_filter_A)

        print("filter_B")
        print(u_filter_B)

        print("pattern")
        print(u_pattern)
        print("패턴과 필터 MAC연산 결과")
