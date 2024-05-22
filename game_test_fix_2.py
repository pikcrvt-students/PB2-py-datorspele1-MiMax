import time
import sys
import os

x_git_print_python_span = '''  
       _ _ _   _ _ _
       | g |   | s |
       | i |   | p |
 - - - - - - - | a |
 | p | y t h o | n |
 | r | - - - - - - -
 | i |
 | n |
 | t |
 - - -

 '''
x0 = '''
       _ _ _   _ _ _
       | 2 |   | 3 |
       |   |   |   |
 - - - - - - - |   |
 | 1 |         |   |
 |   | - - - - - - -
 |   |
 |   |
 |   |
 - - -


'''
x_git = '''
       _ _ _   _ _ _
       | g |   | 3 |
       | i |   |   |
 - - - - - - - |   |
 | 1 |   t     |   |
 |   | - - - - - - -
 |   |
 |   |
 |   |
 - - -


'''
x_git_print = '''
       _ _ _   _ _ _
       | g |   | 3 |
       | i |   |   |
 - - - - - - - |   |
 | p |   t     |   |
 | r | - - - - - - -
 | i |
 | n |
 | t |
 - - -


'''
x_git_print_span = '''
       _ _ _   _ _ _
       | g |   | s |
       | i |   | p |
 - - - - - - - | a |
 | p |   t     | n |
 | r | - - - - - - -
 | i |
 | n |
 | t |
 - - -


'''
x_git_print_python = '''
       _ _ _   _ _ _
       | g |   | 3 |
       | i |   |   |
 - - - - - - - |   |
 | p | y t h o | n |
 | r | - - - - - - -
 | i |
 | n |
 | t |
 - - -


'''
x_git_python = '''
       _ _ _   _ _ _
       | g |   | 3 |
       | i |   |   |
 - - - - - - - |   |
 | p | y t h o | n |
 |   | - - - - - - -
 |   |
 |   |
 |   |
 - - -


'''
x_git_python_span = '''
       _ _ _   _ _ _
       | g |   | s |
       | i |   | p |
 - - - - - - - | a |
 | p | y t h o | n |
 |   | - - - - - - -
 |   |
 |   |
 |   |
 - - -


'''
x_git_span = '''
       _ _ _   _ _ _
       | g |   | s |
       | i |   | p |
 - - - - - - - | a |
 | 1 |   t     | n |
 |   | - - - - - - -
 |   |
 |   |
 |   |
 - - -


'''
x_python = '''
       _ _ _   _ _ _
       | 2 |   | 3 |
       |   |   |   |
 - - - - - - - |   |
 | p | y t h o | n |
 |   | - - - - - - -
 |   |
 |   |
 |   |
 - - -
               

'''
x_python_span = '''
       _ _ _   _ _ _
       | 2 |   | s |
       |   |   | p |
 - - - - - - - | a |
 | p | y t h o | n |
 |   | - - - - - - -
 |   |
 |   |
 |   |
 - - -
              

'''
x_python_span_print = '''
       _ _ _   _ _ _
       | 2 |   | s |
       |   |   | p |
 - - - - - - - | a |
 | p | y t h o | n |
 | r | - - - - - - -
 | i |
 | n |
 | t |
 - - -
               

'''
x_python_print = '''
       _ _ _   _ _ _
       | 2 |   | 3 |
       |   |   |   |
 - - - - - - - |   |
 | p | y t h o | n |
 | r | - - - - - - -
 | i |
 | n |
 | t |
 - - -
               

'''
x_print = '''
       _ _ _   _ _ _
       | 2 |   | 3 |
       |   |   |   |
 - - - - - - - |   |
 | p |         |   |
 | r | - - - - - - -
 | i |
 | n |
 | t |
 - - -
               

'''
x_print_span = '''
       _ _ _   _ _ _
       | 2 |   | s |
       |   |   | p |
 - - - - - - - | a |
 | p |         | n |
 | r | - - - - - - -
 | i |
 | n |
 | t |
 - - -
               

'''
x_span = '''
       _ _ _   _ _ _
       | 2 |   | s |
       |   |   | p |
 - - - - - - - | a |
 | 1 |         | n |
 |   | - - - - - - -
 |   |
 |   |
 |   |
 - - -
               

'''
Jautajumi = '''1 (vertikāli) (5 burti) Kura Python funkcija tiek izmantota, lai attēlotu tekstu uz ekrāna?
1 (horizontāli) (5 burti) Kāda programmēšanas valoda tiek izmantota Django projektā?
2 (3 burti) Kura versiju kontroles sistēma tiek plaši izmantota, lai pārvaldītu un izsekotu izmaiņas kodā? 
3 (4 burti) Programmēšanas valoda, kas paredzēta Parrot virtuālajai mašīnai.'''
Jautajums_print = '''1 (vertikāli) (5 burti) Kura Python funkcija tiek izmantota, lai attēlotu tekstu uz ekrāna?'''
Jautajums_python= '''1 (horizontāli) (5 burti) Kāda programmēšanas valoda tiek izmantota Django projektā?'''
Jautajums_git = '''2 (3 burti) Kura versiju kontroles sistēma tiek plaši izmantota, lai pārvaldītu un izsekotu izmaiņas kodā? '''
Jautajums_span = '''3 (4 burti) Programmēšanas valoda, kas paredzēta Parrot virtuālajai mašīnai.'''

