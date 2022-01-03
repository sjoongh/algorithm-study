import sys
from collections import Counter

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
 
# 산술평균 - 다 더해서 / n
print(round(sum(li)/n))
 
# 중앙값 - 오름차순 -> 중간값
li.sort()
print(li[n//2])
 
# 최빈값 - 빈출
# Counter라이브러리를 사용해 개수 체크
# colors = Counter(['blue', 'green', 'red', 'blue','red','blue'])
# print(colors) --> Counter({'blue': 3, 'red': 2, 'green': 1})
# print(colors.most_common()) --> [('red', 3), ('blue', 2), ('green', 1)]
# Counter(리스트).most_common()은 Counter가 많은 순서대로 정렬
# most_common(2)를 할 경우 가장많은 것 부터 2개 출력
cnt_li = Counter(li).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]: #최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])
 
# 범위 - 최댓값-최솟값
print(max(li)-min(li))