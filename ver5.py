import threading

global flag2, flag1, turno
flag2 = True
flag1 = True
turno = 1
def process1():

        #Dependiendo del turno en el que se encuentre llega a espera
        #hasta que el turno del otro poceso acabe
        while globals()['flag2'] == True:
            if globals()['turno'] == 1:
                  globals()['flag1'] = False
            while globals()['turno'] == 1:
                print('Proceso ',threading.current_thread().getName(),' - en espera')      
            globals()['flag1'] = True            
        print('Proceso ',threading.current_thread().getName(),' - sección critica')                       
        globals()['turno'] = 1
        globals()['flag1'] = False
                                 
def process2():
        while globals()['flag1'] == True:
            if globals()['turno'] == 0:
                  globals()['flag2'] = False
            while globals()['turno'] == 0:
                print('Proceso ',threading.current_thread().getName(),' - en espera')            
            globals()['flag2'] = True  
        print('Proceso ',threading.current_thread().getName(),' - sección critica')                       
        globals()['turno'] = 0
        globals()['flag2'] = False

hilo1 = threading.Thread(target=process1)
hilo2 = threading.Thread(target=process2)
hilo1.start()
hilo2.start()

