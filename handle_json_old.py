import json,os

def read_json():
    json_file = os.path.join(os.path.dirname(__file__),"data.json")
    data = {}
    print(json_file)
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
        return data
        
    print("다시 실행 해주세요.")
    return

# 불러오는 과정에서 함수를 이쁘게 짜고 싶어서 일단 skip함
def filter_load(data:dict):
    print("#","-"*20)
    print(f"#[1] 필터 로드")
    print("#","-"*20)
    filter_hash_table =  _filter_search()
    print("✓")

def _filter_load():
    ...

# expected 값 정규화
# 아쉬움 : in-place 할 수 있었으면 좋겠다. -> new_data에서 다른 값들은 정상적으로 복사하기
# 아쉬움 : in-place 할 수 있었으면 좋겠다. -> data에서 pop()하고 키만 바꾸기
def label_regularize(data):
    new_data ={}
    # filter 키 정규화
    for k1,v1 in data["filters"].items():
        # k1 : "size_5", "size_13", ...
        for k2,v2 in v1.items():
            # k2 : "cross", "x"
            if k2 =="cross":
                # 얇은 복사가 이뤄진다고 한다. (대안 필요)
                new_data["filters"][k1]["Cross"] = copy_2d(v2)
            if k2 == "x":
                new_data["filters"][k1]["X"] = copy_2d(v2)
    
    # expected 값 정규화
    # "+" -> "Cross"
    # "x" -> "X"
    for k1,v1 in data["patterns"]:
        # k1 : size_5_1, ...
        for k2,v2 in v1.items():
            # k2 = "input" , "expected"
            if k2=="expected":
                if v2 == "+":
                    new_data["patterns"][k1]["expected"] = "Cross"
                elif v2 == "x":
                    new_data["patterns"][k1]["expected"] = "X"

    # in-place 할 수 있었으면 좋겠다.
    return new_data
# in-place 하게 수정중
# expected 값 정규화
# data안에서 바꾸는 내용들을 pop()하여 새로운 키를 배정하자 
def label_regularize_1(data):
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
        for k2,v2 in pattern_size_dict.items():
            # k2 = "input" , "expected"
            if k2 == "expected":
                if v2 =="+":
                    v2="Cross"
                if v2 =="x":
                    v2 = "X"

    # in-place 할 수 있었으면 좋겠다.
    return data

# 몰라서 찾아봄
# deepcopy 라이브러리를 대체하기 위해서 사용함
def copy_2d(original:list[list]):
    copied = []
    for row in original:
        copied.append(list(row))
    return copied

# 다른 파일에서는 호출 안되게(_) 설정함
def _filter_search(data):
    filter_table ={}

    ...

