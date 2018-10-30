import wmi

GB = 1073741824  # bytes 2 GB convert

# computerName = input(r"\\")

computerName = 'dtpolbn7004'
c = wmi.WMI(computerName)


def wmi_zapytanie(wmi_value, wmi_class):
    wql = ("SELECT " + wmi_value + " FROM " + wmi_class)
    for result in c.query(wql):
        print(getattr(result, wmi_value))


wmi_zapytanie('serialnumber', 'win32_bios')
