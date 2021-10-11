list=[
  {"sno":1,"name":"Raj","city":"Chennai"},
  {"task1":"Cutting","task2":"Cooking","task3":"Serving"}
]

def processPeople(sno,name,city):
    print("sno ",sno)
    print("name ",name)
    print("city ",city)

def processPerson(person):
    print("sno ",person["sno"])
    print("name ",person["name"])
    print("city ",person["city"])
  



def processTasks1(task):
    print("doing ",task["task1"])
    print("doing ", task["task2"])
    print("doing ",task["task3"])

def processTasks2(task1,task2,task3):
    print("doing ",task1)
    print("doing", task2)
    print("doing",task3)

processPeople(list[0]["sno"],list[0]["name"],list[0]["city"])
processPerson(list[0])

runTasks=processTasks2
runTasks(list[1]["task1"],list[1]["task2"],list[1]["task3"])
runTasks=processTasks1
runTasks(list[1])
runTasks=processPerson
runTasks(list[0])