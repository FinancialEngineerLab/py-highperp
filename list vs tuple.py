numbers = [5,1,6,7,122]
numbers[2] = 2 * numbers[0] # update !
numbers.append(222) # insert !

''' List의 append시 초과할당 문제 

N+1가 아닌 M (M>N) 만큼 할당한다! 
M = (N >> 3) + (3 if N < 9 else 6)

100,000,000 vs 112,500,007
10 * 1,000,000 vs 16,000,000

'''


''' Tuple은 할당과 복사가 추가할때마다 일어남 = 메모리 효율 
'''
