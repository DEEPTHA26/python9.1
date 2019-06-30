num8=int(input())
if num8>1:
  for i in range(2,num8):
    if(num8%i)==0:
      print("no")
      break
    else:
      print("yes")
else:
  print("no")