def game_start():
    global atbildes
    global Kludu_skaits
    Kludu_skaits = 5
    for i in range(4):
        atbildes[i] = 0
    os.system("cls")
    print(atbildes)
    print(x0, "Sveicināti! Šodien jūs risināsiet krustvārdu mīklu, novēlu jums veiksmi un nepieļaujiet kļūdas :)")
    print ("Jums palika", Kludu_skaits,"kļūdas")
    time.sleep(3)
    print(Jautajums_print)
    time.sleep(1)
    print(Jautajums_python)
    time.sleep(1)
    print(Jautajums_git)
    time.sleep(1)
    print(Jautajums_span)
    
def printPicture(xH): 
    os.system("cls") 
    print(atbildes)
    print(xH) 
    print(Jautajumi)

atbildes = [0]*4

def ievade_atbilde_parbauda():
    if ievade == "git":
        if atbildes[0] == 1:
            print("Jūs jau ievadījāt šo atbildi!")
            ievade_code()
        else:  
            atbildes[0] = 1
    elif ievade == "python":
        if atbildes[1] == 1:
            print("Jūs jau ievadījāt šo atbildi!")
            ievade_code()
        else:  
            atbildes[1] = 1   
    elif ievade == "print":
        if atbildes[2] == 1:
            print("Jūs jau ievadījāt šo atbildi!")
            ievade_code()
        else:  
            atbildes[2] = 1
    elif ievade == "span":
        if atbildes[3] == 1:
            print("Jūs jau ievadījāt šo atbildi!")
            ievade_code()
        else:  
            atbildes[3] = 1

def ievade_code():
    global ievade
    global Kludu_skaits
    print("Ievadiet atbildi: ", end="")
    ievade = input("")
    ievade_atbilde_parbauda()
    while ievade != "git" and ievade != "python" and ievade != "span" and ievade != "print":
        print()
        print("Nepareizi!")
        Kludu_skaits -= 1
        print("Jums palika", Kludu_skaits,"kļūdas")
        if Kludu_skaits == 0:
            print("LOSE")
            time.sleep(1)
            sys.exit()
        ievade = input("")
        ievade_atbilde_parbauda()
    
