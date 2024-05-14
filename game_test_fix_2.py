import time
import sys
import os


x_final = '''  
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
Jautajumi = '''1 (vertikali) (5 burti) Kura Python funkcija tiek izmantota, lai attēlotu tekstu uz ekrāna?
1 (horizontali) (5 burti) Kāda programmēšanas valoda tiek izmantota Django projektā?
2 (3 burti) Kura versiju kontroles sistēma tiek plaši izmantota, lai pārvaldītu un izsekotu izmaiņas kodā? 
3 (4 vurti) Programmēšanas valoda, kas paredzēta Parrot virtuālajai mašīnai.'''
Jautajums_print = '''1 (vertikali) (5 burti) Kura Python funkcija tiek izmantota, lai attēlotu tekstu uz ekrāna?'''
Jautajums_python= '''1 (horizontali) (5 burti) Kāda programmēšanas valoda tiek izmantota Django projektā?'''
Jautajums_git = '''2 (3 burti) Kura versiju kontroles sistēma tiek plaši izmantota, lai pārvaldītu un izsekotu izmaiņas kodā? '''
Jautajums_span = '''3 (4 vurti) Programmēšanas valoda, kas paredzēta Parrot virtuālajai mašīnai.'''

def game_start():
    global Kļudu_skaits
    Kļudu_skaits = 5
    os.system("cls")
    print(x0, "Sveicinati! Šodien jūs risināsiet krustvārdu mīklu, novēlu jums veiksmi un nepieļaujiet kļūdas :)")
    print ("Jums palika", Kļudu_skaits,"kļudas")
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
    print(xH) 
    print(Jautajumi)

def ievade_code():
    global ievade
    global Kļudu_skaits
    print("Ievadiet atbildi: ", end="")
    ievade = input("")
    while ievade != "git" and ievade != "python" and ievade != "span" and ievade != "print":
        print()
        print("Nepareizi!")
        Kļudu_skaits -= 1
        print("Jums palika", Kļudu_skaits,"kļudas")
        if Kļudu_skaits == 0:
            print("LOSE")
            time.sleep(1)
            sys.exit()
        ievade = input("")
    
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
            elif ievade == "python":
                printPicture(x_git_print_python)
            ievade_code()
            if ievade == "python":
                printPictirefinal(x_final)
            elif ievade == "span":
                printPictirefinal(x_final)
        if ievade == "python":
            printPicture(x_git_python)
            ievade_code()
            if ievade == "span":
                printPicture(x_git_python_span)
            elif ievade == "print":
                printPicture(x_git_print_python)
            ievade_code()
            if ievade == "print":
                printPictirefinal(x_final)
            elif ievade == "span":
                printPictirefinal(x_final)
        if ievade == "span":
            printPicture(x_git_span)
            ievade_code()
            if ievade == "print":
                printPicture(x_git_print_span)
            elif ievade == "python":
                printPicture(x_git_python_span)
            ievade_code()
            if ievade == "print":
                printPictirefinal(x_final)
            elif ievade == "python":
                printPictirefinal(x_final)
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
                printPictirefinal(x_final)
            elif ievade == "print":
                print(x_final)
        if ievade == "span":
            printPicture(x_python_span)
            ievade_code()
            if ievade == "git":
                printPicture(x_git_python_span)
            elif ievade == "print":
                printPicture(x_python_span_print)
            ievade_code()
            if ievade == "git":
                printPictirefinal(x_final)
            elif ievade == "print":
                printPictirefinal(x_final)
        if ievade == "print":
            printPicture(x_python_print)
            ievade_code()
            if ievade == "span":
                printPicture(x_python_span_print)
            elif ievade == "git":
                printPicture(x_git_print_python)
            ievade_code()
            if ievade == "git":
                printPictirefinal(x_final)
            elif ievade == "span":
                printPictirefinal(x_final)
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
                printPictirefinal(x_final)
            elif ievade == "python":
                printPictirefinal(x_final)
        if ievade == "span":
            printPicture(x_print_span)
            ievade_code()
            if ievade == "git":
                printPicture(x_git_print_span)
            elif ievade == "python":
                printPicture(x_python_span_print)
            ievade_code()
            if ievade == "git":
                printPictirefinal(x_final)
            elif ievade == "python":
                printPictirefinal(x_final)
        if ievade == "python":
            printPicture(x_python_print)
            ievade_code()
            if ievade == "span":
                printPicture(x_python_span_print)
            elif ievade == "git":
                printPicture(x_git_print_python)
            ievade_code()
            if ievade == "git":
                printPictirefinal(x_final)
            elif ievade == "span":
                printPictirefinal(x_final)
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
                printPictirefinal(x_final)
            elif ievade == "python":
                printPictirefinal(x_final)
        if ievade == "print":
            printPicture(x_print_span)
            ievade_code()
            if ievade == "git":
                printPicture(x_git_print_span)
            elif ievade == "python":
                printPicture(x_python_span_print)
            ievade_code()
            if ievade == "git":
                printPictirefinal(x_final)
            elif ievade == "python":
                printPictirefinal(x_final)
        if ievade == "python":
            printPicture(x_python_span)
            ievade_code()
            if ievade == "print":
                printPicture(x_python_span_print)
            elif ievade == "git":
                printPicture(x_git_python_span)
            ievade_code()
            if ievade == "git":
                printPictirefinal(x_final)
            elif ievade == "print":
                printPictirefinal(x_final)

def printPictirefinal(xH):
    os.system("cls")
    print(xH)
    print("Apsveicu!")
    end_time = time.time()
    result_time = 0
    result_time = round(end_time - start_time, 3)
    print("Jūsu laiks: ", end="")
    print(result_time)
    nakamais_meginajums()

def nakamais_meginajums():
    print("Jūs gribat uzlabot savu rezultatu?")
    print()
    print("Ja gribat, nospežat ENTER")
    print('Ja ne, ievadiet "exit"')       
    ievade = input()
    if ievade == "":
        global start_time
        game_start()
        start_time = time.time()
        game_basic()
        nakamais_meginajums()
    if ievade == "exit":
        os.system("cls")
        print("Paldies par spelešanu!")
        sys.exit()
        
game_start()
start_time = time.time()
game_basic()
nakamais_meginajums()        