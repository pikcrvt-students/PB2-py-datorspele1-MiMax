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
x1 = '''
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


print(x1, "Sveicinati!...")
time.sleep(1)
print("Jūsu jautajumi:...")
input = ("")
if input == "git":
    print(x2)
