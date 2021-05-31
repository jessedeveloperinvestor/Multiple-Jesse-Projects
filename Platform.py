#pip install datetime
import time
import platform
import getpass
machine=str(platform.node())
architecture=str(platform.architecture())
opsys=str(platform.system())
os_vers=str(platform.release())
proces=str(platform.processor())
py_vers=str(platform.python_version())
a='\n'
a1='Machine: '
a2='Architecture: '
a3='OS: '
a4='OS Version: '
a5='Processor: '
a6='Python Version: '
print(a+a1+machine+a+a2+architecture+a+a3+opsys+a+a4+os_vers+a+a5+proces+a+a6+py_vers+a)
print ('Time: '+time.strftime("%Y-%m-%d %H:%M:%S"))
print ('Time am/pm: '+time.strftime("%Y-%m-%d %I:%M:%S"))
print('PC User: '+getpass.getuser())
print('\nYour password is: '+getpass.getpass('Insert your password and hit enter'))