a=int(input("국어 점수를 입력해주세요 : "))
b=int(input("수학 점수를 입력해주세요 : "))
c=int(input("영어 점수를 입력해주세요 : "))
d=int(input("한국사 점수를 입력해주세요 : "))

print("평균점수는 ",(a+b+c+d)/4,"입니다") 

if a<(a+b+c+d)/4 :
  print("국어점수가 평균보다",((a+b+c+d)/4)-a,"낮습니다. 분발하세요!")
if b<(a+b+c+d)/4 :
  print("수학점수가 평균보다",((a+b+c+d)/4)-b,"낮습니다. 분발하세요!")
if c<(a+b+c+d)/4 :
  print("영어점수가 평균보다",((a+b+c+d)/4)-b,"낮습니다. 분발하세요!")
if d<(a+b+c+d)/4 :
  print("한국사점수가 평균보다",((a+b+c+d)/4)-b,"낮습니다. 분발하세요!")
if a>b and a>c and a>d :
  print("국어를 제일 잘해요!")
elif b>c and b>d and b>a :
  print("수학을 제일 잘해요!")
elif c>d and c>a and c>b :
  print("영어를 제일 잘해요!")
elif d>a and d>b and d>c :
  print("한국사를 제일 잘해요!")