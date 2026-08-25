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

# 패턴인지 필터인지 확인
# 몇번째 패턴, 필터인지 확인
# user_input하는 차원의 수 만큼 one_line_input 반환함
def pat_fil_input(pat_or_fil:str,sep_str:str="")->list[MAT_SIZE]:
    print("#","-"*20)
    if pat_or_fil =="필터":
        print(f"#[1] [{sep_str}] 필터 입력")
    else:
        print(f"#[2] 패턴 입력")

    print("#","-"*20)

    print(f"{pat_or_fil} {sep_str} ({MAT_SIZE}줄 입력, 공백 구분)")
    
    matrix = []
    for i in range(0,MAT_SIZE):
        row = one_line_input(f"row:{i+1}> ")
        matrix.append(row)

    return matrix

# explain에는 몇번쨰 행을 입력해주세요. 하고 입력해주자
def one_line_input_mag(explain:str):
    while True:
        select = input(explain).strip()
        array = select.split(" ")
        if len(array) == MAT_SIZE:
            digitable_lengh = 0
            for i in array:
                try:
                    i_f = float(i)
                    if -1 <= i_f <= 1:
                        digitable_lengh +=1
                    else:
                        print("-1 ~ 1사이의 값을 입력해주세요.")
                except:
                    print(f"{i}는 float으로 변환이 불가합니다.")
            # digitable_length 가 MAT_size (3) 일경우

            if digitable_lengh == MAT_SIZE:
                # print( int(array[0]),int(array[1]),int(array[2]))
                # [int(x) for x in array]와 같음

                return [float(x) for x in array]
        else:
            print(f"{MAT_SIZE} 개의 숫자를 입력해야 합니다.")
            print("0 1 0 처럼 띄어 쓰기(' ')로 구분 바랍니다.")

def one_line_input(explain:str):
    while True:
        select = input(explain).strip()
        array = select.split(" ")
        if len(array) == MAT_SIZE:
            digitable_lengh = 0
            for i in array:
                try:
                    i_f = float(i)
                    digitable_lengh +=1
                except:
                    print(f"{i}는 float으로 변환이 불가합니다.")
            # digitable_length 가 MAT_size (3) 일경우

            if digitable_lengh == MAT_SIZE:
                # print( int(array[0]),int(array[1]),int(array[2]))
                # [int(x) for x in array]와 같음

                return [float(x) for x in array]
        else:
            print(f"{MAT_SIZE} 개의 숫자를 입력해야 합니다.")
            print("0 1 0 처럼 띄어 쓰기(' ')로 구분 바랍니다.")
