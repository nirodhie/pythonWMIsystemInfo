import math
import subprocess

import wmi

GB = 1073741824  # bytes 2 GB convert

# computerName = input(r"\\")

computerName = 'dtpolbn7004'
c = wmi.WMI(computerName)


def wmi_zapytanie(wmi_value, wmi_class):
    wql = ("SELECT " + wmi_value + " FROM " + wmi_class)
    for result in c.query(wql):
        print(getattr(result, wmi_value))


def wmi_zapytanie_GB(wmi_value, wmi_class):
    wql = ("SELECT " + wmi_value + " FROM " + wmi_class)
    for result in c.query(wql):
        print(math.ceil(int(getattr(result, wmi_value)) / GB))


wmi_zapytanie('serialnumber', 'win32_bios')
wmi_zapytanie('SMBIOSBIOSVersion', 'win32_bios')
wmi_zapytanie('OSArchitecture', 'win32_OperatingSystem')
wmi_zapytanie('model', 'win32_COMPUTERSYSTEM')
wmi_zapytanie('vendor', 'win32_COMPUTERSYSTEMproduct')
wmi_zapytanie('username', 'win32_COMPUTERSYSTEM')
wmi_zapytanie('NumberOfCores', 'Win32_Processor')
wmi_zapytanie('NumberOfLogicalProcessors', 'Win32_Processor')
wmi_zapytanie('name', 'Win32_Processor')
wmi_zapytanie_GB('size', 'Win32_diskdrive')
wmi_zapytanie('caption', 'Win32_diskdrive')
wmi_zapytanie('serialnumber', 'Win32_diskdrive')


def bitlocker_key(linenumber):
    process1 = subprocess.Popen(['cmd.exe', '/c', 'manage-bde', '-protectors', 'C:', '-get'], stdout=subprocess.PIPE)
    output_as_list = []
    for line in process1.stdout:
        output_as_list.append(str(line).replace(r"\r\n'", "").replace("b'", "").replace("None", ""))
    # print('\n'.join(output_as_list))
    return output_as_list[linenumber]


print(bitlocker_key(9).lstrip())
