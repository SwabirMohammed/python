lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))
for i in range(lower, upper+1):
   if((i%3==0) & (i%5==0)):
      print("FizzBuzz")
   elif(i%3==0):
      print("Fizz")
   elif(i%5==0):
       print("Buzz")
   else:print("Not in Range")


