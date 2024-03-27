import time
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



print(x0, "Sveicinati!...")
time.sleep(1)
print("Jūsu jautajumi:...")








input1 = input("")
if input1 == "git":
    print(x2)

input2_1 = input("")
if input2_1 == "print":
    print(x2_1)

input2_1_3 = input("")
if input2_1_3 == "mainigais":
    print(x2_1_3)
elif input2_1_3 == "python":
    print(x2_1_1h)

input2_1_3_f = input("")
if input2_1_3_f == "python":
    print(x_final)
elif input2_1_3_f == "mainigais":
    print(x_final)
    
