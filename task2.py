def divisible_by_3_turing_machine(binary_input):
   
    state = 'q0'

    for bit in binary_input:
        if bit not in {'0', '1'}:
            return False  # Invalid character

        if state == 'q0':
            state = 'q0' if bit == '0' else 'q1'
        elif state == 'q1':
            state = 'q2' if bit == '0' else 'q0'
        elif state == 'q2':
            state = 'q1' if bit == '0' else 'q2'

    return state == 'q0'



print(divisible_by_3_turing_machine("110"))   # True → 6
print(divisible_by_3_turing_machine("101"))   # False → 5
print(divisible_by_3_turing_machine("1001"))  # True → 9
