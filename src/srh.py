import os
import subprocess
os.system("mode con cols=20 lines=2")
def killall():
    subprocess.Popen('powershell.exe -command "(New-Object -comObject Shell.Application).Windows() | foreach-object {$_.quit()}; Get-Process | Where-Object {$_.MainWindowTitle -ne \"\"} | stop-process"')
def restart():
    os.system('shutdown.exe /r /t 00')
def shutdown():
    os.system('shutdown.exe -s -t 00')
def main():
    inp = input('')
    if inp=='0':
        shutdown()
    if inp=='1':
        restart()
    if inp=='k':
        killall()
    else:
        exit()
main()
        