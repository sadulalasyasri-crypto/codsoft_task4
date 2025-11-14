def main():
    tasks=[]
    while True:
        print("\n---- To-Do List ----")
        print("1.Add Task")
        print("2.Show Tasks")
        print("3.Mark Task as Done")
        print("4.Exit")
        ch=input("Enter your choice: ")
        if ch=='1':
            print()
            n_tasks=int(input("How may task you want to add"))
            for i in range(n_tasks):
                task=input("Enter the task: ")
                tasks.append({"task":task,"done":False})
                print("Task added!")
        elif ch=='2':
            print("\nTasks:")
            for index,taask in enumerate(tasks):
                status="Done" if task["done"] else "Not Done"
                print(f"{index+1}.{task['task']}-{status}")
        elif ch=='3':
            task_index=int(input("Enter the task to mark as Done: "))
            if 0<=task_index<len(tasks):
                tasks[task_index]["done"]=True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        elif ch=='4':
            print("Exiting the to-do list.")
        else:
            print("Invalid choice.please try again.")
if __name__=="__main__":
    main()
