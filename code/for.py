ktx_station_list = ["서울", "대전", "동대구", "부산"]

idx = 0
while idx < len(ktx_station_list):
    print(f"이번 정차역은 {ktx_station_list[idx]}입니다.")
    idx = idx + 1

for this_station in ktx_station_list:
    print(f"이번 정차역은 {this_station}입니다.")
