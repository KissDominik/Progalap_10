from math import gcd

def masik_legnagyobbkozos():
    nem_ugyan_az_a_valtozo1 = open("szamok.txt","r")
    nem_ugyan_az_a_valtozo2 = nem_ugyan_az_a_valtozo1.readline()
    nem_ugyan_az_a_valtozo2 = nem_ugyan_az_a_valtozo2.strip().split()
    nem_ugyan_az_a_valtozo3 = []
    for i in range(len(nem_ugyan_az_a_valtozo2)):
        nem_ugyan_az_a_valtozo3.append(int(nem_ugyan_az_a_valtozo2[i]))
    print(nem_ugyan_az_a_valtozo3)
    
    nem_ugyan_az_a_valtozo4 = 0
    for i in range(len(nem_ugyan_az_a_valtozo3)-1):
        
        nem_ugyan_az_a_valtozo5go = gcd(nem_ugyan_az_a_valtozo3[i],nem_ugyan_az_a_valtozo3[i+1])
        if nem_ugyan_az_a_valtozo5go > nem_ugyan_az_a_valtozo4:
            nem_ugyan_az_a_valtozo4 = nem_ugyan_az_a_valtozo5go
    print(nem_ugyan_az_a_valtozo4)


def is_prime(nem_ugyan_az_a_valtozo8):
    
    nem_ugyan_az_a_valtozo6 = True
    nem_ugyan_az_a_valtozo7 = 2
    while nem_ugyan_az_a_valtozo7 <= nem_ugyan_az_a_valtozo8 // 2 and nem_ugyan_az_a_valtozo6:
        if nem_ugyan_az_a_valtozo8 % nem_ugyan_az_a_valtozo7 == 0:
            nem_ugyan_az_a_valtozo6 = False
        else:
            nem_ugyan_az_a_valtozo7 =+ 1 
    return nem_ugyan_az_a_valtozo6

    

def main():
    # a = int(input("Kérem, adjon meg egy egész számot: "))
    # if is_prime(a):
    #     print("prím szám.")
    # else:
    #     print("nem prím szám.")

    # number = 0
    # while not (100 <= number <= 1000):
    #     number = int(input("Kérem, adjon meg egy számot [100, 1000] között: "))
    # print_prime_factorization(number)
    masik_legnagyobbkozos()




# Függvény meghívása és eredmény kiíratása


# Feladat 2
def factorize(number):
    factors = []
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            factors.append(divisor)
            number /= divisor
        else:
            divisor += 1
    return factors

# Feladat 2.a
def print_prime_factorization(number):
    factors = factorize(number)
    print(f"A(z) {number} prímtényezős felbontása:")
    for factor in factors:
        print(factor)
    


main()