# check whether the number is odd or even, without using funtion calling
num = int(input("Enter a number :"))
if num>=1 :
  if num % 2 == 0 :
     print("{} is even :".format(num))
  else :
     print("{} is odd :".format(num))
else :
      print("{} is neither even nor odd".format(num))
   
