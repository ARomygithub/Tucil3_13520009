import time
from queue import PriorityQueue
from util import *

# wrapper puzzle yang memakai c(p) sebagai prioritas
class PuzzleBnB:
    def __init__(self,fp,gp,puzzle):
        self.fp = fp
        self.gp = gp
        self.priority = fp+gp
        self.puzzle = puzzle
    
    def __lt__(self, other):
        return self.priority < other.priority

# membuat puzzle
while(True):
    print("Pilih opsi pembangkitan posisi awal 15-Puzzle")
    print("1. Dari file")
    print("2. Dari random generator")
    opsi = int(input("Masukkan nomor opsi: "))
    if(opsi==1):
        puzzle = inputPuzzleFromFile()
        break
    elif(opsi==2):
        puzzle = randomPuzzle()
        break
    else:
        print("Opsi tidak valid")

printDivider()
print("Matriks posisi awal 15-puzzle:")
printPuzzle(puzzle)
sum = printKURANG_I_X(puzzle)
printDivider()
if(sum%2==1):
    print("15-puzzle tidak dapat diselesaikan karena hasil penjumlahan bernilai ganjil")
else:
    print("15-puzzle dapat diselesaikan!")
    print("MULAI PENCARIAN...")
    pq = PriorityQueue()
    mp = {puzzle:0} # dict/map penyimpan best fp so far
    mpAction = dict()
    ctNode = 0
    start = time.time()
    pq.put(PuzzleBnB(0,g(puzzle),puzzle))
    ctNode +=1
    while(pq.qsize()>0):
        PrioPuzzle = pq.get()
        fpu = PrioPuzzle.fp
        pu = PrioPuzzle.puzzle
        if(fpu>mp[pu]):
            continue
        if(sol(pu)):
            final = pu
            ctStep = fpu
            break
        for k in range(4):
            if(canMove(k,pu)):
                pv = after(k,pu)
                if((pv not in mp) or mp[pv]>fpu+1):
                    mp[pv] = fpu+1
                    mpAction[pv] = k
                    pq.put(PuzzleBnB(fpu+1,g(pv),pv))
                    ctNode +=1

    # pencarian selesai
    end = time.time()
    elapsedTime = end-start
    print("PENCARIAN SELESAI")
    printDivider()

    list_of_puzzle = []
    u = final
    while(u!=puzzle):
        k = mpAction[u]
        list_of_puzzle.append((u,action[k]))
        u = before(k,u)
    list_of_puzzle.reverse()
    print("Posisi awal:")
    printPuzzle(puzzle)
    printDivider()
    ctAksi=1
    for u, act in list_of_puzzle:
        print("Aksi ke-{}: ".format(ctAksi)+act)
        print("Hasil setelah aksi:")
        printPuzzle(u)
        printDivider()
        ctAksi +=1
    
    print("Langkah yang dibutuhkan: {}".format(ctStep))
    print("Waktu eksekusi program: {}".format(elapsedTime))
    print("Jumlah simpul yang dibangkitkan: {}".format(ctNode))
