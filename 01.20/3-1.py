n=int(input())

if(n<2):
    print("소수가 아니다")
else:
  for i in range(2,n):
    if(n%i==0):
      print("소수가 아니다")
      quit()

      
print("소수이다")