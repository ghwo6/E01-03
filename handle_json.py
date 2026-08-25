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
        return label_regularize(data)
        
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

# 다른 파일에서는 호출 안되게(_) 설정함
def _filter_search(data):
    filter_table ={}

    ...

print(read_json())