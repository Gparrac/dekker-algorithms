import threading
import time

globals()['flag2'] = True
globals()['flag1'] = True
def process1():
        
        #llega a punto muerto en espera
        while globals()['flag2'] == True :
            print('Proceso ',threading.current_thread().getName(),' - en espera')
            time.sleep(2)                  
        print('Proceso ',threading.current_thread().getName(),' - Sección critica')
        globals()['flag2'] = False            
                          
def process2():
        
        while globals()['flag1'] == True :            
            print('Proceso ',threading.current_thread().getName(),' - en espera')            
            time.sleep(2)
        print('Proceso ',threading.current_thread().getName(),' - Sección critica')
        globals()['flag1'] = False   
        
hilo1 = threading.Thread(target=process1)
hilo2 = threading.Thread(target=process2)
hilo1.start()
hilo2.start()