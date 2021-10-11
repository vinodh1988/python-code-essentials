def process(step1,step2='packaging',step3='deploying'):
    print("doing ",step1)
    print("doing ",step2)
    print("doing ",step3)

process("coding","testing","deploying")
print("----------------------------")
activities=["coding","testing",'packing','reporting',"deploying",'designing','monitoring'
,'debugging']

process(step1=activities[0],step3=activities[1],step2=activities[7])
process(activities[0],step3=activities[3],step2=activities[7])
print("-------------------------------------------")
process(step1="coding",step2="building")
process(activities[0],step3=activities[3],step2=activities[7])
print("-------------------------------------------")
process(step1='coding',step3="deploy to cloud")