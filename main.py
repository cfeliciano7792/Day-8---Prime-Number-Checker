#Write your code below this line 👇


def prime_checker(number):
  is_prime = True
  while is_prime:
    for num in range(2, number + 1):
      if number % num == 0 and not num == number:
        is_prime = False
    print("Not a Prime")

  

    
      
        
    
    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



