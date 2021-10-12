def outertask(task):
  print('began task',task)
  print('doing somebackground activity')

  def innerTask(thread):
      #print('started performing ',thread, 'within ',task,'  task')
      print("started performing {} thread within {} task".format(thread,task))

  innerTask('memory allocation activity')
  
  return innerTask

subtasks=outertask('OS Process scheduling')
subtasks('thread priority')
subtasks('garbage collection')
subtasks('process killing')