from config import user_input_mat_size

MAT_SIZE = user_input_mat_size

def int_select(explain:str, under:int,uppper:int):
    while True:
        select = input(explain).strip()
        # 빈칸 입력시
        if select == "":
            print("빈칸이 입력되었습니다. 다시 입력해주세요.","\n")
        else:
            if select.isdigit():
                select = int(select)
                if under <= select <= uppper:
                    return select
                else:
        # 범위가 벗어난 값 입력시
                    print(f"{under} ~ {uppper} 사이의 값을 입력해주세요.")
        # 숫자가 아닌 값 입력시
            else:
                print("숫자를 입력해주세요.")

# explain에는 몇번쨰 행을 입력해주세요. 하고 입력해주자
def one_line_input(explain:str):
    while True:
        select = input(explain).strip()
        array = select.split(" ")
        if len(array) == MAT_SIZE:
            digitable_lengh = 0
            for i in array:
                if i.isdigit():
                    digitable_lengh +=1
                else:
                    print(f"{i}는 숫자로 변형이 불가합니다. 다시 입력바랍니다.")
            # digitable_length 가 MAT_size (3) 일경우

            if digitable_lengh == MAT_SIZE:
                # print( int(array[0]),int(array[1]),int(array[2]))
                # [int(x) for x in array]와 같음

                return [int(x) for x in array]
        else:
            print(f"{MAT_SIZE} 개의 숫자를 입력해야 합니다.")

# pattern_input
def _mat_input(explain:str):
    n = MAT_SIZE
    mat = []
    print(str)
    for i in range(MAT_SIZE):
        l = one_line_input(f"{i+1}번째 행을 입력해주세요.")
        mat.append(l)

    return mat

# pattern은 1과 2가 들어오니까 이를 추상황해서 반복되는 과정을 줄이자.
# pattern만 있는지 알았는데 filter도 있다. if를 사용해 type을 확인하도록 하자
# type : pattern 또는 filter
# mat_input을 추상화 한다고 생각하자.

# mat_input(~)을 이용하여 패턴 또는 필터 1 2를 입력
# _mat_input(~)에서 one_line_input(~) -> int~~
def mat_input(type:str,number:int):

    print("=================================")
    print(f" [{number}] {type} 입력")
    print("=================================")

    return _mat_input(f"{type} {number} {MAT_SIZE}줄 입력, 공백 구분")

    