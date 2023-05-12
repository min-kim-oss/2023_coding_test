def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    student = [1 for i in range (n)]
    for i in (lost):
        student[i-1] = 0
    answer = 0
    for i in (reserve):
        if(student[i-1] == 0):
            student[i-1] = 1
        elif(i != 1 and student[i-2] == 0):
            student[i-2] = 1
        elif(i != n and student[i] == 0 and ((i+1) not in (reserve))):
            student[i] = 1
    for i in range(n):
        if (student[i] == 1):
            answer += 1
    return answer
