class Todolist():
    def __init__(self):
        self.task=[]
        def Adding_new_Task(self,task):
            if task:
                list1={"task":task,"done":False}
                self.task.append(list1)
                print(f"Task {task} has added successfully to list")
            else:
                print("enter valid task")
        def Removing_the_existing_task(self,task):
            for t in task:
                if t["task"]==task:
                    self.task.remove(t)
                    print("entered Task has removed sussessfully")
                    return
            print("task is not found")
        def Display_the_task(self,task):
            if task:
                print("your TO-DO-LIST")
                for index,task in enumerate(self,start=1):
                    status="Done" if task["done"] else "not done"
                    print(f"{index}.{task["task"]}-{status}")
            else:
                print("your TO-DO-LIST is empty")
        def Task_marks_complete(self):
            task_index=int(input("enter the task number to be marked as done"))-1
            if 0<=task_index<len(self.task):
                self.task[task_index]["done"]=True
                print("entered task has been marked as done")
            else:
                print("invalid task number")
        def main():
            toDo_list=Todolist()
            while True:
                print("\n choose an choice")
                print("1.add task")
                print("2.remove task")
                print("3.display task")
                print("4.mark task as complete")
                print("5.exit")
                choice=input("enter your choice:")
                if choice=="1":
                    task=input("enter the task to add:")
                    toDo_list.Adding_new_Task(task)
                elif choice=="2":
                    task=input("enter task to remove:")
                    toDo_list.Removing_the_existing_task(task)
                elif choice=="3":
                    toDo_list.Display_the_task()
                elif choice=="4":
                    toDo_list.Task_marks_complete(None)
                elif choice=="5":
                    print("exiting app")
                    break
                else:
                    print("invalid choice please enter valid option")
        main()

