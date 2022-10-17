
import threading
import time

globals()['turno'] = 1
def process1():
    #Problema al generar dependencia entre el tiempo de los procesos
    while globals()['turno'] != 1:
        print('Proceso ',threading.current_thread().getName(),' - espera...')            
    print('Proceso ',threading.current_thread().getName(),' - ejecutando sección critica!!!')            
    time.sleep(2)
    globals()['turno'] = 2
def process2():
    while globals()['turno'] != 2:
        print('Proceso ',threading.current_thread().getName(),' - espera...')            
    print('Proceso ',threading.current_thread().getName(),' - ejecutando sección critica!!!')            
    globals()['turno'] = 1
hilo1 = threading.Thread(target=process1)
hilo2 = threading.Thread(target=process2)
hilo1.start()
hilo2.start()    