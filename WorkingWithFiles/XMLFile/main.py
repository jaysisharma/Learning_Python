import xml.etree.ElementTree as ET


# Writing on a XML file
# Creating an XML element

root = ET.Element('data')

# Creating the child elements inside the root element
child1 = ET.SubElement(root,'item') 
child2 = ET.SubElement(root,'item')
child3 = ET.SubElement(root,'item')

# Appending the values

child1.text = 'Item1'
child2.text = 'Item2'
child3.text = 'Item3'

tree = ET.ElementTree(root)

tree.write('data.xml')

# Reading a XML File


# Parsing the xml file
tree = ET.parse('data.xml')
root = tree.getroot() #getting the root element

for child in root:
    # Printing the text with the tag from the file
    print(child.tag, child.text)


