"""
1. 아이디어
- 2중 for문, 값 1 && 방문 X => DFS
- DFS를 통해 찾은 값을 저장 후 정렬해서 출력

2. 시간복잡도
- DFS : O(V+E)
- V = n^2, E = 4N^2
- V+E = 5N^2 ~= N^2 ~= 625 < 2억 >> 사용 가능

3. 자료구조
- 그래프 저장 : int[][]
- 방문여부 : bool[][]
- 결과값 : int[][]
"""

import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
check = [[False]*N for _ in range(N)]
result = []
each = 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    global each # 전역변수로 바꿔주는 작업
    each += 1 # 연속된 크기 계산해야함
    
    for k in range(4): # 사방으로 다 봐야하니까
        ny = y + dy[k]
        nx = x + dx[k] 
        if 0<=ny<N and 0<=nx<N:
            if map[ny][nx] == 1 and check[ny][nx] == False:
                check[ny][nx] = True
                dfs(ny, nx)
                
                
for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and check[j][i] == False:
            check[j][i] = True # 방문체크 표시
            
            # DFS로 크기 구하기
                # BFS : 함수 호출, 리턴값으로 크기 받아왔음
                # DFS 재귀함수는 크기 받아오는게 어려움. => 전역변수 이용 (each=0)
            each = 0
            dfs(j,i)

            result.append(each) # 크기를 결과 리스트에 넣기

result.sort()
print(len(result))
for i in result: 
    print(i)
