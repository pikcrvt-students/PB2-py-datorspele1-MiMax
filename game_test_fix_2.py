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

os.system("cls")
print(x0, "Sveicinati! Šodien jūs risināsiet krustvārdu mīklu, novēlu jums veiksmi un nepieļaujiet kļūdas :)")
time.sleep(1)
Jautajumi = '''1 (vertikali) Kura Python funkcija tiek izmantota, lai attēlotu tekstu uz ekrāna?
1 (horizontali) Kāda programmēšanas valoda tiek izmantota Django projektā?
2 Kura versiju kontroles sistēma tiek plaši izmantota, lai pārvaldītu un izsekotu izmaiņas kodā? 
3 Atribūts, kurš atgriež tupli, kas satur sakritības (sākuma, beigu) pozīcijas'''
print(Jautajumi)
pal = "Apsveicu!"

def printPicture(xH): 
    os.system("cls") 
    print(xH) 
    print(Jautajumi)
def printPictirefinal(xH):
    os.system("cls")
    print(xH)
    print(pal)
    sys.exit()

y = 5
def hint():
    global y
    global i
    while i != "git" and i != "python" and i != "span" and i != "print":
        print("Nepareizi!")
        y -= 1
        if y == 0:
            print("LOSE")
            sys.exit()
        i = input("")


i = input("")
hint()

if i == "git":
    printPicture(x2)
    i = input("")
    hint()
    if i == "print":
        printPicture(x2_1)
        i = input("")
        hint()
        if i == "span":
            printPicture(x2_1_3)
        elif i == "python":
            printPicture(x2_1_1h)
        i = input("")
        hint()
        if i == "python":
            printPictirefinal(x_final)
        elif i == "span":
            printPictirefinal(x_final)
    if i == "python":
        printPicture(x2_1h)
        i = input("")
        hint()
        if i == "span":
            printPicture(x2_1h_3)
        elif i == "print":
            printPicture(x2_1_1h)
        i = input("")
        hint()
        if i == "print":
            printPictirefinal(x_final)
        elif i == "span":
            printPictirefinal(x_final)
    
    if i == "span":
        printPicture(x2_3)
        i = input("")
        hint()
        if i == "print":
            printPicture(x2_1_3)
        elif i == "python":
            printPicture(x2_1h_3)
        i = input("")
        hint()
        if i == "print":
            printPictirefinal(x_final)
        elif i == "python":
            printPictirefinal(x_final)
if i == "python":
    printPicture(x1h)
    i = input ("")
    if i == "git":
        printPicture(x2_1h)
        i = input("")
        hint()
        if i == "span":
            printPicture(x2_1h_3)
        elif i == "print":
            printPicture(x2_1_1h)
        i = input("")
        hint()
        if i == "span":
            printPictirefinal(x_final)
        elif i == "print":
            print(x_final)
    if i == "span":
        printPicture(x1h_3)
        i = input("")
        hint()
        if i == "git":
            printPicture(x2_1h_3)
        elif i == "print":
            printPicture(x1h_3_1)
        i = input("")
        hint()
        if i == "git":
            printPictirefinal(x_final)
        elif i == "print":
            printPictirefinal(x_final)
    if i == "print":
        printPicture(x1h_1)
        i = input("")
        hint()
        if i == "span":
            printPicture(x1h_3_1)
        elif i == "git":
            printPicture(x2_1_1h)
        i = input("")
        hint()
        if i == "git":
            printPictirefinal(x_final)
        elif i == "span":
            printPictirefinal(x_final)
if i == "print":
    printPicture(x1)
    i = input ("")
    if i == "git":
        printPicture(x2_1)
        i = input("")
        hint()
        if i == "span":
            printPicture(x2_1_3)
        elif i == "python":
            printPicture(x2_1_1h)
        i = input("")
        hint()
        if i == "span":
            printPictirefinal(x_final)
        elif i == "python":
            printPictirefinal(x_final)
    if i == "span":
        printPicture(x1_3)
        i = input("")
        hint()
        if i == "git":
            printPicture(x2_1_3)
        elif i == "python":
            printPicture(x1h_3_1)
        i = input("")
        hint()
        if i == "git":
            printPictirefinal(x_final)
        elif i == "python":
            printPictirefinal(x_final)
    if i == "python":
        printPicture(x1h_1)
        i = input("")
        hint()
        if i == "span":
            os.system("cls")
            print(x1h_3_1)
            printPicture(x1h_3_1)
        elif i == "git":
            printPicture(x2_1_1h)
        i = input("")
        hint()
        if i == "git":
            printPictirefinal(x_final)
        elif i == "span":
            printPictirefinal(x_final)
if i == "span":
    printPicture(x3)
    i = input ("")
    if i == "git":
        printPicture(x2_3)
        i = input("")
        hint()
        if i == "print":
            printPicture(x2_1_3)
        elif i == "python":
            printPicture(x2_1h_3)
        i = input("")
        hint()
        if i == "print":
            printPictirefinal(x_final)
        elif i == "python":
            printPictirefinal(x_final)
    if i == "print":
        printPicture(x1_3)
        i = input("")
        hint()
        if i == "git":
            printPicture(x2_1_3)
        elif i == "python":
            printPicture(x1h_3_1)
        i = input("")
        hint()
        if i == "git":
            printPictirefinal(x_final)
        elif i == "python":
            printPictirefinal(x_final)
    if i == "python":
        printPicture(x1h_3)
        i = input("")
        hint()
        if i == "print":
            printPicture(x1h_3_1)
        elif i == "git":
            printPicture(x2_1h_3)
        i = input("")
        hint()
        if i == "git":
            printPictirefinal(x_final)
        elif i == "print":
            printPictirefinal(x_final)