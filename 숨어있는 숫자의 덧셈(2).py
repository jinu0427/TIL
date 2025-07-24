def solution(my_string):
    temp = '' # 숫자를 모아둘 공간
    answer = 0 # 숫자들의 합을 저장할 변수
    for one in my_string: # 문자열을 한 글자씩 꺼내서
        if one.isdigit(): # 그 글자가 숫자라면
            temp += one # temp에 계속 이어붙이기
        else: # 숫자가 아닌 다른 글자라면
            if temp != '': # temp에 숫자가 들어있으면
                answer += int(temp) # 숫자로 바꿔서 더해주고
                temp = '' # temp는 다시 비워주기
    if temp != '': # 문자열이 끝나고도 숫자가 남아있을 수 있으니까
        answer += int(temp) # 마지막 숫자도 더해주기
    return answer # 결과 반환
print(solution("aAb1B2cC34oOp"))  # 출력: 37
print(solution("1a2b3c4d123Z"))  # 출력: 133