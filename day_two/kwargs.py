def process(**items):
    for key,value in items.items():
        print(key,"'s value is", value)


process(sno=1,name="Rahul",city="Chennai")
print("---------------------------------------------------")
process(name="Rajan",interests="Java")