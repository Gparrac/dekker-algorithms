import threading

globals()['flag2'] = False
globals()['flag1'] = False
def process1():
        #Al intentar entrar llegan a la sección critica y no hay forma de
        # salir debido a su interbloqueo
        while globals()['flag2'] == True :
            print('Proceso ',threading.current_thread().getName(),' - en espera')
        globals()['flag2']= True
        print('Proceso ',threading.current_thread().getName(),' - Entrando en sección critica')            
        globals()['flag2']= False                    
def process2():
        while globals()['flag1'] == True :
            print('Proceso ',threading.current_thread().getName(),' - en espera')            
        globals()['flag2']= True
        print('Proceso ',threading.current_thread().getName(),' - Entrando en sección critica')            
        globals()['flag2']= False
hilo1 = threading.Thread(target=process1)
hilo2 = threading.Thread(target=process2)
hilo1.start()
hilo2.start()