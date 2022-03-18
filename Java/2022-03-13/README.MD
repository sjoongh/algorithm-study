**복기 1.**
<br />**문제 : S(string)을 interval에 적힌 숫자에 따라 해당 인덱스를 변경하는 문제**

S : abcde
interval : [ [1,3], [1,4], [2,5] ]
interval에 따라서 S 문자열의 문자 위치 변경하는 알고리즘

- **해결방법**
1. startIdx와 endIdx변수를 활용해 해당 영역만 뽑아냄
2. S.substring()을 사용해 해당 영역만 changeString 메소드로 보내줌
3. changeStinrg()에서 toCharArray로 char형으로 변환후 문자열 switch (tip : 여기서 str.length() / 2 만큼만 switch && 애초에 변경하고 싶은 영역만 보냈음)
4. new String()으로 다시 str type으로 return
5. switch된 string과 선택되지 않은 start(string)나 end(string) 범위가 있을경우 더한다음 출력

**복기2.**
**문제 : 로봇이 빠져나올 수 있는 출발점의 개수를 출력**

P : "<<<><"
로봇은 위 블록의 아무곳이나 들어갈 수 있음
>< 같이 겹치는 영역을 만나면 빠져나올 수 없음
그러므로 <<< 같이 빠져나올 수 있는 출발점의 개수를 count(start, end)
<img src="https://user-images.githubusercontent.com/77228818/158925626-db83fbcf-5077-4e03-ae8d-a63ba712ce3d.png" />

- **해결방법**
1. 시작점(left) --> 빠져나오는 영역의 마지막부터 계산 <만 계산하면 되므로 >가 나오면 break
2. 끝점(right) --> 시작점과 반대로 출력
3. 시작점+끝점으로 빠져나올수 있는 개수를 모두 count

**복기 3.**

**문제 : 금액이 순서대로 들어있는 배열이 존재, 주어진 항목 중에서 k개 이상의 항목을 선택하여 새 보험상품 만듬
배열[2,5,3,8,1], k = 3, t = 11이 주어진 경우, 3개 이상의 항목을 선택하는 방법은 총 16가지가 존재함
이 중 선택된 항목들의 보장 금액의 합이 11이하가 되는 경우는 6가지가 존재한다.
항목별 보장금액이 순서대로 들어있는 배열 arr과 k,t가 매개변수일때, arr에서 k개 이상의 항목을 선택했을 때 금액 합이 t이하가 되는 경우의 수** 
<img src="https://user-images.githubusercontent.com/77228818/158925634-faba9c66-5387-4f37-a5d1-4a8c5f9575e8.png" />
<img src="https://user-images.githubusercontent.com/77228818/158926597-5191691c-3a57-4a82-8229-3e8b3725e4f8.png" />
<img src="https://user-images.githubusercontent.com/77228818/158925643-33ede8c9-96d1-4388-94a2-978996c22d9b.png" />

- **해결방법**
idx : idx로 인덱스 위치를 옮겨가며 level과 sum의 조건을 만족시킴
level : 재귀함수를 끝내기 위함, level == arr.length가 될 경우 탐색이 종료되었으므로 return
sum : sum한 값이 t(합)이하의 수가 되는 것을 확인하기 위함

idx는 모든 경우를 탐색해야 하므로 i+1(재귀)
level : 재귀로 들어간 함수(idx)가 종료된것을 구분하기 위해 level + 1
sum : idx가 탐색할때마다 경우의 수를 계산

**복기 4.**

**문제 : int[] arr로 주어진 숫자 중 k만큼 선택해 연속된 배열의 값 중 가장 높은 영역의 합계를 출력**

- **해결방법**
1. k와 int[]arr의 길이가 같은 경우를 생각해 반복문으로 k의 길이만큼 arr[]을 더해준다.
2. max = sum에 대입 후 반복문을 사용 해 arr.length만큼 돌림
3. 오른쪽으로 한칸씩 자리를 옮겨가며 연속된 배열의 k만큼의 영역에서 가장 큰 영역을 뽑아낸다.
4. sum -= arr[lt++] --> 오른쪽으로 이동시 가장 왼쪽의 배열값을 빼내기 위함
5. sum += arr[rt++] --> 오른쪽으로 이동시 오른쪽 값을 더해주기 위함
6. sum > max가 될 경우에만 max값에 다시 넣어준다.
7. 2번의 반복문이 종료되면 가장 큰 영역이 max에 남아있으므로 return 해준다.

**복기 5.**

**문제 :
gold_prices : [2,5,1,3,4]
result : 4
금 한 돈의 시세가 [2,4,1,3,4]일 때 최대 이익을 구하시오
이익이 발생하지 않으면 팔지 않아도 되며 sell을 한 다음날은 buy할 수 없습니다.**

<img src ="https://user-images.githubusercontent.com/77228818/158925648-20e08570-f70f-4d5f-bb04-f35d3529abe4.png" />
<img src ="https://user-images.githubusercontent.com/77228818/158925649-ce707c1f-0b22-4166-bde8-08c19a2e4b5e.png" />

- **해결방법(TODO)**

**복기 6.**

**문제 : 사칙연산**

<img src="https://user-images.githubusercontent.com/77228818/158925651-dae077a8-f606-4d2a-beff-5961f0e8d4ed.png" />
<img src="https://user-images.githubusercontent.com/77228818/158925654-5a384669-4d02-4cf0-8452-4357cfe72c7c.png" />

