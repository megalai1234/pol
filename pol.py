number=int(raw_input("Enter a number"))
sum1=0
n=number
while number!=0:
	rem=number%10
	sum1=sum1*10+rem
	number=number/10
if sum1==n:
	print n, "is palindrome"
else:
	print n, "is not palindrome"
