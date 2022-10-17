import threading

globals()['flag2'] = True
globals()['flag1'] = True
def process1():
        
        #Bloqueo por espera en punto muerto
        while globals()['flag2'] == True:
            print('Proceso ',threading.current_thread().getName(),' - en espera')
        print('Proceso ',threading.current_thread().getName(),' - Entrando en sección critica')                        
        globals()['flag1']=False
def process2():

        while globals()['flag1'] == True:
            print('Proceso ',threading.current_thread().getName(),' - en espera')            
        print('Proceso ',threading.current_thread().getName(),' - Entrando en sección critica')            
        globals()['flag2']=False
        
hilo1 = threading.Thread(target=process1)
hilo2 = threading.Thread(target=process2)
hilo1.start()
hilo2.start()