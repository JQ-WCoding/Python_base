# 값 넣기 예시
a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'jun'
a[4] = [1, 2, 3]
print(a)

del a['name']
print(a)

# dict_keys -> 객체로 반환 메모리 낭비를 줄이기 위해서 리스트로 변환과정을 생략
print(a.keys())
# 리스트로 필요한 경우 list 함수를 사용하여 변환 시켜주는 작업이 필요하다 파이썬 3.0 이후 부터
print(list(a.keys()))
print(a)

# values 는 dict_items 객체를 보내줌
print(a.values())
print(list(a.values()))

# key value 쌍으로 얻기 -> 튜플로 묶어서 나온다
print(a.items())
print(list(a.items()))

# 전부 삭제
a.clear()
print(a)
