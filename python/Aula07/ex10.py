print("Me diga um numero e eu lhe direi todos os numeros primos até ele: ")
num = int(input())
for i in range(2, num + 1):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)