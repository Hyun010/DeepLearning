# 변수
# 파이썬 코드에서 샾은 샾 이후의 내용에 대해서는 파이썬이 읽지 않고 넘어가는 사람만 읽는 코드를 의미합니다.

exchange_rate = 1100 # 원 / 달러 환율, 0x5e90d4c0

# day 1
print("="*10 + "day 1" + "="*10)
dollar_in_account = 3.5 # 0x5eead4c0
korea_won = int(dollar_in_account * exchange_rate)
print(f"현재 가지고 있는 금액은 원화로 : {korea_won}원 입니다.")

# day 2
print("="*10 + "day 2" + "="*10)
dollar_in_account = dollar_in_account + 5
korea_won = int(dollar_in_account * exchange_rate)
print(f"현재 가지고 있는 금액은 원화로 : {korea_won}원 입니다.")

