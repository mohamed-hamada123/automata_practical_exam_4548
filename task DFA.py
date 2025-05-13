def dfa_accepts_101(s):
    state = "q0"
    for ch in s:
        if state == "q0":
            if ch == "0":
                state = "q0"
            elif ch == "1":
                state = "q1"
        elif state == "q1":
            if ch == "0":
                state = "q2"
            elif ch == "1":
                state = "q1"
        elif state == "q2":
            if ch == "0":
                state = "q0"
            elif ch == "1":
                state = "q3"
        elif state == "q3":
            
            state = "q3"
    return state == "q3"


print(int(dfa_accepts_101("1101")))  
print(int(dfa_accepts_101("0000")))   
print(int(dfa_accepts_101("101010"))) 
