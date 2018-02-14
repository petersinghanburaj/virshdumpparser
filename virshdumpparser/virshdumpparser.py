# Parser to parse virsh dump xml files

import sys
import xml.etree.ElementTree as ET
from terminaltables import AsciiTable


def main():
# Main function which will be called
# to parse the list of xml files.

    import pdb; pdb.set_trace()
    for xmlfile in sys.argv[1:]:

        # create element tree object
        tree = ET.parse(xmlfile)
        table_data = []
        table_data.append(['Field', 'Value'])

        # get root element
        root = tree.getroot()

        #for child in root:
        #    print(child.tag, child.attrib)

        table_data.append(['Name', get_text(root, tag='name')])

        table_data.append(['Domian Id', get_attrib(root, 'id')])

        #table_data.append(['Instance UUID', get_text(root, path='sysinfo/system/entry', attrib='name', value='uuid')])
        table_data.append(['Instance UUID', get_text(root, tag='uuid')])
        

        ns = {'nova': "http://openstack.org/xmlns/libvirt/nova/1.0"}
        
        name = get_text(root, path='.//', tag='nova:name', ns=ns)
        table_data.append(['Instance Name', name])
        
        flavor_name = get_attrib(root, 'name', path='.//', tag='nova:flavor', ns=ns)
        flavor_disk = get_text(root, path='.//', tag='nova:memory', ns=ns)
        flavor_vcpu = get_text(root, path='.//', tag='nova:vcpus', ns=ns)
        flavor_memory = get_text(root, path='.//', tag='nova:memory', ns=ns)
        #flavor = flavor_name + ' (' + flavor_memory + ' MB, ' + flavor_vcpu + ' VCPUs, ' + flavor_disk + ' GB) '
        flavor = "%s (%s  MB, %s VCPUs, %s GB)" %(flavor_name, flavor_memory, flavor_vcpu, flavor_disk)
        table_data.append(['Flavor', flavor])
        
        image = get_attrib(root, 'uuid', path='.//', tag='nova:root', ns=ns)
        table_data.append(['Image ID', image])

        
        interfaces = get_elements(root, path='./devices/', tag='interface', listout=True)
        table_data.append(['No of Interfaces', len(interfaces)])

        for interface in interfaces:
            itype = get_attrib(interface, 'type')
            mac = get_attrib(interface, 'address', tag='mac')
            driver = get_attrib(interface, 'name', tag='driver')
            atype = get_attrib(interface, 'type', tag='address')
            domain = get_attrib(interface, 'domain', tag='address')
            bus = get_attrib(interface, 'bus', tag='address')
            slot = get_attrib(interface, 'slot', tag='address')
            iname = "Interface (%s)" %(mac)
            idetails = "Interface Type: %s\nMAC: %s\nDriver: %s\nAddress Type: %s\nDomain: %s\nBus: %s\nSlot: %s" %(itype, mac, driver, atype, domain, bus, slot)
            #idetails = "\033[32mInterface Type: %s\nMAC: %s\nDriver: %s\nAddress Type: %s\nDomain: %s\nBus: %s\nSlot: %s\n\033[0m" %(itype, mac, driver, atype, domain, bus, slot)
            table_data.append([iname, idetails])


        disks = get_elements(root, path='./devices/', tag='disk', listout=True)
        table_data.append(['No of Disks', len(disks)])

        for disk in disks:
            dtype = get_attrib(disk, 'type')
            drtype = get_attrib(disk, 'type', tag='driver')
            target = get_attrib(disk, 'dev', tag='target')
            bus = get_attrib(disk, 'bus', tag='target')
            serial = get_text(disk, tag='serial')
            dname = "Disk (%s)" %(target)
            ddetails = "Disk Type: %s\nDriver Type: %s\nDevice Path: %s\nBus: %s\nSerial No: %s" %(dtype, drtype, target, bus, serial)

            source = get_elements(disk, tag='source')
            source_attrib = ''
            for attrib in source.keys():
                source_attrib += "   %s: %s\n" %(attrib, source.get(attrib))
            ddetails += "\nSource: \n%s" %(source_attrib)

            table_data.append([dname, ddetails])

        #print(get_text(root))
        #print (get_text(root, tag='name'))
        #print (get_text(root, path='./sysinfo/system/entry', attrib='name', value='uuid'))
        #print (get_text(root, path='metadata/nova:instance/nova:name'))

        #root.find('sysinfo').find('system').findall('entry')
        #get_element(root, 'sysinfo')
        #get_element(root, 'system')
        #get_element(root, 'entry')

        #obj = root.find('sysinfo/system/entry')
        #print(obj.tag, obj.attrib)


        #print("Name of Instance is : ", name )

        #devices = root.find('devices')
        #for device in devices:
        #    print(device.tag, device.attrib)

        #print(table_data)
        #ele = get_element(root, tag='metadata')
        #print(ele)
        #print(instance)

        print("\n\nInstance details of file: %s " %(xmlfile))
        table = AsciiTable(table_data)
        print(table.table)


def get_attrib(element, attr, **args):
    element = get_elements(element, **args)
    if element is None:
        return 'None'
    else:
        return element.get(attr)

def get_elements(element, path=None, tag=None, attrib=None, value=None, ns={}, listout=False):
    elements = [element]
    #if not path:
        #elements = element.findall(path)
    search = '.' if not path else path
    if tag:
        #elements = element.findall(tag)
        search = search + tag
    if attrib and value:
        #search = search + '[@'+attrib+'=\''+value+'\']'
        search = "%s[@%s='%s']" %(search, attrib, value)
    #print(search)
    elements = element.findall(search, ns)
        #element.findall(".//entry[@name=uuid]")
        #for ele in elements:
        #    if get_attrib(ele, attrib) != value:
        #        elements.remove(ele)
    if listout:
        return elements
    if elements:
        return elements[0]
    return None

def get_text(element, **args):
    element = get_elements(element, **args)
    if element is None:
        return 'None'
    else:
        return element.text

if __name__ == "__main__":
 
    # calling main function
    main()
