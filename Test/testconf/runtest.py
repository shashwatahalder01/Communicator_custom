import os
from uitlsfunction import readdate, readcounter

reportFolderName = f"{readdate()}_{readcounter()}"
command = f"pytest -s --reruns 500 --reruns-delay 2 testcase/whatsapp/test_whatsapp_07_different_person_different_message.py"
os.system(command)
