#XML
#Tag - valor - en arbol - atributos
import xml.etree.ElementTree as ET
user = '''
    <datos>
        <nombre>Angel</nombre>
        <apellido>Peres</apellido>
        <tlfn>+34666356666</tlfn>
        <email hide="yes" />
    </datos>
'''

xml_data = ET.fromstring(user)
print(xml_data)
print(f"Nombre:{xml_data.find('nombre').text}")
print(f"Apellido:{xml_data.find('apellido').text}")
print(f"Telefono:{xml_data.find('tlfn').text}")
print(f"Email:{xml_data.find('email').get('hide')}")