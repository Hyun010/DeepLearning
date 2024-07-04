def exchange_dollar_to_won(dollar, exchange_rate=1100):
    won = int(dollar * exchange_rate)
    return won

exchange_rate = 1200
dollar_in_account = 4.5

won_in_account = exchange_dollar_to_won(dollar_in_account)

print(f"{dollar_in_account} 달러는 현재 {won_in_account}원 입니다.")

won_in_account = exchange_dollar_to_won(dollar_in_account, exchange_rate)

print(f"{dollar_in_account} 달러는 현재 {won_in_account}원 입니다.")

def exchange_won_to_dollar(won, exchange_rate=1100):
    dollar = won / exchange_rate
    return dollar

dollar_in_account = exchange_won_to_dollar(won_in_account, exchange_rate)

print(dollar_in_account)