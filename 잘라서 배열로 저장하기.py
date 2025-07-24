def solution(my_str, n):
    result = []  # 잘라서 넣을 빈 리스트 만들기
    for i in range(0, len(my_str), n): # 0부터 문자열 끝까지 n씩 증가하면서 자르기
        part = my_str[i:i+n] # i부터 i+n 전까지 자르기
        result.append(part) # 잘라낸 부분을 리스트에 추가
    return result
print(solution("abc1Addfggg4556b", 6)) # ['abc1Ad', 'dfggg4', '556b']
print(solution("abcdef123", 3)) # ['abc', 'def', '123']