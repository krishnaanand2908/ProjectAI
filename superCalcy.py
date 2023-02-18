import os
import fontstyle
import math

def infinity_add():
    os.system('cls')
    txtadd = fontstyle.apply(f'Enter a rational number:\n', 'cyan/bold')
    disclaimer = fontstyle.apply('You can only add 2 numbers at a time', 'red/bold')
    continuetxt = fontstyle.apply('Press ENTER to add another Rational Number', 'white/bold')
    program_finished = fontstyle.apply('Program sucessfuly closed', 'green/bold')
    num1 = float(input(txtadd))
    num2 = float(input(txtadd))
    os.system('cls')
    sumtxt = (num1 + num2)
    print(fontstyle.apply(f'{num1} + {num2} = {sumtxt}', 'yellow/bold'))
    while(True):
        choice = input(continuetxt)
        if choice == '':
            numx = float(input(txtadd))
            os.system('cls')
            print(disclaimer)
            print(fontstyle.apply(f'{sumtxt} + {numx} = {sumtxt+numx}\n', 'yellow/bold'))
            sumtxt = sumtxt + numx
            continue
        else:
            print(program_finished)
            break

def infinity_subtract():
    os.system('cls')
    txtsub = fontstyle.apply('Enter a rational number:\n', 'cyan/bold')
    continuetxt=fontstyle.apply('Press ENTER to add another Rational Number', 'white/bold')
    disclaimer=fontstyle.apply('You can only subtract 2 numbers at a time', 'red/bold')
    print(disclaimer)
    print(fontstyle.apply('Format: [First Number] - [Second Number]', 'red/bold/underline'))
    num1 = float(input(txtsub))
    num2 = float(input(txtsub))
    difftxt = (num1 - num2)
    print(fontstyle.apply(f'{num1} - {num2} = {difftxt}', 'yellow/bold'))
    while(True):
        choice = input(continuetxt)
        if choice == '':
            numx = float(input(txtsub))
            os.system('cls')
            print(disclaimer)
            print(fontstyle.apply('Format: [First Number] - [Second Number]', 'red/bold/underline'))
            print(fontstyle.apply(f'{difftxt} - {numx} = {difftxt-numx}\n', 'yellow/bold'))
            difftxt = difftxt - numx
            continue
        else:
            break
        
def infinity_multiply():
    os.system('cls')
    txtmulti = fontstyle.apply('Enter a rational number:\n', 'cyan/bold')
    continuetxt=fontstyle.apply('Press ENTER to multiply another Rational Number', 'white/bold')
    disclaimer=fontstyle.apply('You can only multiply 2 numbers at a time', 'red/bold')
    print(disclaimer)
    num1 = float(input(txtmulti))
    num2 = float(input(txtmulti))
    multitxt = (num1 * num2)
    print(fontstyle.apply(f'{num1} x {num2} = {multitxt}', 'yellow/bold'))
    while(True):
        choice = input(continuetxt)
        if choice == '':
            print(disclaimer)
            numx = float(input(txtmulti))
            os.system('cls')
            print(disclaimer)
            print(fontstyle.apply(f'{multitxt} x {numx} = {multitxt*numx}\n', 'yellow/bold'))
            multitxt = numx * multitxt
            continue
        else:
            break

def infinity_divide():
    os.system('cls')
    txtdiv = fontstyle.apply('Enter a rational number:\n', 'cyan/bold')
    continuetxt=fontstyle.apply('Press ENTER to divide another Rational Number', 'white/bold')
    disclaimer=fontstyle.apply('You can only divide 2 numbers at a time', 'red/bold')
    print(disclaimer)
    print(fontstyle.apply('Format: [First Number] / [Second Number]', 'blue/bold'))
    num1 = float(input(txtdiv))
    num2 = float(input(txtdiv))
    divtxt = (num1 / num2)
    print(fontstyle.apply(f'{num1} / {num2} = {divtxt}', 'yellow/bold'))
    while(True):
        choice = input(continuetxt)
        if choice == '':
            print(disclaimer)
            numx = float(input(txtdiv))
            os.system('cls')
            print(disclaimer)
            print(fontstyle.apply('Format: [First Number] / [Second Number]', 'blue/bold'))
            print(fontstyle.apply(f'{divtxt} / {numx} = {divtxt/numx}\n', 'yellow/bold'))
            divtxt = divtxt / numx
            continue
        else:
            break    

