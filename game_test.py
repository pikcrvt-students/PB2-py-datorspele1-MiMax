import time
import sys
import os
x_final = '''
       _ _ _   _ _ _
       | g |   | m |
       | i |   | a |
 - - - - - - - | i |
 | p | y t h o | n |
 | r | - - - - | i |
 | i |         | g |
 | n |         | a |
 | t |         | i |
 - - -         | s |
               - - -
 '''
x0 = '''
       _ _ _   _ _ _
       | 2 |   | 3 |
       |   |   |   |
 - - - - - - - |   |
 | 1 |         |   |
 |   | - - - - |   |
 |   |         |   |
 |   |         |   |
 |   |         |   |
 - - -         |   |
               - - -

'''

x2 = '''
       _ _ _   _ _ _
       | g |   | 3 |
       | i |   |   |
 - - - - - - - |   |
 | 1 |   t     |   |
 |   | - - - - |   |
 |   |         |   |
 |   |         |   |
 |   |         |   |
 - - -         |   |
               - - -

'''

x2_1 = '''
       _ _ _   _ _ _
       | g |   | 3 |
       | i |   |   |
 - - - - - - - |   |
 | p |   t     |   |
 | r | - - - - |   |
 | i |         |   |
 | n |         |   |
 | t |         |   |
 - - -         |   |
               - - -

'''

x2_1_3 = '''
       _ _ _   _ _ _
       | g |   | m |
       | i |   | a |
 - - - - - - - | i |
 | p |   t     | n |
 | r | - - - - | i |
 | i |         | g |
 | n |         | a |
 | t |         | i |
 - - -         | s |
               - - -

'''
x2_1_1h = '''
       _ _ _   _ _ _
       | g |   | 3 |
       | i |   |   |
 - - - - - - - |   |
 | p | y t h o | n |
 | r | - - - - |   |
 | i |         |   |
 | n |         |   |
 | t |         |   |
 - - -         |   |
               - - -

'''

x2_1h = '''
       _ _ _   _ _ _
       | g |   | 3 |
       | i |   |   |
 - - - - - - - |   |
 | p | y t h o | n |
 |   | - - - - |   |
 |   |         |   |
 |   |         |   |
 |   |         |   |
 - - -         |   |
               - - -

'''
x2_1h_3 = '''
       _ _ _   _ _ _
       | g |   | m |
       | i |   | a |
 - - - - - - - | i |
 | p | y t h o | n |
 |   | - - - - | i |
 |   |         | g |
 |   |         | a |
 |   |         | i |
 - - -         | s |
               - - -

'''
x2_3 = '''
       _ _ _   _ _ _
       | g |   | m |
       | i |   | a |
 - - - - - - - | i |
 | 1 |   t     | n |
 |   | - - - - | i |
 |   |         | g |
 |   |         | a |
 |   |         | i |
 - - -         | s |
               - - -

'''
x1h = '''
       _ _ _   _ _ _
       | 2 |   | 3 |
       |   |   |   |
 - - - - - - - |   |
 | p | y t h o | n |
 |   | - - - - |   |
 |   |         |   |
 |   |         |   |
 |   |         |   |
 - - -         |   |
               - - -

'''
x1h_3 = '''
       _ _ _   _ _ _
       | 2 |   | m |
       |   |   | a |
 - - - - - - - | i |
 | p | y t h o | n |
 |   | - - - - | i |
 |   |         | g |
 |   |         | a |
 |   |         | i |
 - - -         | s |
               - - -

'''
x1h_3_1 = '''
       _ _ _   _ _ _
       | 2 |   | m |
       |   |   | a |
 - - - - - - - | i |
 | p | y t h o | n |
 | r | - - - - | i |
 | i |         | g |
 | n |         | a |
 | t |         | i |
 - - -         | s |
               - - -

'''
x1h_1 = '''
       _ _ _   _ _ _
       | 2 |   | 3 |
       |   |   |   |
 - - - - - - - |   |
 | p | y t h o | n |
 | r | - - - - |   |
 | i |         |   |
 | n |         |   |
 | t |         |   |
 - - -         |   |
               - - -

'''

x1 = '''
       _ _ _   _ _ _
       | 2 |   | 3 |
       |   |   |   |
 - - - - - - - |   |
 | p |         |   |
 | r | - - - - |   |
 | i |         |   |
 | n |         |   |
 | t |         |   |
 - - -         |   |
               - - -

'''
x1_3 = '''
       _ _ _   _ _ _
       | 2 |   | m |
       |   |   | a |
 - - - - - - - | i |
 | p |         | n |
 | r | - - - - | i |
 | i |         | g |
 | n |         | a |
 | t |         | i |
 - - -         | s |
               - - -

'''
x3 = '''
       _ _ _   _ _ _
       | 2 |   | m |
       |   |   | a |
 - - - - - - - | i |
 | 1 |         | n |
 |   | - - - - | i |
 |   |         | g |
 |   |         | a |
 |   |         | i |
 - - -         | s |
               - - -

'''

