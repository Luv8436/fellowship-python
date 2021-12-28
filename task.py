import sys

def readTask():
    file = open("path/to/plans/task.txt" , "r")
    lines = file.readlines()

    tasks = dict()
    for line in lines:
        task = line.strip().split(" ",1)
        if int(task[0]) not in tasks.keys():
            tasks[int(task[0])] = [task[1]]
        else:
            tasks[int(task[0])].append(task[1])

    file.close()

    return tasks

def sizeOfTask():
    tasks = readTask()
    size=0
    for priority in tasks:
        size+=len(tasks[priority])
    
    return size

def help():
    file = open("path/to/plans/help.txt" , "r")
    lines = file.readlines()
    for line in lines:
        print(line.strip())
    file.close()

def writeIntoTask(tasks):
    file = open("path/to/plans/task.txt" , "w")
    for key in sorted(tasks):
        for value in tasks[key]:
            file.write(str(key)+" "+value+"\n")

    file.close()

def readCompletedTasks():
    file = open("path/to/plans/completed.txt" , "r")
    lines = file.readlines()

    tasks = []
    for line in lines:
        task = line.strip()
        tasks.append(task)

    file.close()

    return tasks

def writeInToCompleted(completed):
    file = open("path/to/plans/completed.txt" , "w")
    for task in completed:
        file.write(task+"\n")

    file.close()

def deleteTask(i):
    tasks = readTask()

    # if sizeOfTask()<i:
        
        
    j=1
    deletedTask = None
    for priority in sorted(tasks):
        for task in tasks[priority]:
            if j==i:
                deletedTask = task
                tasks[priority].remove(task)
                return (tasks ,deletedTask)
            j+=1
    
    return (tasks ,None)

        
        
if len(sys.argv)<2:
    help()


elif (sys.argv[1]=="help"):
    help()

elif sys.argv[1]=="ls":
    # get dictionary of tasks with priority as key and values as list of tasks
    if sizeOfTask()==0:
        print("There are no pending tasks!")
    else:
        tasksOut = readTask()

        index=1
        for priority in sorted(tasksOut):
            for task in tasksOut[priority]:
                print(str(index)+". "+task+" ["+str(priority)+"]")
                index+=1

elif sys.argv[1]=="report":
    tasks = readTask()
    print("Pending : "+str(sizeOfTask()))
    index=1
    for priority in sorted(tasks):
        for task in tasks[priority]:
            print(str(index)+". "+task+" ["+str(priority)+"]")
            index+=1
    print()
    completedFileTasks = readCompletedTasks()
    print("Completed : "+str(len(completedFileTasks)))
    index=1
    for completedTask in completedFileTasks:
        print(str(index)+". "+completedTask)
        index+=1



elif sys.argv[1]=="done":
    if len(sys.argv)==3:
        i=int(sys.argv[2])
        response = deleteTask(i)
        tasks = response[0]
        completedTask = response[1]
        if completedTask is None:
            print("Error: no incomplete item with index #"+str(i)+" exists.")
        else:
            print("Marked item as done.")
            # write the updated tasks in task file
            writeIntoTask(tasks)
            # read tasks from completed.txt and add the completed task and write into file again
            completedFileTasks = readCompletedTasks()
            completedFileTasks.append(completedTask)
            writeInToCompleted(completedFileTasks)
    else:
        print("Error: Missing NUMBER for marking tasks as done.")

elif sys.argv[1]=="del":
    if len(sys.argv)==3:
        i=int(sys.argv[2])
        response = deleteTask(i)
        tasks = response[0]
        deletedTask = response[1]
        if deletedTask==None:
            print("Error: task with index #"+str(i)+" does not exist. Nothing deleted.")
        else:
            print("Deleted task #"+str(i))
            writeIntoTask(tasks)
    else:
        print("Error: Missing NUMBER for deleting tasks.")

    
elif sys.argv[1]=="add":
    if len(sys.argv)==4:
        
        tasks = readTask()
        task = sys.argv[3]
        priority = int(sys.argv[2])
        
        for key in tasks:
            if task in tasks[key]:
                tasks[key].remove(task)

        completedTasks = readCompletedTasks()
        if task in completedTasks:
            completedTasks.remove(task)
            writeInToCompleted(completedTasks)
        
        if priority not in tasks.keys():
            tasks[priority] = [task]
            writeIntoTask(tasks)
            print("Added task: "+'"'+sys.argv[3]+'"'+" with priority "+sys.argv[2])
        elif task not in tasks[priority]:
            tasks[priority].append(task)
            writeIntoTask(tasks)
            print("Added task: "+'"'+sys.argv[3]+'"'+" with priority "+sys.argv[2])
    else:
        print("Error: Missing tasks string. Nothing added!")
        
        