def factorial():
     while(True):
        os.system('cls')
        inp = int(input(fontstyle.apply('Enter the number of which you want the factorial:\n', 'cyan/bold')))
        fact = 1
        if inp < 0:
            print(fontstyle.apply('Plese ENTER a Whole Number!\nPress Enter to Continue!\n', 'red/bold/underline'))
            temp = input()
            continue
        else:
            for i in range (1, inp+1):
                fact = fact*i
            print(fontstyle.apply(f'{inp}! = {fact}', 'yellow/bold'))
            
        choice = input(fontstyle.apply('Press Enter to contine else press any key:\n', 'cyan/bold'))
        if choice == '':
            continue
        else:
            break
        
# def hcf():
#     txtgcd = fontstyle.apply('Enter a rational number:\n', 'cyan/bold')
#     continuetxt=fontstyle.apply('Press ENTER to input another Rational Number', 'purple/bold')
#     os.system('cls')
#     while(True):
#         a = int(input(txtgcd))
#         b = int(input(txtgcd))
#         if a > b:
#             smaller = b
#         else:
#             smaller = a
            
#         for i in range(1, smaller+1):
#             if a%i == 0 and b%i == 0:
#                 gcd = i
#         print(fontstyle.apply(f'HCF of {a} and {b} is {gcd}', 'yellow/bold'))


# def infinity_hcf():
#     while(True):
#         os.system('cls')
#         temp = input(fontstyle.apply('Press Enter to continue:\n', 'cyan'))
#         hcf()
#         choice = str(input(fontstyle.apply('Press Enter to continue else press any key to exit!\n')))
#         if choice == '':
#             print(fontstyle.apply('HCF program is re-runing...'))
#             continue
#         else:
#             break
                    


            
def advance_hcf2():  # hcf and gcd are same thing
    list1 = []  # Empty list to store all hcf elements
    os.system('cls')
    while True:
        element = input(fontstyle.apply(
            "Enter integer element or press Enter to display result: ", "cyan/bold"))
        if element == "":  # checks if user has entered "ENTER"
            break  # exit the while loop
        else:
            element = int(element)  # converting string element into integer
            list1.append(element)  # adding element to list

    temp_gcd = list1[0]  # assumed first element of list as gcd
    for i in list1:
        # comparing gcd with every element if list
        temp_gcd = math.gcd(temp_gcd, i)
        

    print(fontstyle.apply(f'Required HCF: {temp_gcd}', 'yellow/bold/underline'))
    
def advance_lcm2():
    list1 = []  # Empty list to store all hcf elements
    os.system('cls')
    while True:
        element = input(fontstyle.apply(
            "Enter integer element or press Enter to display result: ", 'cyan/bold'))
        if element == "":  # checks if user has entered "ENTER"
            break  # exit the while loop
        else:
            element = int(element)  # converting string element into integer
            list1.append(element)  # adding element to list

    temp_lcm = list1[0]  # assumed first element of list as lcm
    for i in list1:
        # comparing lcm with every element if list
        temp_lcm = math.lcm(temp_lcm, i)

    print(fontstyle.apply(f'Required LCM: {temp_lcm}', 'purple/bold/underline'))
    
def infinity_exponents():
    os.system('cls')
    txtexpo = fontstyle.apply('Enter base value:\n', 'cyan/bold')
    continuetxt=fontstyle.apply('Press Enter to assign the power value:\n', 'white/bold')
    num1 = float(input(txtexpo))
    num2 = float(input(txtexpo))
    expotxt = (num1 ** num2)
    print(fontstyle.apply(f'{num1} ^ {num2} = {expotxt}', 'yellow/bold'))
    while(True):
        choice = input(continuetxt)
        if choice == '':
            numx = float(input(txtexpo))
            os.system('cls')
            print(fontstyle.apply(f'{expotxt} ^ {numx} = {expotxt**numx}\n', 'yellow/bold'))
            expotxt = expotxt ** numx
            continue
        else:
            break
        
