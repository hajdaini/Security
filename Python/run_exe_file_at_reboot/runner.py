import subprocess, time, os, sys


def Exec(cmd):
    # Vérifier si la commande existe
    if cmd:
        execproc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        cmdoutput = execproc.stdout.read() + execproc.stderr.read()
        return cmdoutput


def check_privilege():
    # Vérifier si l'utilisateur a accès aux registres
    privilege = Exec('reg query "HKU\S-1-5-19" | find "error"')
    if privilege != b'':
        print("[*] You must be an administrator to run the program\n")
        time.sleep(6)
        sys.exit(1)


def check_OS():
    if os.name == "nt":
        check_privilege()
    else:
        print("[*] Operating system is not Windows.\n")
        time.sleep(6)
        sys.exit(1)


def add_to_Registry(exePath):
    # Vérifier si l'exe existe
    if os.path.isfile(exePath) == False:
        print("[*] Error : Executable not found.\n")
        return False
    name_of_register = "TestHatim"
    Exec('reg ADD HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run /v "' + name_of_register + '" /t REG_SZ /d "' + exePath + '" /F')


os.system('cls')
check_OS()
exePath = input("--> Enter your exe path: ")
add_to_Registry(exePath)
