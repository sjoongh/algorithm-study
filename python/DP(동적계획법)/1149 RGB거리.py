# 1. 각 셀은 현재 집을(R,G,B)로 칠했을때의 최소비용이다.
# 집2에 R을 칠하는 경우 = 집2를 R로 칠하는 비용 + min(집1을 G로 칠하는 경우, 집1을 B로 칠하는경우)
# 집2에 B을 칠하는 경우 = 집2를 B로 칠하는 비용 + min(집1을 G로 칠하는 경우, 집1을 R로 칠하는경우)
n = int(input()) # 집의 수
color = [list(map(int, input().split())) for _ in range(n)] # 각 집을 R,G,B로 칠하는 비용

for i in range(1,n):
    # 첫번째의 [0][0],[0][1],[0][2] 에는 각각 빨간, 초록, 파란색의 첫번째값을 넣어줌
    # -> 때문에 range(1)부터 start
    # 2번째 값부터는 연속된 색상을 가지면 안되므로
    # color[i][0] = 현재 빨간색집의 비용 +  min(이전 초록색집의 dp와 이전 파란색집의 dp 중)을 넣어준다
    color[i][0] = color[i][0]+min(color[i-1][1],color[i-1][2]) # 현재 i번째에서 0번째 색깔(red)을 고른 경우
    color[i][1] = color[i][1]+min(color[i-1][0],color[i-1][2]) # 현재 i번째에서 1번째 색깔(green)을 고른 경우
    color[i][2] = color[i][2]+min(color[i-1][0],color[i-1][1]) # 현재 i번째에서 2번째 색깔(blue)을 고른 경우

# 즉 n까지 집을 색칠했을때(종료) 순차적으로 쌓아온 값을 이용해 
# 각 집을 3가지 경우의 color로 색칠했을 때 min([i][0], [i][1], [i][2])값만을 출력
# 즉 for문이 돌아갈때마다 현재집을 칠할 수 있는 color 3가지의 모든 경우의 수를 고려해서 나온 min 결과가 정답이다.
print(min(color[n-1]))