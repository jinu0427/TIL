def solution(n):
    answer = [] # 결과를 저장할 빈 리스트 만들기
    i = 2 # 2부터 나눠보기 시작
    while i <= n:
        if n % i == 0: # n이 i로 나누어 떨어지면
            if i not in answer:  # 이미 리스트에 없으면
                answer.append(i) # 리스트에 넣기
            n = n // i # n을 i로 나눠서 줄이기
        else:
            i = i + 1 # 안 나눠지면 i를 하나 키워서 다음 숫자 보기
    return answer
print(solution(12)) # [2, 3]
print(solution(17)) # [17]
print(solution(420)) # [2, 3, 5, 7]