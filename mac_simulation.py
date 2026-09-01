from user_input import int_select,pat_fil_input
from config import user_input_mat_size
from mac import mac_2d
# from handle_json import verification_test_dict
from handle_json import read_json, verificate, label_regularize,test_label_regularize,verificated_dict_labelrize

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
            case 2:
                self.menu_2()


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
        u_match_filter(u_pattern,u_filter_A,u_filter_B)
        

    def menu_2(self):
        # test_label_regularize()
        # 데이터 읽어옴
        data = read_json()
        # 검증
        verified_dict = verificate(data)
        # 데이터 라벨링함
        label_regularize(data)
        # 검증때 가져온 dict도 라벨링함 나중에 쓰일거 같아서 가져옴
        verified_dict = verificated_dict_labelrize(verified_dict)
        print("#","-"*20)
        print(f"#[2] 패턴 분석 (라벨 정규화 적용)")
        print("#","-"*20)

        # [1] 가공된 data를 통해 pattern을 하나씩 가져 와야함
        # [2] pattern 사이즈에 맞게 각 각의 필터들을 가져와야함
        # mac 연산 실행
        # pattern key 출력
        # Cross에 대한 점수 출력 : label링된 값 출력하면 될듯
        # X 에 대한 점수 출력 : ..
        # 판정값 출력 : X , Cross , UNDECIDED
        # 예시
        # 판정: X | expected: X | PASS
        # 판정: Cross | expected: Cross | PASS
        # 판정: UNDECIDED | expected: X | FAIL (동점 규칙)
        for pat_name, pat_size_dict in data["patterns"].items():
            pat_size = pat_name.split("_")[1]
            same_size_filters = []
            for fil_name, size_dict_fil in data["filters"].items():
                if fil_name["_"][1] == pat_size:
                    for ex, fil in size_dict_fil:
                        
                    ...

            print("-"*10 , pat_name,"-"*10)
            
        print()
