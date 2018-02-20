# Parser to parse virsh dump xml files

import xml.etree.ElementTree as ET


class VirshXMLParser:

    def __init__(self, xmlfile=None):
        self.root = None
        if xmlfile:
            tree = ET.parse(xmlfile)
            self.root = tree.getroot()

    def get_attrib(self, attr, **args):
        element = self.get_elements(**args)
        if element is None:
            return 'None'
        else:
            return element.get(attr)

    def get_elements(
            self,
            path=None,
            tag=None,
            attrib=None,
            value=None,
            ns={},
            listout=False):
        elements = [self.root]
        search = '.' if not path else path
        if tag:
            search = search + tag
        if attrib and value:
            search = "%s[@%s='%s']" % (search, attrib, value)
        elements = self.root.findall(search, ns)
        if listout:
            return elements
        if elements:
            return elements[0]
        return None

    def get_text(self, **args):
        element = self.get_elements(**args)
        if element is None:
            return 'None'
        else:
            return element.text
