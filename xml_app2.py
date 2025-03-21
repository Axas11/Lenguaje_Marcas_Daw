#XML desde archivo

import xml.etree.ElementTree as ET

try:
    xml_file = open('plants.xml')
    if xml_file.readable():
        xml_data = ET.fromstring(xml_file.read())
        lst_plants = xml_data.findall('PLANT')
        print(len(lst_plants))
        for plant in lst_plants:
            print(f"Nombre: {plant.find('COMMON').text}")
            print(f"Botanica: {plant.find('BOTANICAL').text}")
            print("-----------------------------------------")
    else:
        print(False)
except Exception as error:
    print("")
finally:
    xml_file.close()