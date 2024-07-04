data_list_a = [1, 2, 3.0, 4] # list는 대괄호를 활용하여 여러개의 값을 콤마로 구분하여 감싸서 변수를 선언할 수 있다.


print(data_list_a[0]) # 딕셔너리와 차이는 특정 값을 조회하는 key를 파이썬이 자동으로 설정해주고, 0에서 1씩 커지게 설정이 된다.
print(data_list_a[2])
print(data_list_a[-1]) # 또한 파이썬에서는 리스트의 마지막값에 -1이라는 key가 추가로 할당되고,
print(data_list_a[-3]) # 계속해서 -1로 감소시켜 값을 반대방향에서 읽어 올 수 있습니다.
# print(data_list_a[4]) # 저장된 갯수를 넘어서는 위치의 값을 조회하는 경우 IndexError를 발생
# print(data_list_a[-5])

print(data_list_a[1])
data_list_a[1] = 20 # 특정 순서의 데이터를 변경할 때는 원하는 데이터의 위치의 숫자를 대괄호로 감싸고
print(data_list_a[1]) # 등호로 할당하면 해당 숫자 위치의 값이 변경된다.

# 리스트의 경우 더하기 연산을 사용할 수 있다.
# 더하기 연산은 두 리스트를 하나의 리스트로 합치는 역할을 한다.
data_list_1 = [0, 1]
data_list_2 = [2, 3]
data_list_3 = data_list_1 + data_list_2
print(data_list_3) # [0, 1, 2, 3]