def table_loop():
    os.system('cls')
    while(True):
        number = float(input(fontstyle.apply('Enter a Rational number to generate its multiplication table:  ', 'purple/bold')))
        number_of_multiples = int(input(fontstyle.apply('Enter the number of multiples:  ', 'purple/bold'))) 
        for i in range(1, number_of_multiples+1):
            print(fontstyle.apply(f'{number} x {i} = {number * i}', 'yellow/bold/underline'))
        choice = input(fontstyle.apply('Press Enter to continue else press any key to exit!\n', 'green/bold'))
        if choice == '':
            continue
        else:
            break

def expotable():
    os.system('cls')
    while(True):
        base = float(input(fontstyle.apply('Enter the base value:  ', 'green/bold')))
        power = float(input(fontstyle.apply('Enter the power value:  ', 'green/bold')))
        items = int(input(fontstyle.apply('Enter the number of values you want:  ', 'green/bold')))
        
        try:
        
            for i in range(1, items):
                print(fontstyle.apply(f'{base} ^ {power} = {power ** base}', 'purple/bold/underline'))
                base = base ** power
        
        except OverflowError:
            print(fontstyle.apply('Can\'t continue to display!\nResults Too Large!!!!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', 'red/bold/underline'))
        
        choice = input(fontstyle.apply('Press Enter to continue else press any key to exit!\n', 'green/bold'))
        if choice == '':
            os.system('cls')
            print(fontstyle.apply('Re-running the program...\nRe-run Successful!', 'green'))
            continue
        else:
            break


def main_calcy():
    add = fontstyle.apply('1. Addition', 'blue/bold/underline')
    sub = fontstyle.apply('2. Subtraction', 'red/bold/underline')
    multi = fontstyle.apply('3. Multiplication', 'green/bold/underline')
    divi = fontstyle.apply('4. Division', 'white/bold/underline')
    expo = fontstyle.apply('5. Exponents', 'cyan/bold/underline')
    hcf = fontstyle.apply('6. HCF/GCD', 'purple/bold/underline')
    lcm = fontstyle.apply('7. LCM', 'yellow/bold/underline')
    factorial1 = fontstyle.apply('8. Factorial', 'red/bold/underline')
    table = fontstyle.apply('9. Multiplication Tables', 'red/bold/underline/italic')
    expotab = fontstyle.apply('10. Exponential Tables', 'blue/bold/underline/italic')
    txt1 = fontstyle.apply('Enter the number in front of the operation you which you want to use:', 'black/white_bg/bold')
    
    while(True):
        os.system('cls')
        print(fontstyle.apply(f'{txt1}\n{add}\n{sub}\n{multi}\n{divi}\n{expo}\n{hcf}\n{lcm}\n{factorial1}\n\n{table}\n{expotab}\n'))
        choice = int(input(fontstyle.apply('---> ', 'white/bold')))
        
        if choice == 1:
            infinity_add()
            continue
        elif choice == 2:
            infinity_subtract()
            continue
        elif choice == 3:
            infinity_multiply()
            continue
        elif choice == 4:
            infinity_divide()
            continue
        elif choice == 5:
            infinity_exponents()
            continue
        elif choice == 6:
            advance_hcf2()
            temp = input(fontstyle.apply('Press Enter to continue', 'green/bold'))
            continue
        elif choice == 7:
            advance_lcm2()
            temp = input(fontstyle.apply('Press Enter to continue', 'green/bold'))
            continue
        elif choice == 8:
            factorial()
            continue
        elif choice == 9:
            table_loop()
            continue
        elif choice == 10:
            expotable()
            continue
        else:
            break


