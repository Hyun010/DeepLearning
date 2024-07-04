data_int_a = 10
data_int_b = 3
# 따옴표 앞에 f로 시작하는 경우 f-string 이라고 부르며, 중괄호 안의 내용을 수행해서 수행된 결과를
# 문자열로 변환해서 하나의 문자열로 반환해주는 기능을 제공합니다.
# f'a + b = {data_int_a + data_int_b}' 의 경우 중괄호 안의 내용을 수행해서 10 + 3 의 결과값이 13이 저장되고
# 해당 값을 문자열 '13'으로 변경해 따옴표 안에 입력해서 하나의 문장으로 만들어줍니다.
print(f'a + b = {data_int_a + data_int_b}')
print(f'a - b = {data_int_a - data_int_b}')
print(f'a * b = {data_int_a * data_int_b}')
print(f'a ** b = {data_int_a ** data_int_b}') # 거듭제곱 연산 a^b
print(f'a / b = {data_int_a / data_int_b}') # 사칙 연산의 나누기, 나누기의 경우 실수로 변환되어 값이 계산됨
print(f'a // b = {data_int_a // data_int_b}') # 몫을 계산해주는 연산자
print(f'a % b = {data_int_a % data_int_b}') # 나머지를 계산해주는 연산자

data_float_a = 10.0
data_float_b = 2.0
print(f'a + b = {data_float_a + data_float_b}')
print(f'a - b = {data_float_a - data_float_b}')
print(f'a * b = {data_float_a * data_float_b}')
print(f'a ** b = {data_float_a ** data_float_b}') # 거듭제곱 연산 a^b
print(f'a / b = {data_float_a / data_float_b}') # 사칙 연산의 나누기, 나누기의 경우 실수로 변환되어 값이 계산됨
print(f'a // b = {data_float_a // data_float_b}') # 몫을 계산해주는 연산자
print(f'a % b = {data_float_a % data_float_b}') # 나머지를 계산해주는 연산자

data_string_a = "AI 서비스 런칭"
data_string_b = ' class 101'
print(data_string_a)
print(data_string_a + data_string_b) # 문자열의 더하기는 두개 문자열을 순대로 합친 결과가 반환된다.
print(data_string_a * 2) # 곱하기의 경우 data_string_a * 2는 data_string_a + data_string_a 와 동일하기 때문에 반복한 결과가 반환된다.
# 나머지 사칙연산은 동작하지 않는다.

data_bool_true = True # True는 파이썬에서 1과 동일하게 간주한다.
data_bool_false = False # False는 파이썬에서 0과 동일하게 간주한다.
print(data_bool_false and data_bool_true)
print(data_bool_false or data_bool_true)

# 모든 사칙연산은 표현 범위가 커지게 변형되며 표현 범위는 float이 가장크고 다음이 int 그리고 bool이 된다.
print(data_int_a + data_bool_true) # int + bool -> int / 10 + True = 10 + 1 = 11
print(data_int_a + data_float_a) # int + float -> float / 10 + 10.0 = 20.0
print(data_bool_true + data_float_a) # bool + float -> float True + 10.0 = 1 + 10.0 = 11.0
# str + bool, int, float -> error