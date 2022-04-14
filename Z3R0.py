import socket
import subprocess
 

print("███████╗██████╗░██████╗░░█████╗░ ████████╗███████╗░█████╗░███╗░░░███╗")
print("╚════██║╚════██╗██╔══██╗██╔══██╗ ╚══██╔══╝██╔════╝██╔══██╗████╗░████║")
print("░░███╔═╝░█████╔╝██████╔╝██║░░██║ ░░░██║░░░█████╗░░███████║██╔████╔██║")
print("██╔══╝░░░╚═══██╗██╔══██╗██║░░██║ ░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║")
print("███████╗██████╔╝██║░░██║╚█████╔╝ ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║")
print("╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░ ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝")

conexion = socket.socket()
conexion.bind( ('localhost', 443) )
conexion.listen(1)

while True:
    conexion, addr = conexion.accept()
    print("[+] conexion establecida")
    print("addr")
    conexion.sendfile()
    conexion.close()



    def Army():
     Army = subprocess.call(Army=True)
     Army.call(ipconfig=True)
     Army.call(cd=True)
     Army.call(Tasklist=True)
     Army.call(dir=True)
     Army.call(start=True)
     Army.call(cls=True)
     Army.call(cmd=True)
     Army.call(mkdir=True)
     Army.call(ping=True)