#this program prints numbers from 1-100 and for multiples of 3 it prints Fizz, for 5 Buzz and for 3 and 5 FizzBuzz
def print_numbers():
	for i in range(1,101):
		if i%3==0 and i%5!=0:
			print("Fizz")
		elif i%3!=0 and i%5==0:
			print("Buzz")
		elif i%3==0 and i%5==0:
			print("FizzBuzz")
		else:
			print(i)

print_numbers()	