def game_basic():
    ievade_code()
    if ievade == "git":
        printPicture(x_git)
        ievade_code()
        if ievade == "print":
            printPicture(x_git_print)
            ievade_code()
            if ievade == "span":
                printPicture(x_git_print_span)
            if ievade == "python":
                printPicture(x_git_print_python)
            ievade_code()
            if ievade == "python":
                printPictirefinal(x_git_print_python_span)
            elif ievade == "span":
                printPictirefinal(x_git_print_python_span)
        if ievade == "python":
            printPicture(x_git_python)
            ievade_code()
            if ievade == "span":
                printPicture(x_git_python_span)
            elif ievade == "print":
                printPicture(x_git_print_python)
            ievade_code()
            if ievade == "print":
                printPictirefinal(x_git_print_python_span)
            elif ievade == "span":
                printPictirefinal(x_git_print_python_span)
        if ievade == "span":
            printPicture(x_git_span)
            ievade_code()
            if ievade == "print":
                printPicture(x_git_print_span)
            elif ievade == "python":
                printPicture(x_git_python_span)
            ievade_code()
            if ievade == "print":
                printPictirefinal(x_git_print_python_span)
            elif ievade == "python":
                printPictirefinal(x_git_print_python_span)
    if ievade == "python":
        printPicture(x_python)
        ievade_code()
        if ievade == "git":
            printPicture(x_git_python)
            ievade_code()
            if ievade == "span":
                printPicture(x_git_python_span)
            elif ievade == "print":
                printPicture(x_git_print_python)
            ievade_code()
            if ievade == "span":
                printPictirefinal(x_git_print_python_span)
            elif ievade == "print":
                print(x_git_print_python_span)
        if ievade == "span":
            printPicture(x_python_span)
            ievade_code()
            if ievade == "git":
                printPicture(x_git_python_span)
            elif ievade == "print":
                printPicture(x_python_span_print)
            ievade_code()
            if ievade == "git":
                printPictirefinal(x_git_print_python_span)
            elif ievade == "print":
                printPictirefinal(x_git_print_python_span)
        if ievade == "print":
            printPicture(x_python_print)
            ievade_code()
            if ievade == "span":
                printPicture(x_python_span_print)
            elif ievade == "git":
                printPicture(x_git_print_python)
            ievade_code()
            if ievade == "git":
                printPictirefinal(x_git_print_python_span)
            elif ievade == "span":
                printPictirefinal(x_git_print_python_span)
    if ievade == "print":
        printPicture(x_print)
        ievade_code()
        if ievade == "git":
            printPicture(x_git_print)
            ievade_code()
            if ievade == "span":
                printPicture(x_git_print_span)
            elif ievade == "python":
                printPicture(x_git_print_python)
            ievade_code()
            if ievade == "span":
                printPictirefinal(x_git_print_python_span)
            elif ievade == "python":
                printPictirefinal(x_git_print_python_span)
        if ievade == "span":
            printPicture(x_print_span)
            ievade_code()
            if ievade == "git":
                printPicture(x_git_print_span)
            elif ievade == "python":
                printPicture(x_python_span_print)
            ievade_code()
            if ievade == "git":
                printPictirefinal(x_git_print_python_span)
            elif ievade == "python":
                printPictirefinal(x_git_print_python_span)
        if ievade == "python":
            printPicture(x_python_print)
            ievade_code()
            if ievade == "span":
                printPicture(x_python_span_print)
            elif ievade == "git":
                printPicture(x_git_print_python)
            ievade_code()
            if ievade == "git":
                printPictirefinal(x_git_print_python_span)
            elif ievade == "span":
                printPictirefinal(x_git_print_python_span)
    if ievade == "span":
        printPicture(x_span)
        ievade_code()
        if ievade == "git":
            printPicture(x_git_span)
            ievade_code()
            if ievade == "print":
                printPicture(x_git_print_span)
            elif ievade == "python":
                printPicture(x_git_python_span)
            ievade_code()
            if ievade == "print":
                printPictirefinal(x_git_print_python_span)
            elif ievade == "python":
                printPictirefinal(x_git_print_python_span)
        if ievade == "print":
            printPicture(x_print_span)
            ievade_code()
            if ievade == "git":
                printPicture(x_git_print_span)
            elif ievade == "python":
                printPicture(x_python_span_print)
            ievade_code()
            if ievade == "git":
                printPictirefinal(x_git_print_python_span)
            elif ievade == "python":
                printPictirefinal(x_git_print_python_span)
        if ievade == "python":
            printPicture(x_python_span)
            ievade_code()
            if ievade == "print":
                printPicture(x_python_span_print)
            elif ievade == "git":
                printPicture(x_git_python_span)
            ievade_code()
            if ievade == "git":
                printPictirefinal(x_git_print_python_span)
            elif ievade == "print":
                printPictirefinal(x_git_print_python_span)

def printPictirefinal(xH):
    os.system("cls")
    print(xH)
    print("Apsveicu!")
    end_time = time.time()
    result_time = round(end_time - start_time, 3)
    laika_saraksts.append(result_time)
    print("Jūsu laiks:", result_time, "sekundes")
    nakamais_meginajums()

laika_saraksts = [0]

def nakamais_meginajums():
    print("Vai gribat uzlabot savu rezultātu? (Y/N)")    
    ievade = input()
    if ievade == "Y" or ievade == "y":
        global start_time
        game_start()
        start_time = time.time()
        game_basic()
        nakamais_meginajums()
    else:
        del(laika_saraksts[0])
        elementu_skaits = len(laika_saraksts)
        mazakais_skaitlis = laika_saraksts[0]
        for num in range(1, elementu_skaits):
            if laika_saraksts[num] < mazakais_skaitlis:
                mazakais_skaitlis = laika_saraksts[num]
        print("Jūsu rezultati: ", laika_saraksts)
        print("Jūsu labakais laiks:", mazakais_skaitlis, "sekundes")
        print("Paldies par spelešanu!")
        sys.exit()
        
game_start()
start_time = time.time()
game_basic()
nakamais_meginajums()