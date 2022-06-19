# 첫번째 정수로 다시 돌아오는 횟수
tmp = inp = int(input())
count=0

while True:
   ten = tmp//10
   one = tmp % 10
   res= ten + one
   count += 1
   tmp = int(str(tmp%10) + str(res%10))
#    -> 문자열로 합하고 다시 int형으로 변환
   if (inp==tmp):
       break
print(count)