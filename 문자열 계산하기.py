def solution(my_string):
    answer = 0
    parts = my_string.split() # 문자열을 공백 기준으로 나눔 → ["3", "+", "4"] 이런 리스트가 됨
    answer = int(parts[0]) # 첫 번째 숫자를 answer에 넣어줌
    i = 1 # 연산자와 숫자는 번갈아 나오기 때문에 1부터 시작해서 2씩 증가시킴
    while i < len(parts):
        if parts[i] == "+": # "+"면 더해줌
            answer = answer + int(parts[i + 1])
        else:
            answer = answer - int(parts[i + 1]) # "-"면 빼줌
        i = i + 2 # 다음 연산자를 보기 위해 2칸 이동
    return answer
print(solution("3 + 4")) # 7
