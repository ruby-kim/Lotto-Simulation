# random 모듈을 import해 주세요.
import random

# 1. 중복 없이 로또의 당첨 번호를 만듭니다.
lotto =[]
while True:
	num = random.randint(1, 45)
	if not num in lotto:
		lotto.append(num)
		if len(lotto) == 6:
			break

      
      
# 2. 사용자 입력으로 시뮬레이션을 위한 번호를 중복 없이 받습니다.
pick = []
display_num = 1
while True:
	num = int(input(str(display_num) + "번째 숫자를 입력해주세요: "))
	if not num in pick and 1 <= num <= 45:
		pick.append(num)
		display_num += 1
		if len(pick) == 6:
			break
	else:
		print("중복되지 않는 1~45 사이의 수를 입력해주세요!\n")



# 3. 랜덤으로 뽑은 번호와 입력받은 번호 사이에 일치한 번호의 개수를 확인합니다
cnt = 0
for num in lotto:
	if num in pick:
		cnt = cnt + 1



# 4. 몇 개가 일치했는지, 그리고 몇 등인지 출력해 주세요.
lotto.sort()
pick.sort()

print("로또 당첨 번호:", end="")
for i in range(6):
	print(lotto[i], end=" ")
print("")

print("입력한 번호  :", end="")
for i in range(6):
	print(pick[i], end=" ")
print("\n")

# 6개 -> 1등   ===> 7 - cnt로 값을 구할 수 있음
# 5개 -> 2등
# 4개 -> 3등
# 3개 -> 4등
# 2개 -> 5등

if cnt >= 2:
	print("총 " + str(cnt) + "개가 일치하므로 " + str(7 - cnt) + "등입니다")
else:
	print("총 " + str(cnt) + "개가 일치하므로 꽝입니다.")
