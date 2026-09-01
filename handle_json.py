import json,os

def read_json():
    json_file = os.path.join(os.path.dirname(__file__),"data.json")
    data = {}
    # print(json_file)
    try:
        with open(json_file,'rt',encoding="utf-8") as f:
            data = json.load(f)

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return
    except json.JSONDecodeError:
        print("Json 형식이 아닙니다.")
    except UnicodeDecodeError as e:
        print(e)
        return
    except Exception as e:
        print(e)
        return
        

    if data["meta"]["type"] == "json":
        # data.items() 를 하면 key와 value를 동시에 접근 가능함(딕셔너리에 씀)
        # enumerate(data)를 하면 index와 value를 동시에 접근 가능함(리스트,튜플에 씀)
        # for k,v in data.items():
            # print(f"key = {k} , value = {v}")
        # print(data)
        # 
        return data
        # return label_regularize(data)
        
    print("다시 실행 해주세요.")
    return





# 검증된 data를 담는 dict도 필요할거 같음
# 검증된 필터와 패턴들은 어떤게 있는지 표시하는 딕셔너리를 반환하는 함수이다.

# filters size_str cross,x
# patterns size_str +,x
def verificate(data:dict):

    # 쓰는 코드가 잘 썻는지 확인하는 코드가 필요하다.
    # 딕셔너리를 만들고 패턴 or 필터, size_n_n과 expected를 가져와 key로 만들고
    # value에 True와 False를 반환하게 하자
    verification_test_dict = {}

    filter_loadData_dict = {}
    # size - 크기를 넣자
    # + x - 필터 data
    # True - 있음
    if not data["meta"]["type"] == "json":
        return {}
    
    print("#","-"*20)
    print("#[1] 필터 로드")
    for size_str,size_dict in data["filters"].items():
        # k = cross, x
        for k,array in size_dict.items():
            result = _verificate_array_deep(array,size_str)
            if result:
                if size_str not in filter_loadData_dict:
                    filter_loadData_dict[size_str] = {}
                    
                filter_loadData_dict[size_str][k]= True
                verification_test_dict[f"filter {size_str} {k}"] = True
            else:
                if size_str not in filter_loadData_dict:
                    filter_loadData_dict[size_str] = {}
                
                filter_loadData_dict[size_str][k]= True
                verification_test_dict[f"filter {size_str} {k}"] = False

    for size_str , size_dict in data["patterns"].items():
        array = size_dict.get("input")
        # k = x, +
        k = size_dict.get("expected")

        result = _verificate_array_deep(array,size_str)
        if result:
            verification_test_dict[f"pattern {size_str} {k}"] = True
        else:
            verification_test_dict[f"pattern {size_str} {k}"] = False
    for n in [5,13,25]:
        for k in filter_loadData_dict.keys():
            if int(k.split("_")[1]) == n:
                print(f"✓ {k} 필터 로드 완료 (", end="")
                print(*list(filter_loadData_dict[k].keys()),sep=",",end="")
                print(")")
    print()
    # print(filter_loadData_dict)
    return verification_test_dict

# 검증을 한 후에 라벨링을 하느라 verification_test_dict에는 라벨링이 되지 않아 이 부분을 추가함
def verificated_dict_labelrize(verificate_dict:dict):

    registedList = list(verificate_dict.keys())
    # registedList를 돌면서 verificate_dict의 key에 있는 cross,x,+를 Cross or X로 바꾸자
    for k in registedList:
        original_label = k.split(" ")[2]
        if original_label in ["cross","+"]:
            after_label = "Cross"
        elif original_label == "x":
            after_label = "X"
        # after_k 를 이용해서 라벨링된 새로운 key를 할당함
        after_k = k.split(" ")[0]+ " " + k.split(" ")[1] + " " + after_label
        verificate_dict[after_k] = verificate_dict.pop(k)
    return verificate_dict


# 패턴과 키에 대해서
# N의 정사각행렬이 맞는지 확인
# N의 정사각행렬이 아니면 실패케이스에 등록
# size와 행렬을 주고
# 맞으면 True
# 다르면 False 를 반환하자
def _verificate_array(array:list[list],size_need_parse:str):
    size = int(size_need_parse.split("_")[1])
    if size == len(array) and size == len(array[0]):

        return True
    return False

# 다 맞는게 이상해서 하나 하나 확인해봄
def _verificate_array_deep(array:list[list],size_need_parse:str):
    size = int(size_need_parse.split("_")[1])
    if size != len(array):
        return False
    for l in array:
        if size != len(l):
            return False
    return True
# in-place 하게 수정중
# expected 값 정규화
# data안에서 바꾸는 내용들을 pop()하여 새로운 키를 배정하자
def label_regularize(data):
    # filter 키 정규화
    for size,filter_size_dict in data["filters"].items():
        # size : "size_5" , "size_13" , ...
        if "cross" in filter_size_dict:
            filter_size_dict["Cross"] = filter_size_dict.pop("cross")
        if "x" in filter_size_dict:
            filter_size_dict["X"] = filter_size_dict.pop("x")

    # expected 값 정규화
    # "+" -> "Cross"
    # "x" -> "X"
    for size,pattern_size_dict in data["patterns"].items():
        # size : size_5_1, ...
        # pattern_size_dict = {"input": list[list[float]],"expected":"x" or "+"}
        exp = pattern_size_dict.get("expected")
        if exp =="+":
            pattern_size_dict["expected"] = "Cross"
        if exp =="x":
            pattern_size_dict["expected"] = "X"
    return data

# 몰라서 찾아봄
# deepcopy 라이브러리를 대체하기 위해서 사용함
def copy_2d(original:list[list]):
    copied = []
    for row in original:
        copied.append(list(row))
    return copied

#시험 삼아 잘 출력 되는지 확인해봄
def test_label_regularize():
    r = read_json()
    # r = verificate(r)
    label_regularize(r)
    print("test입니다. ----- start")
    for k,v in r.items():
        if k == "meta":
            # meta 내부는 dict 형식
            for k2,v2 in r["meta"].items():
                print(f"{k}, value= {v}",sep="\n")
        if k == "filters":
            for size,size_dict in r["filters"].items():
                print(f"{k},key = {size} value= {v}",sep="\n")
        if k == "patterns":
            for size , pattern_size_dict in r["patterns"].items():
                print(f"{k},key = {size} value= {pattern_size_dict}",sep="\n",end="\n")

    print("test입니다. ----- end")
# 각 사이즈 마다 필터와 패턴들을 담자
# size
# pattern, filter
#  X +
# 패턴과 필터의 사이즈를 비교하고 다르면 실패 케이스에 추가 하자



if __name__ == "__main__":
    r = read_json()
    print("read_json")
    # print(r)
    dict_verify = verificate(r)
    print("verificate")
    print(dict_verify)
    dict_verify = verificated_dict_labelrize(dict_verify)
    print("verificated_dict_labelrize")
    print(dict_verify)
    label_regularize(r)
    
    # test_label_regularize()

