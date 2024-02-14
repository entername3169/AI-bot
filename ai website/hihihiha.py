from sr import spre
p = 0
print("HOLA!!! SOY DORA!!! CAN YOU SAY: BANANA????")

q1 = spre("en-GB")
if q1.strip() == "banana":
    p += 1
    print("YOU DID IT!!! NOW CAN YOU SAY: WATER???")
    q2 = spre("en-GB")
    if q2.strip() == "water":
        p += 1
        print("YOU DID IT!!! NOW CAN YOU SAY: TOENAIL???")
        q3 = spre("en-GB")
        if q3.strip() == "toenail":
            p += 1
            print("YOU DID IT!!!")
            print("YOU HAVE", p, "POINTS!!!")
        else:
            p -= 1
            print("NUH UH! YOU LOSE! LOSER!")
    else:
        p -= 1
        print(q2)
        print("NUH UH! YOU LOSE! LOSER!")
        
else:
    p -= 1
    print("NUH UH! YOU LOSE! LOSER!")