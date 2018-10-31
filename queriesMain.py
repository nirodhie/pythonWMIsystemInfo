import math
import subprocess

import wmi

GB = 1073741824  # bytes 2 GB convert

# computerName = input(r"\\")

computerName = '.'
c = wmi.WMI(computerName)


def wmi_zapytanie(wmi_value, wmi_class):
    wql = ("SELECT " + wmi_value + " FROM " + wmi_class)
    for result in c.query(wql):
        return(getattr(result, wmi_value))


def wmi_zapytanie_GB(wmi_value, wmi_class):
    wql = ("SELECT " + wmi_value + " FROM " + wmi_class)
    for result in c.query(wql):
        return(math.ceil(int(getattr(result, wmi_value)) / GB))

print(wmi_zapytanie('vendor', 'win32_COMPUTERSYSTEMproduct'),wmi_zapytanie('model', 'win32_COMPUTERSYSTEM'))
print('Service tag',wmi_zapytanie('serialnumber', 'win32_bios'))
print('BIOS version',wmi_zapytanie('SMBIOSBIOSVersion', 'win32_bios'))
print(wmi_zapytanie('OSArchitecture', 'win32_OperatingSystem'),'system')
print('Logged in user',wmi_zapytanie('username', 'win32_COMPUTERSYSTEM'))
print(wmi_zapytanie('name', 'Win32_Processor'))
print('with',wmi_zapytanie('NumberOfCores', 'Win32_Processor'),'cores and ',wmi_zapytanie('NumberOfLogicalProcessors', 'Win32_Processor'),'logical processors')
print('Attached disks:')
print(wmi_zapytanie('caption', 'Win32_diskdrive'),'has total capacity of',wmi_zapytanie_GB('size', 'Win32_diskdrive'),'GB and',wmi_zapytanie('serialnumber', 'Win32_diskdrive'),'serial number')


percentFreeSpace = math.ceil((wmi_zapytanie_GB('freespace','win32_logicaldisk')/(wmi_zapytanie_GB('size', 'Win32_diskdrive')))*100)

print('C: has',wmi_zapytanie_GB('freespace','win32_logicaldisk'),'GB free,which is',percentFreeSpace, '%')
print("RAM:")


def bitlocker_key(linenumber):
    process1 = subprocess.Popen(['cmd.exe', '/c', 'manage-bde', '-protectors', 'C:', '-get'], stdout=subprocess.PIPE)
    output_as_list = []
    for line in process1.stdout:
        output_as_list.append(str(line).replace(r"\r\n'", "").replace("b'", "").replace("None", ""))
    # print('\n'.join(output_as_list))
    return output_as_list[linenumber]


# print(bitlocker_key(9).lstrip())
