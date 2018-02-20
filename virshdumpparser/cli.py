import sys
from virshdumpparser import parser
from terminaltables import AsciiTable

def main():
# Main function which will be called
# to parse the list of xml files.

    for xmlfile in sys.argv[1:]:

        # create element tree object
        #tree = ET.parse(xmlfile)
        # get root element
        #root = tree.getroot()
        VXMLP = parser.VirshXMLParser(xmlfile)

        table_data = []
        table_data.append(['Field', 'Value'])


        table_data.append(['Name', VXMLP.get_text(tag='name')])

        table_data.append(['Domian Id', VXMLP.get_attrib('id')])

        table_data.append(['Instance UUID', VXMLP.get_text(tag='uuid')])
        

        ns = {'nova': "http://openstack.org/xmlns/libvirt/nova/1.0"}
        name = VXMLP.get_text(path='.//', tag='nova:name', ns=ns)
        table_data.append(['Instance Name', name])
        
        flavor_name = VXMLP.get_attrib('name', path='.//', tag='nova:flavor', ns=ns)
        flavor_disk = VXMLP.get_text(path='.//', tag='nova:memory', ns=ns)
        flavor_vcpu = VXMLP.get_text(path='.//', tag='nova:vcpus', ns=ns)
        flavor_memory = VXMLP.get_text(path='.//', tag='nova:memory', ns=ns)
        flavor = "%s (%s  MB, %s VCPUs, %s GB)" %(flavor_name, flavor_memory, flavor_vcpu, flavor_disk)
        table_data.append(['Flavor', flavor])
        
        image = VXMLP.get_attrib('uuid', path='.//', tag='nova:root', ns=ns)
        table_data.append(['Image ID', image])

        
        interfaces = VXMLP.get_elements(path='./devices/', tag='interface', listout=True)
        table_data.append(['No of Interfaces', len(interfaces)])

        InterfaceVXMLP = parser.VirshXMLParser()
        for interface in interfaces:
            InterfaceVXMLP.root = interface
            itype = InterfaceVXMLP.get_attrib('type')
            mac = InterfaceVXMLP.get_attrib('address', tag='mac')
            driver = InterfaceVXMLP.get_attrib('name', tag='driver')
            atype = InterfaceVXMLP.get_attrib('type', tag='address')
            domain = InterfaceVXMLP.get_attrib('domain', tag='address')
            bus = InterfaceVXMLP.get_attrib('bus', tag='address')
            slot = InterfaceVXMLP.get_attrib('slot', tag='address')
            iname = "Interface (%s)" %(mac)
            idetails = "Interface Type: %s\nMAC: %s\nDriver: %s\nAddress Type: %s\nDomain: %s\nBus: %s\nSlot: %s" %(itype, mac, driver, atype, domain, bus, slot)
            table_data.append([iname, idetails])


        disks = VXMLP.get_elements(path='./devices/', tag='disk', listout=True)
        table_data.append(['No of Disks', len(disks)])

        DiskVXMLP = parser.VirshXMLParser()
        for disk in disks:
            DiskVXMLP.root = disk
            dtype = DiskVXMLP.get_attrib('type')
            drtype = DiskVXMLP.get_attrib('type', tag='driver')
            target = DiskVXMLP.get_attrib('dev', tag='target')
            bus = DiskVXMLP.get_attrib('bus', tag='target')
            serial = DiskVXMLP.get_text(tag='serial')
            dname = "Disk (%s)" %(target)
            ddetails = "Disk Type: %s\nDriver Type: %s\nDevice Path: %s\nBus: %s\nSerial No: %s" %(dtype, drtype, target, bus, serial)

            source = DiskVXMLP.get_elements(tag='source')
            source_attrib = ''
            for attrib in source.keys():
                source_attrib += "   %s: %s\n" %(attrib, source.get(attrib))
            ddetails += "\nSource: \n%s" %(source_attrib)

            table_data.append([dname, ddetails])

        print("\n\nInstance details of file: %s " %(xmlfile))
        table = AsciiTable(table_data)
        print(table.table)



if __name__ == "__main__":
 
    # calling main function
    sys.exit(main())
