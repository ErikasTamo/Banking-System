import colorama
from colorama import Fore
import os
import time
import random

colorama.init(autoreset=True)

def main():
    os.system('cls')
    print('''
 1. Log In
 2. Register
        ''')
    choice = input("Enter Choice: ")
    if choice == '1':
        os.system('cls')
        validate()
    elif choice == '2':
        os.system('cls')
        register()
    else:
        print()
        print(f'{Fore.RED}Incorrect Option')
        time.sleep(2)
        os.system('cls')
        main()

def validate():
    e = input("Enter your Username: ")
    p = input("Enter your password: ")

    if e == 'admin' and p == 'root':
        count = 0
        run = True
        letter = "qwertyuiopasdfghjklzxcvbnm"
        numbers = "1234567890"
        while(run):
            for i in range(53):
                print(f"{Fore.GREEN}{random.choice(letter)}{random.choice(letter)}{random.choice(letter)}{random.choice(letter)}{random.choice(letter)}{random.choice(letter)}{random.choice(letter)}{random.choice(letter)}{random.choice(letter)}{random.choice(letter)}{random.choice(letter)}{random.choice(letter)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}")
            time.sleep(0.05)
            #os.system('cls')
            count += 1
            if count == 500:
                exit()

    f = open(f"{e}.txt", 'r')

    for line in f:
        entityList = line.split(',')
        if e == entityList[0] and p  ==  entityList[1]:
            time.sleep(2)
            os.system('cls')
            options(entityList[0])
            
def register():
    e = input("Enter Username: ")
    p = input("Enter Password: ")
    cp = input("Confirm Password: ")

    if p == cp:
        f = open(f'{e}.txt' , 'w')
        f.write(f'{e},{p},500') 
        f.close()
        time.sleep(3)
        os.system('cls')
        validate()
    else:
        print("Passwords dont Mach")

def options(name):
    print(f"Hello {name}")
    print('''
 1. Withdraw
 2. Deposit
 3. Check
 4. Exit
        ''')
    choice = input("Enter Choice: ")
    if choice == '1':
        withdraw(name)
    elif choice == '2':
        deposit(name)
    if choice == '3':
        balance(name)
    elif choice == '4':
        time.sleep(1)
        os.system('cls')
        exit()

def deposit(name):
    print()
    f = open(f'{name}.txt', 'r')

    amount = int(input('Enter the amount you want to deposit: '))
    for line in f:
        entityList = line.split(',')
        e = entityList[0]
        p = entityList[1]
        b = entityList[2]
    f.close()
    f = open(f'{name}.txt', 'w')
    newB = amount + int(b)
    f.write(f'{e},{p},{newB}')
    print(f"New Balance: {newB}$")
    f.close()
    print()
    input("Press ENTER to continue")
    os.system('cls')
    options(name)

def withdraw(name):
    print()
    f = open(f'{name}.txt', 'r')

    amount = int(input('Enter the amount you want to withdraw: '))
    for line in f:
        entityList = line.split(',')
        e = entityList[0]
        p = entityList[1]
        b = entityList[2]
    f.close()
    f = open(f'{name}.txt', 'w')
    newB = int(b) - amount
    f.write(f'{e},{p},{newB}')
    print(f"New Balance: {newB}$")
    f.close()
    print()
    input("Press ENTER to continue")
    os.system('cls')
    options(name)

def balance(name):
    print()
    f = open(f'{name}.txt', 'r')
    for line in f:
        entityList = line.split(',')
        b = entityList[2]
    bb = b
    print(f"Your current Balance: {bb}$")
    print()
    input("Press ENTER to continue")
    os.system('cls')
    options(name)

main()
