import os
import subprocess
import time

#Criando variáveis
exe = "powershell.exe"
comando = "(Get-ADComputer $env:COMPUTERNAME).DistinguishedName"

#Comando no powershell
retorno = subprocess.run(
    args=[exe, comando],
    capture_output=True,
    shell= True,
    universal_newlines=True)

if(retorno.returncode == 0):
    #Retorno de valores
    print("Retorno: ", retorno.stdout)
    print("Erro: ", retorno.stderr)
    
    #Identificação da OU
    inicio = retorno.stdout.index("OU=") + 3
    fim = retorno.stdout.index(",", inicio + 1)
    
    OU = retorno.stdout[inicio:fim]
    
    print(OU)
    
    #Casos
    match OU:
        case "TI":
            print("Você faz parte do TI")
        case "Administrador":
            print("Você faz parte do Administrador")

