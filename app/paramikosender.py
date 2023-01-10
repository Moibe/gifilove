import os
import paramiko

def upload_result(resultado):

    print("Impresión de los resultados desde Paramiko...")
    print(resultado[0]) #GIF
    print(resultado[1]) #APNG
    #print(resultado[2]) #MP4

    ssh = paramiko.SSHClient() 
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect("opal2.opalstack.com", username="moibe", password="Qaonrr_182")
    sftp = ssh.open_sftp()
    print("Conectado a servidor...")
    print("Subiendo gif.")
    sftp.put("./" + resultado[0], "/home/moibe/apps/holocards/" + resultado[0])
    print("Subiendo apng.")
    sftp.put("./" + resultado[1], "/home/moibe/apps/holocards/" + resultado[1])
    #print("Subiendo mp4.")
    #sftp.put("./" + resultado[2], "/home/moibe/apps/holocards/" + resultado[2])
    sftp.close()
    ssh.close()
    print("Cerramos ssh.")