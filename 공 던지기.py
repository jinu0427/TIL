def solution(numbers, k):
    n = len(numbers) # 몇 명이 있는지
    index = (2 * (k - 1)) % n # (k-1): 던진 횟수, 2 * (k - 1): 이동한 칸 수, % len(numbers): 배열 길이 넘으면 다시 처음부터 돌기
    answer = numbers[index]  # numbers 배열에서 해당 위치의 사람 번호 반환
    return answer
print(solution([1, 2, 3, 4], 2))        # 출력: 3
print(solution([1, 2, 3, 4, 5, 6], 5))  # 출력: 3
print(solution([1, 2, 3], 3))           # 출력: 2