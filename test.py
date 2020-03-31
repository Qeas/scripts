def solution(A):
    if max(A) - min(A) + 1 != len(A):
        return 0
    delta = min(A)
    B = [0] * len(A)
    for a in A:
        if B[a - delta] > 0:
            return 0
        B[a - delta] = 1
    if sum(B) == len(A):
        return 1
    return 0


A = [2, 0]

print('solution ', solution(A))
