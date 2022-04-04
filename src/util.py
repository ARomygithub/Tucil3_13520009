import random

# VAR GLOBAL
dr = [1,0,-1,0]
dc = [0,-1,0,1]
action = ["up","right","down","left"]

def randomPuzzle():
    puzzle = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","-"]
    random.shuffle(puzzle)
    # print(tuple(puzzle))
    return tuple(puzzle)

def inputPuzzleFromFile():
    while(True):
        pathInput = input("Masukkan path file input: ")
        try:
            file = open(pathInput, "r")
            puzzle = tuple(file.read().split())
            # print(puzzle)
            return puzzle
        except(OSError):
            print("path input tidak valid")

def printDivider():
    print("========================================================================================")

def printPuzzle(puzzle):
    ct = 0
    for i in range(4):
        for j in range(4):
            print(puzzle[ct], end=" ")
            ct +=1
        print()

def KURANG(i, puzzle):
    kecil_I = 0
    if(i==16):
        for k in range(16):
            if(puzzle[k]=="-"):
                break
            elif(int(puzzle[k])<i):
                kecil_I +=1
    else:
        for k in range(16):
            if(puzzle[k]=="-"):
                continue # 16>i
            elif(int(puzzle[k])==i):
                break
            elif(int(puzzle[k])<i):
                kecil_I +=1
    return (i-1-kecil_I)

# jika "-" di baris+kolom ganjil return 1, else return 0
def X(puzzle):
    idx = puzzle.index("-")
    # print("idx "+str(idx))
    baris = idx //4
    kolom = idx % 4
    if((baris+kolom)%2==1):
        return 1
    else:
        return 0

# mencetak nilai KURANG(i),X dan mengembalikan totalnya
def printKURANG_I_X(puzzle):
    sum = 0
    print("Berikut nilai KURANG(i) dan X:")
    for i in range(1,17):
        kurangi = KURANG(i,puzzle)
        print("KURANG({}) = {}".format(i,KURANG(i,puzzle)))
        sum += kurangi
    x = X(puzzle)
    print("X= {}".format(x))
    sum += x
    print("SIGMA KURANG(i) + X = {}".format(sum))
    return sum

def g(puzzle):
    ct = 0
    for i in range(16):
        if(puzzle[i]!="-" and int(puzzle[i])!=i+1):
            ct +=1
    return ct

def sol(puzzle):
    for i in range(15):
        if(puzzle[i]=="-" or int(puzzle[i])!=i+1):
            return False
    if(puzzle[15]!="-"):
        return False
    return True

def toIdx(r,c):
    return 4*r+c

def toRC(idx):
    return idx//4,idx%4

# cek puzzle dapat melakukan aksi ke-k
def canMove(k,puzzle):
    r,c = toRC(puzzle.index("-"))
    rk = r+dr[k]; ck = c+dc[k]
    return (rk>=0 and rk<=3 and ck>=0 and ck<=3)

# mengembalikan posisi puzzle setelah aksi ke-k
def after(k,puzzle):
    r,c = toRC(puzzle.index("-"))
    rk = r+dr[k]; ck = c+dc[k]
    p = list(puzzle)
    idx = toIdx(r,c); idxk = toIdx(rk,ck)
    temp = p[idx]
    p[idx] = p[idxk]
    p[idxk] = temp
    return tuple(p)

#mengembalikan posisi puzzle sebelum melakukan aksi ke-k
def before(k,puzzle):
    return after((k+2)%4,puzzle)