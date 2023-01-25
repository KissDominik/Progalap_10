be = input()
mgh = ["a", "e", "i", "o", "u"]
egynek_szamit = ["cs", "ccs", "dz", "ddz", "dzs" "ty", "tty", "sz", "ssz", "gy", "ggy", "ly", "lly", "ny", "nny"]
mgh_index = []
megoldas = []










for i in range(len(be)):
    if be[i] in mgh:
        mgh_index.append(i)

for i in range(0, len(mgh_index)-1):
    megoldas.append(mgh_index[i+1] - mgh_index[i])

for i in megoldas:
    print(i-1, end=" ")