os.system("cls")
print(x0, "Sveicinati! Šodien jūs risināsiet krustvārdu mīklu, novēlu jums veiksmi un nepieļaujiet kļūdas :)")
time.sleep(3)
Jautajumi = '''1 (vertikali) Kura Python funkcija tiek izmantota, lai attēlotu tekstu uz ekrāna?
1 (horizontali) Kāda programmēšanas valoda tiek izmantota Django projektā?
2 Kura versiju kontroles sistēma tiek plaši izmantota, lai pārvaldītu un izsekotu izmaiņas kodā? 
3 Kādu funkciju parasti izmanto Python programmā, lai norādītu, kura daļa no koda ir galvenā un jāizpilda vispirms?'''
print(Jautajumi)
pal = "Apsveicu!"

def final():
    os.system("cls")
    print(x_final)
    print(pal)
    sys.exit()
def x2_1_3_def():
    os.system("cls")
    print(x2_1_3)
    print(Jautajumi)
def x2_1_1h_def():
    os.system("cls")
    print(x2_1_1h)
    print(Jautajumi)

i = input("")
if i == "git":
    os.system("cls")
    print(x2)
    print(Jautajumi)
    i = input("")
    if i == "print":
        os.system("cls")
        print(x2_1)
        print(Jautajumi)
        i = input("")
        if i == "mainigais":
            x2_1_3_def()
        elif i == "python":
            x2_1_1h_def()
        i = input("")
        if i == "python":
            final()
        elif i == "mainigais":
            final()
    if i == "python":
        os.system("cls")
        print(x2_1h)
        print(Jautajumi)
        i = input("")
        if i == "mainigais":
            os.system("cls")
            print(x2_1h_3)
            print(Jautajumi)
        elif i == "print":
            x2_1_1h_def()
        i = input("")
        if i == "print":
            final()
        elif i == "mainigais":
            final()
    
    if i == "mainigais":
        os.system("cls")
        print(x2_3)
        print(Jautajumi)
        i = input("")
        if i == "print":
            x2_1_3_def()
        elif i == "python":
            os.system("cls")
            print(x2_1h_3)
            print(Jautajumi)
        i = input("")
        if i == "print":
            final()
        elif i == "python":
            final()
if i == "python":
    os.system("cls")
    print(x1h)
    print(Jautajumi)
    i = input ("")
    if i == "git":
        os.system("cls")
        print(x2_1h)
        print(Jautajumi)
        i = input("")
        if i == "mainigais":
            os.system("cls")
            print(x2_1h_3)
            print(Jautajumi)
        elif i == "print":
            x2_1_1h_def()
        i = input("")
        if i == "mainigais":
            final()
        elif i == "print":
            final()
    if i == "mainigais":
        os.system("cls")
        print(x1h_3)
        print(Jautajumi)
        i = input("")
        if i == "git":
            os.system("cls")
            print(x2_1h_3)
            print(Jautajumi)
        elif i == "print":
            os.system("cls")
            print(x1h_3_1)
            print(Jautajumi)
        i = input("")
        if i == "git":
            final()
        elif i == "print":
            final()
    if i == "print":
        os.system("cls")
        print(x1h_1)
        print(Jautajumi)
        i = input("")
        if i == "mainigais":
            os.system("cls")
            print(x1h_3_1)
            print(Jautajumi)
        elif i == "git":
            x2_1_1h_def()
        i = input("")
        if i == "git":
            final()
        elif i == "mainigais":
            final()
if i == "print":
    os.system("cls")
    print(x1)
    print(Jautajumi)
    i = input ("")
    if i == "git":
        os.system("cls")
        print(x2_1)
        print(Jautajumi)
        i = input("")
        if i == "mainigais":
            x2_1_3_def()
        elif i == "python":
            x2_1_1h_def()
        i = input("")
        if i == "mainigais":
            final()
        elif i == "python":
            final()
    if i == "mainigais":
        os.system("cls")
        print(x1_3)
        print(Jautajumi)
        i = input("")
        if i == "git":
            x2_1_3_def()
        elif i == "python":
            os.system("cls")
            print(x1h_3_1)
            print(Jautajumi)
        i = input("")
        if i == "git":
            final()
        elif i == "python":
            final()
    if i == "python":
        os.system("cls")
        print(x1h_1)
        print(Jautajumi)
        i = input("")
        if i == "mainigais":
            os.system("cls")
            print(x1h_3_1)
            print(Jautajumi)
        elif i == "git":
            x2_1_1h_def()
        i = input("")
        if i == "git":
            final()
        elif i == "mainigais":
            final()
if i == "mainigais":
    os.system("cls")
    print(x3)
    print(Jautajumi)
    i = input ("")
    if i == "git":
        os.system("cls")
        print(x2_3)
        print(Jautajumi)
        i = input("")
        if i == "print":
            x2_1_3_def()
        elif i == "python":
            os.system("cls")
            print(x2_1h_3)
            print(Jautajumi)
        i = input("")
        if i == "print":
            final()
        elif i == "python":
            final()
    if i == "print":
        os.system("cls")
        print(x1_3)
        print(Jautajumi)
        i = input("")
        if i == "git":
            x2_1_3_def()
        elif i == "python":
            os.system("cls")
            print(x1h_3_1)
            print(Jautajumi)
        i = input("")
        if i == "git":
            final()
        elif i == "python":
            final()
    if i == "python":
        os.system("cls")
        print(x1h_3)
        print(Jautajumi)
        i = input("")
        if i == "print":
            os.system("cls")
            print(x1h_3_1)
            print(Jautajumi)
        elif i == "git":
            os.system("cls")
            print(x2_1h_3)
            print(Jautajumi)
        i = input("")
        if i == "git":
            final()
        elif i == "print":
            final()