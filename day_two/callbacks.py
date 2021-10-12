def factoryProcess(item,process):
   stage="initial"
   print(item, ' is printed')
   process(stage)
   stage="binding"
   print(item, ' is sent for binding')
   process(stage)
   stage ="finishing"
   print(item, ' cover page is attached')
   process(stage)

def userProcess(stage):
    if stage=="initial":
        print('arranging pages and pasting picture')
    elif stage=="binding":
        print('preparing images for cover page')
    elif stage=="finishing":
        print('Book is ready is for sale')


print("Started book manufacturing")
print("Documented the book in a document editor")
factoryProcess("Java Book",userProcess)