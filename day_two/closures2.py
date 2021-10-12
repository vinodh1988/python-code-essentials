def outer(state):
    temp=state
    print('performing outer activity with ',temp)
    def inner():
        nonlocal temp
        nonlocal state
        state='MNCMNC'
        print('doing task utilizing outer state ',state)
        temp="XYZXYZXYZ"
        print("performing ",temp)
    inner()
    print("done with outer activity",temp)
    print(state)
outer("ABCABCABC")