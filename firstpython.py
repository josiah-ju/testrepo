# Display the output

import threading
import os

def task1(num):
  print('task1 name : {}' .format(threading.current_thread().name))
  print('task1 id : {}' .format(os.getpid()))
  print('task1 input num : ', num)
  
def task2(num):
  print('task2 name : {}' .format(threading.current_thread().name))
  print('task2 id : {}' .format(os.getpid()))
  print('task2 input num : ', num)
  
if __name__=="__main__":
  
  print('main thread name : {}' .format(threading.main_thread().name))
  print('main thread id : {}' .format(os.getpid()))
  
  t1 = threading.Thread(target=task1, args=(10,), name='Task-1')
  t2 = threading.Thread(target=task2, args=(20,), name='Task-2')
  
  t1.start()
  t2.start()
  
  t1.join()
  t2.join()
  
  print('Done !!!')
