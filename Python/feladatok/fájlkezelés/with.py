with open("fajlnev.txt", "r") as fr:
    fr.readline()


fw = open("fajlnev", "w")
fw.writeline("")
fr.close()

# Ird le milyen hibakat latsz a kepen

#csak a masodik reszen van:
# nem kell fr.close()
# nincs fw.close()
# fajlnev.txt
# fw.write()