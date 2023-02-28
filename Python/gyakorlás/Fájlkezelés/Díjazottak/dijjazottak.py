from random import *

def feladat1(vnevek:list, knevek:list, pontok:list):
    fr = open("be.txt", "r")
    be = fr.readlines()
    
    global hatar
    hatar = float(be[0])
    
    for i in range(1, len(be)):
        be[i] = be[i].replace(";", " ")
        be[i] = be[i].replace("\n", "")
        vnevek.append(be[i].split()[0])
        knevek.append(be[i].split()[1])
        pontok.append(be[i].split()[2])
        
        
def feladat2(vnevek:list, knevek:list, pontok:list):
    vnevek.append("Aloe")
    knevek.append("Vera")
    pontok.append(randint(1, int(hatar*0.75)))
    
    
def feladat3(pontok, p, a, b, c, d, vnevek, knevek):
    for i in range(len(pontok)):
        
        if int(pontok[i]) > int(p*0.9):
            a.append(vnevek[i] + knevek[i])
            
        elif int(pontok[i]) > int(p*0.8):
            b.append(vnevek[i] + knevek[i])
            
        elif int(pontok[i]) > int(p*0.7):
            c.append(vnevek[i] + knevek[i])
            
        elif int(pontok[i]) < int(p*0.7):
            d.append(vnevek[i] + knevek[i])
            
            
def feladat4(vnevek, knevek, a, b, c, d):
    fw = open("ki.txt", "w")
    for i in range(len(a)):
        fw.write(str(len(a)))
        fw.write(";")
        fw.write(str(a[i]))
        fw.write(";")
    fw.write("\n")
        
    for i in range(len(b)):
        fw.write(str(len(b)))
        fw.write(";")
        fw.write(str(b[i]))
        fw.write(";")
    fw.write("\n")
    
    for i in range(len(c)):
        fw.write(str(len(c)))
        fw.write(";")
        fw.write(str(c[i]))
        fw.write(";")
    fw.write("\n")
    
    for i in range(len(d)):
        fw.write(str(len(d)))
        fw.write(";")
        fw.write(str(d[i]))
        fw.write(";")
    fw.write("\n")
    fw.close()
            

def main():
    vnevek = []
    knevek = []
    pontok = []
    
    feladat1(vnevek, knevek, pontok)
    feladat2(vnevek, knevek, pontok)
    
    a = []
    b = []
    c = []
    d = []
    feladat3(pontok, hatar, a, b, c, d, vnevek, knevek)

    feladat4(vnevek, knevek, a, b, c, d)
    
    # print(1 < 2.00)
    print(vnevek)
    print(knevek)
    print(pontok)
    print(a)
    print(b)
    print(c)
    print(d)
main()