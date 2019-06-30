N=int(input())
temp=N
pallindrome=0
while N!=0:
  number=N%10
  pallindrome=pallindrome*10+number
  N=N//10
if temp==pallindrome:
  print("yes")
else:
print("no")
