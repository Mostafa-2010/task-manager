import time
import json
import sys
import os
from functions import *



# start-ups:
if not os.path.isfile('data.json'):
    with open('data.json', 'x') as f:
        json.dump({}, f)
        
valid_commands = ['add', 'remove', 'show', 'close', 'clear', 'done']
tasks = {}
task_count = 1
pending_tasks = []
done_tasks = []
with open('data.json', 'r') as f:
    tasks = json.load(f)



print (tasks)

                                                                       #THE MAIN LOOP
while True:                                       
    command = input('♦Enter add, remove, show, close, clear, or done: ')
    command = command.lower().strip()
    if command in valid_commands:
        match command:
            case 'add':
                task_name = input('♦ Type the task you want to add: ').lower().strip()
                add_task(tasks, task_name, task_count)
                task_count = counttasks(tasks, task_count)
                organize(tasks, pending_tasks, done_tasks, task_count)
                print(f'♦ "{task_name}" Was added and saved to your tasks successfuly!')
                time.sleep(2)
                print('♦ Your tasks are now:')
                show_tasks(tasks,pending_tasks, done_tasks, task_count)
                time.sleep(2)
                


            case 'remove':
                task_name = input('♦ Type the task you want to remove: ').lower().strip()
                remove_task(tasks, task_name,  task_count)
                task_count = counttasks(tasks, task_count)
                print(f'"{task_name} has been removed!!"')
                show_tasks(tasks, pending_tasks, done_tasks, task_count)
                time.sleep(2)


            case 'show':
                show_tasks(tasks)
                if bool(tasks) == False:
                    print('Φ You have no tasks!, please add tasks first')

            case 'close':
                print ('--------------------------------------closing the program--------------------------------------')
                close()

            case 'clear':
                tasks = clears(tasks)
                print ('♦ All your tasks has been cleared!')
                save(tasks)

            case 'done':
                task_done = input('Enter the task you have already done: ').lower().strip()
                if task_done in pending_tasks or task_done in done_tasks:
                    pending_tasks.remove(task_done)
                    done_tasks.append(task_done)
                else:
                    print ('♦ The task you want to check as done is not available!!')
                    
                  
    else: 
        print ('♦ Please enter a valid command!!')
        continue
