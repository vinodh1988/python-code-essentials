def outer(state):
    temp=state
    print('performing outer activity with ',temp)
    def inner():
        print('doing task utilizing outer state ',state)
        temp="XYZXYZXYZ"
        print("performing ",temp)
    inner()
    print("done with outer activity",temp)

outer("ABCABCABC")