EPSILON = 1e-9

# 나중에 시간 계산할때 간단하게 mac만 계산하도록 refactoring함
def mac_2d(mat_a:list[list[float]],mat_b:list[list[float]]):
    score = 0
    size = len(mat_a)
    for i in range(size):
        for j in range(size):
            score += mat_a[i][j] * mat_b[i][j]
    return score

# 유저 인풋에 대한 결과값을 나타내므로 앞에 u_ 를 붙임
def u_match_filter(pattern:list[list[float]],filter_A:list[list[float]],filter_B:list[list[float]]):
    u_score_A = mac_2d(pattern,filter_A)
    u_score_B = mac_2d(pattern,filter_B)
    result = ""
    
    print("#","-"*20)
    print(f"#[3] MAC 결과 (판정 불가)")
    print("#","-"*20)
    print("A 점수: ",u_score_A)
    print("B 점수: ",u_score_B)
    if abs(u_score_A - u_score_B) < EPSILON:
        result = "UNDECIDED"
        print("판정: 판정 불가 (|A-B| < 1e-9)")
    else:
        if u_score_A > u_score_B:
            result= "A"
        else:
            result= "B"
        print("판정: ",result)


# 처음에 만든 mac함수
# 멋대로 2차원의 배열도 mac 계산 가능하게 해놨다.
# 열의 갯수가 들쭉날쭉한 matrix 아닌것도 가능하도록 구현함
# 멋대로 추상화한 이상하게 생긴 이상한 함수
def mac_2d_abstract(mat_a:list[list[float]],mat_b:list[list[float]]):
    score = 0
    if dimension_size_check(mat_a,mat_b):
        # 행을 돈다.
        for i in range(0,len(mat_a)):
            # N차원이라는 가정도 빼자
            # 열의 돈다.
            for j in range(0,len(mat_a)):
                score += mat_a[i][j] * mat_b[i][j]
    return score

    # 애초에 문제가 이차원의 N의 정사각행렬이므로 아래의 코드로 구현함
def dimension_size_check(array1:list[list],array2:list[list]):
    if not isinstance(array1,list) or len(array1) == 0:
        return
    len_array1 = len(array1)
    
    if len(array1) == len(array2) and len(array1[0]) == len(array2[0]):
        return len_array1


    # 차원의 수가 같은지 확인하자
def dimension_size_check_hard(mat_a:list[list[float]],mat_b:list[list[float]]):

    # len(mat_a) : 3이면
    # range(0,len(mat_a)) : 0 , 1 , 2
    # index범위 안에서 돈다. 

    if len(mat_a) == len(mat_b):
        # len(mat_a): 행의 개수
        # 행마다 mat_a와 mat_b의 열의 개수가 같은지 확인하자.
        for i in range(0,len(mat_a)):
            if len(mat_a[i]) == len(mat_b[i]):
                # 열의 수가 같을떄
                continue
            else:
                # 열의 수가 다를떄
                return False
    else:
        # 행의 수가 다를때
        return False

    # 모든걸 거쳤지만 False를 만나지 않았을때
    return True

def dimension_size_check_recur(a,b):
    # 초기조건(recursive를 안돌게 하는 조건)
    if not isinstance(a,list) and not isinstance(b,list):
        if len(a) == len(b):
            return True

    # 둘 중에 하나만 리스트가 아니면?
    if not isinstance(a,list):
        return False
    if not isinstance(b,list):
        return False

    # 리스트면 돎
    if isinstance(a,list) and isinstance(b,list):
        for i in range(0,len(a)):

            # 하위 채널에 대해 recursive하게 열의 개수를 확인함
            if dimension_size_check_recur(a[i],b[i]):
                continue
            else:
                # 하위 채널에 대해서 recursive하게 확인해 보니 False가 뜸
                # False : (서로 차원의 갯수가 다름)
                return False

        # 모든 차원에 대해서 하위 채널의 열의 개수가 같음
        return True
        
