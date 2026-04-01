import time
import json

# FUNCTIONS
def save(tasks):
    with open('data.json', 'w') as f:
        json.dump(tasks, f, indent=4)
        print(tasks, 'those are the saved data')
        
def close():
    save(tasks)
    time.sleep(5)
    sys.exit(0)
    exit()

def counttasks(tasks, task_count):
    task_count = len(tasks)+1    #to create the next item with correct order
    return task_count

def add_task(tasks, task, task_count):
    str(task_count)    #to prevent errors and duplication as json return int as str
    print(type(tasks.keys))
    tasks[task_count]= {'task':task, 'done':False}
    save(tasks)

    

def remove_task(tasks, task, task_count):
    if task in remove:
        del tasks[task_count['task']]    
        save(tasks)
        return tasks
        
    else:
        return '♦ The task you want to remove is unavailable!'
        time.sleep(2)


def show_tasks(tasks,pending_tasks, done_tasks, task_count):
    with open('data.json', 'r') as f:
        json.load(f)
        for task in tasks.values():
            if task['task'] in pending_tasks:
                print (f'    ○ {task["task"]}')
                time.sleep(0.5)
            else:
                print(f'     • {task["task"]}    (task done!)')
            

def clears(tasks):
    tasks.clear()
    save(tasks)
    return tasks

def organize(tasks, pending_tasks, done_tasks, task_count):     # Will be used in the next version
    for task in tasks.values():
        if task['done'] == False:
            pending_tasks.append(task['task'])
        else:
            if task['task'] in pending_tasks:
                pending_tasks.remove(task['task'])
            done_tasks.append(task['task'])
        continue
