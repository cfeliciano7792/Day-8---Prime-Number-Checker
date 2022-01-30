#Write your code below this line 👇


def prime_checker(number):
  is_prime = True
  if is_prime == True:
    for num in range(2, number):
      if number % num == 0:
        is_prime = False
        

  if is_prime == False:
    print("Not a prime")
  elif is_prime == True:
    print("Prime")  

    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



