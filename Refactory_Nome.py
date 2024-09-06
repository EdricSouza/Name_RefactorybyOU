import os
import subprocess
import time

exe = "powershell.exe"
comando = "(Get-ADComputer $env:COMPUTERNAME).DistinguishedName"

retorno = subprocess.run(
    args=[exe, comando],
    capture_output=True,
    shell= True,
    universal_newlines=True)

print("Retorno: ", retorno.stdout)
print("Erro: ", retorno.stderr)
print("Returno do código: ", retorno.returncode)



