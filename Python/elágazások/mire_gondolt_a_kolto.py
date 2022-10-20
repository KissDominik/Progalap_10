p1 = int(input("irásbeli 1 pontjai: "))
p2 = int(input("irásbeli 2 pontjai: "))
p3 = int(input("irásbeli 3 pontjai: "))
p4 = int(input("szóbeli pontjai: "))

if p1 >= 0 and p1 <= 50 and p2 >= 0 and p2 <= 50 and p3 >= 0 and p3 <= 50 and p4 >= 0 and p4 <= 50:
    if p4 >= 50 * 0.6:
        if p1 >= 50 * 0.8 or p2 >= 50 * 0.8 or p3 >= 50 * 0.8:
            print("átment")
        else:
            print("Bukott")
    else:
        print("Bukott")
else:
    print("nem lehetséges pontszám")