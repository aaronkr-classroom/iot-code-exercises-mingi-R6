1.
다음 내용을 하나의 조건식으로 만드세요.
  홀수 달의 15일 또는 짝수 달의 16일이면 "그날"을 출력함.
  8월 15일이면 "광복절"을 출력함.  
  그 외는 "평일"을 출력함.
  변수는 month와 day를 사용함.
if (month == 8 and day == 15):
    print("광복절")
elif (month % 2 == 1 and day == 15) or (month % 2 == 0 and day == 16):
    print("그날")
else:
    print("평일")

2.for 문을 이용해 1~50의 짝수 합을 구하되, 3의 배수는 제외하세요
total = 0

for i in range(1, 51):
    if not (i % 2 == 1 or i % 3 == 0):
        total += i

print(total)
print(total)
3.
연습문제 4.3을 while 문으로 해결하세요
total = 0
i = 1

while i <= 50:
    if not (i % 2 == 1 or i % 3 == 0):
        total += i
    i += 1

print(total)
