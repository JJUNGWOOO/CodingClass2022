def num(k,n):
  if k==0 :
    return n
  else:
    result=0
    for i in range(1,n+1):
      result+=num(k-1,i)
    return result
k,n=map(int,input("층수 호수 써주세욧!!: ").split())
print(k,"층",n,"호에는",num(k,n),"명이 삽니다")


