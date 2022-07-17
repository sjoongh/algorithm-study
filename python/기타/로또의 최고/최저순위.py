# 로또의 최고 순위와 최저 순위
# x가 산 로또에서 알아볼수 없는 숫자는 0으로구분
# 이 중에서 x가 최고 순위를 받는 경우와 최소 순위를 받는 경우 2가지 구하기
# 비트연산자 & : {0,0} = {0}, {1,1} = {1}, {0,1} = {0}, {0,1} = {0} 이 되는 연산자
# set & set을 하면 중복값만 추출됨 -> 중복값이 없다면 0
def solution(lottos, win_nums):
    # set : 중복을 허용하지 않음, 순서가 없음
    # lottos와 win_nums를 set으로 묶어 중복되는 수를 없앰
    # {44,1,0,31,25} & {31,10,45,1,6,19}-> &연산자로 중복값 추출 {1, 31} -> cnt=2
    cnt = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)  # 0이있으면 count
    # cnt+zero와 cnt가 0이 될 경우 1로 바꿈
    return [7-max(cnt+zero, 1), 7-max(cnt, 1)]
