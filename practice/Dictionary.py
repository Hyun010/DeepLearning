data_dict_a = dict()
data_dict_b = {}
# 딕셔너리 변수는 다음과 같이 두가지 방법으로 선언할 수 있습니다.
# 일반적으로 dict()가 보다 명확하기 때문에 dict로 선언하는 것을 기본으로 합니다.

data_dict_a['data1'] = 10 # 딕셔녀리에 특정 key에 값을 할당하고(등호 왼편에 위치) 싶다면
data_dict_b['data1'] = 10 # 변수다음에 대괄호를 입력하고 대괄호 사이에 나중에 저장한 값을 불러올 key를 입력합니다.
                          # 이떄 key는 이처럼 string 타입의 문자열일 수 도, 정수나 실수 값이 올 수도 있습니다.
                          # 일반적으로 기억하기 쉽게하기 위해 string 타입의 문자열로 key를 설정 하는 것이 좋습니다.

print(data_dict_a['data1'])
print(data_dict_b['data1'])

# 딕셔너리의 경우 사친연산을 수행할 수 없습니다. ex) data_dict_a + data_dict_b -> error
# data_dict_a + data_dict_b

data_dict_c = {
    'data1': 10,
    'data2': 20,
    'data3': 'data',
    'data4': data_dict_a
} # 딕셔너리에 여러개의 값을 한번에 할당하고자 하는 경우, 다음과 같은 방식으로 중괄호를 감싸고 key: value, 를 반복해서 입력하면
print(data_dict_c) # 한번에 딕셔너리에 데이터를 넣어서 저장할 수 있습니다.
print(data_dict_c['data1'])

# 만약 딕셔너리에 입력되지 않은 key를 호출한다면(등호 오른편에 위치 하거나 등호가 없이 사용되는 경우)
# data_dict_c['data5'] -> keyError라는 파이썬 에러를 발생시킵니다.
# data_dict_c['data5']
