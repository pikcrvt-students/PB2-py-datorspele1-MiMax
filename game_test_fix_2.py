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

x2 = '''
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

x2_1 = '''
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

x2_1_3 = '''
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
x2_1_1h = '''
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

x2_1h = '''
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
x2_1h_3 = '''
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
x2_3 = '''
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
x1h = '''
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
x1h_3 = '''
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
x1h_3_1 = '''
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
x1h_1 = '''
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

x1 = '''
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
x1_3 = '''
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
x3 = '''
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
Kļudu_skaits = 5
os.system("cls")
print(x0, "Sveicinati! Šodien jūs risināsiet krustvārdu mīklu, novēlu jums veiksmi un nepieļaujiet kļūdas :)")
print ("Jums palika", Kļudu_skaits,"kļudas")
time.sleep(3)
Jautajumi = '''1 (vertikali) (5 burti) Kura Python funkcija tiek izmantota, lai attēlotu tekstu uz ekrāna?
1 (horizontali) (5 burti) Kāda programmēšanas valoda tiek izmantota Django projektā?
2 (3 burti) Kura versiju kontroles sistēma tiek plaši izmantota, lai pārvaldītu un izsekotu izmaiņas kodā? 
3 (4 vurti) Programmēšanas valoda, kas paredzēta Parrot virtuālajai mašīnai.'''
Jautajumi1 = '''1 (vertikali) (5 burti) Kura Python funkcija tiek izmantota, lai attēlotu tekstu uz ekrāna?'''
Jautajumi1h= '''1 (horizontali) (5 burti) Kāda programmēšanas valoda tiek izmantota Django projektā?'''
Jautajumi2 = '''2 (3 burti) Kura versiju kontroles sistēma tiek plaši izmantota, lai pārvaldītu un izsekotu izmaiņas kodā? '''
Jautajumi3 = '''3 (4 vurti) Programmēšanas valoda, kas paredzēta Parrot virtuālajai mašīnai.'''

print(Jautajumi1)
time.sleep(1)
print(Jautajumi1h)
time.sleep(1)
print(Jautajumi2)
time.sleep(1)
print(Jautajumi3)

def printPicture(xH): 
    os.system("cls") 
    print(xH) 
    print(Jautajumi)
def printPictirefinal(xH):
    os.system("cls")
    print(xH)
    print("Apsveicu!")
    sys.exit()

ievade=""

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
            time.sleep(2)
            sys.exit()
        ievade = input("")
    
ievade_code()
if ievade == "git":
    printPicture(x2)
    ievade_code()
    if ievade == "print":
        printPicture(x2_1)
        ievade_code()
        if ievade == "span":
            printPicture(x2_1_3)
        elif ievade == "python":
            printPicture(x2_1_1h)
        ievade_code()
        if ievade == "python":
            printPictirefinal(x_final)
        elif ievade == "span":
            printPictirefinal(x_final)
    if ievade == "python":
        printPicture(x2_1h)
        ievade_code()
        if ievade == "span":
            printPicture(x2_1h_3)
        elif ievade == "print":
            printPicture(x2_1_1h)
        ievade_code()
        if ievade == "print":
            printPictirefinal(x_final)
        elif ievade == "span":
            printPictirefinal(x_final)
    if ievade == "span":
        printPicture(x2_3)
        ievade_code()
        if ievade == "print":
            printPicture(x2_1_3)
        elif ievade == "python":
            printPicture(x2_1h_3)
        ievade_code()
        if ievade == "print":
            printPictirefinal(x_final)
        elif ievade == "python":
            printPictirefinal(x_final)
if ievade == "python":
    printPicture(x1h)
    ievade_code()
    if ievade == "git":
        printPicture(x2_1h)
        ievade_code()
        if ievade == "span":
            printPicture(x2_1h_3)
        elif ievade == "print":
            printPicture(x2_1_1h)
        ievade_code()
        if ievade == "span":
            printPictirefinal(x_final)
        elif ievade == "print":
            print(x_final)
    if ievade == "span":
        printPicture(x1h_3)
        ievade_code()
        if ievade == "git":
            printPicture(x2_1h_3)
        elif ievade == "print":
            printPicture(x1h_3_1)
        ievade_code()
        if ievade == "git":
            printPictirefinal(x_final)
        elif ievade == "print":
            printPictirefinal(x_final)
    if ievade == "print":
        printPicture(x1h_1)
        ievade_code()
        if ievade == "span":
            printPicture(x1h_3_1)
        elif ievade == "git":
            printPicture(x2_1_1h)
        ievade_code()
        if ievade == "git":
            printPictirefinal(x_final)
        elif ievade == "span":
            printPictirefinal(x_final)
if ievade == "print":
    printPicture(x1)
    ievade_code()
    if ievade == "git":
        printPicture(x2_1)
        ievade_code()
        if ievade == "span":
            printPicture(x2_1_3)
        elif ievade == "python":
            printPicture(x2_1_1h)
        ievade_code()
        if ievade == "span":
            printPictirefinal(x_final)
        elif ievade == "python":
            printPictirefinal(x_final)
    if ievade == "span":
        printPicture(x1_3)
        ievade_code()
        if ievade == "git":
            printPicture(x2_1_3)
        elif ievade == "python":
            printPicture(x1h_3_1)
        ievade_code()
        if ievade == "git":
            printPictirefinal(x_final)
        elif ievade == "python":
            printPictirefinal(x_final)
    if ievade == "python":
        printPicture(x1h_1)
        ievade_code()
        if ievade == "span":
            printPicture(x1h_3_1)
        elif ievade == "git":
            printPicture(x2_1_1h)
        ievade_code()
        if ievade == "git":
            printPicture(x_final)
        elif ievade == "span":
            printPictirefinal(x_final)
if ievade == "span":
    printPicture(x3)
    ievade_code()
    if ievade == "git":
        printPicture(x2_3)
        ievade_code()
        if ievade == "print":
            printPicture(x2_1_3)
        elif ievade == "python":
            printPicture(x2_1h_3)
        ievade_code()
        if ievade == "print":
            printPictirefinal(x_final)
        elif ievade == "python":
            printPictirefinal(x_final)
    if ievade == "print":
        printPicture(x1_3)
        ievade_code()
        if ievade == "git":
            printPicture(x2_1_3)
        elif ievade == "python":
            printPicture(x1h_3_1)
        ievade_code()
        if ievade == "git":
            printPictirefinal(x_final)
        elif ievade == "python":
            printPictirefinal(x_final)
    if ievade == "python":
        printPicture(x1h_3)
        ievade_code()
        if ievade == "print":
            printPicture(x1h_3_1)
        elif ievade == "git":
            printPicture(x2_1h_3)
        ievade_code()
        if ievade == "git":
            printPictirefinal(x_final)
        elif ievade == "print":
            printPictirefinal(x_final)