def solution(M, N):
    total_pieces = M * N     
    cuts = total_pieces - 1  
    return cuts

print(solution(2, 2))  # 출력: 3
print(solution(2, 5))  # 출력: 9
print(solution(1, 1))  # 출력: 0