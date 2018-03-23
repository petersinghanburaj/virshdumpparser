
# virshdumpparser

Tool to parse the xml dump for kvm instance.

This is the implemention on python script to parse the xml file generate by "virsh dumpxml <domin-id>"

## Installation Steps

* Follow the below manual steps to install 'virshdumpparser' tool.

```
# Clone the repo
git clone https://github.com/petersinghanburaj/virshdumpparser.git

# Move to the cloned directoy
cd virshdumpparser/

# Install the package
python setup.py install
```

## Usage

> virshdumpparser instance-01 instance-02

or run using wildcard

> virshdumpparser instance-*

## Sample Outputs

* For a normal OpenStack instance.

```
$ virshdumpparser instance-01

Instance detail for file: instance-01
+-------------------------------+----------------------------------------------------------------------------+
| Field                         | Value                                                                      |
+-------------------------------+----------------------------------------------------------------------------+
| Name                          | instance-00000003                                                          |
| Domian Id                     | 1                                                                          |
| Instance UUID                 | 3b7c062f-e049-4d0b-8800-a878a53f1923                                       |
| Instance Name                 | vm001                                                                      |
| Flavor                        | m1.tiny (512  MB, 1 VCPUs, 512 GB)                                         |
| Image ID                      | 441f6ccc-106a-43df-98ff-3b429b1cdc8e                                       |
| CPU Pining                    | None                                                                       |
| Huge Pages                    | None                                                                       |
| No of Interfaces              | 1                                                                          |
| Interface (fa:xx:xx:xx:xx:xx) | Interface Type: bridge                                                     |
|                               | MAC: fa:xx:xx:xx:xx:xx                                                     |
|                               | Driver: qemu                                                               |
|                               | Address Type: pci                                                          |
|                               | Domain: 0x0000                                                             |
|                               | Bus: 0x00                                                                  |
|                               | Slot: 0x03                                                                 |
| No of Disks                   | 1                                                                          |
| Disk (vda)                    | Disk Type: file                                                            |
|                               | Driver Type: qcow2                                                         |
|                               | Device Path: vda                                                           |
|                               | Bus: virtio                                                                |
|                               | Serial No: None                                                            |
|                               | Source:                                                                    |
|                               |    file: /var/lib/nova/instances/3b7c062f-e049-4d0b-8800-a878a53f1923/disk |
|                               |                                                                            |
+-------------------------------+----------------------------------------------------------------------------+
```

* For a OpenStack instance with CPU Pinning and CEPH backend.

```
$ virshdumpparser instance-04-ceph-cpupinning

Instance detail for file: instance-04-ceph-cpupinning
+-------------------------------+--------------------------------------------------------+
| Field                         | Value                                                  |
+-------------------------------+--------------------------------------------------------+
| Name                          | instance-0000000e                                      |
| Domian Id                     | 3                                                      |
| Instance UUID                 | 26dfc33a-f8fc-4043-8816-5daf8a2dc160                   |
| Instance Name                 | jaison-vnf-001                                         |
| Flavor                        | dpdk.s1 (4096  MB, 4 VCPUs, 4096 GB)                   |
| Image ID                      | 5d665498-ecee-4143-83e1-7b7402b20435                   |
| CPU Pining                    | vCPU => CPU                                            |
|                               |   0  =>  10                                            |
|                               |   1  =>  4                                             |
|                               |   2  =>  11                                            |
|                               |   3  =>  5                                             |
| Huge Pages                    | Size: 1048576 KiB                                      |
|                               | Nodeset: 0                                             |
| No of Interfaces              | 1                                                      |
| Interface (fa:xx:xx:xx:xx:xx) | Interface Type: bridge                                 |
|                               | MAC: fa:xx:xx:xx:xx:xx                                 |
|                               | Driver: None                                           |
|                               | Address Type: pci                                      |
|                               | Domain: 0x0000                                         |
|                               | Bus: 0x00                                              |
|                               | Slot: 0x03                                             |
| No of Disks                   | 1                                                      |
| Disk (vda)                    | Disk Type: network                                     |
|                               | Driver Type: raw                                       |
|                               | Device Path: vda                                       |
|                               | Bus: virtio                                            |
|                               | Serial No: None                                        |
|                               | Source:                                                |
|                               |    protocol: rbd                                       |
|                               |    name: vms/26dfc33a-f8fc-4043-8816-5daf8a2dc160_disk |
|                               |                                                        |
+-------------------------------+--------------------------------------------------------+
```

* For a OpenStack instance with DPDK and SR-IOV.

```
$ virshdumpparser instance-05-dpdk instance-06-sriov

Instance detail for file: instance-05-dpdk
+-------------------------------+----------------------------------------------------------------------------+
| Field                         | Value                                                                      |
+-------------------------------+----------------------------------------------------------------------------+
| Name                          | instance-00000005                                                          |
| Domian Id                     | 2                                                                          |
| Instance UUID                 | 14fc2b93-e8e6-43dc-8a21-274659f048f7                                       |
| Instance Name                 | rhel0                                                                      |
| Flavor                        | dpdk.medium (1024  MB, 2 VCPUs, 1024 GB)                                   |
| Image ID                      | 1b89797a-07f4-4730-ac00-f2f8359c0486                                       |
| CPU Pining                    | vCPU => CPU                                                                |
|                               |   0  =>  6,8,10                                                            |
|                               |   1  =>  6,8,10                                                            |
| Huge Pages                    | Size: 1048576 KiB                                                          |
|                               | Nodeset: 0                                                                 |
| No of Interfaces              | 1                                                                          |
| Interface (fa:xx:xx:xx:xx:xx) | Interface Type: vhostuser                                                  |
|                               | MAC: fa:xx:xx:xx:xx:xx                                                     |
|                               | Driver: None                                                               |
|                               | Address Type: pci                                                          |
|                               | Domain: 0x0000                                                             |
|                               | Bus: 0x00                                                                  |
|                               | Slot: 0x03                                                                 |
| No of Disks                   | 1                                                                          |
| Disk (vda)                    | Disk Type: file                                                            |
|                               | Driver Type: qcow2                                                         |
|                               | Device Path: vda                                                           |
|                               | Bus: virtio                                                                |
|                               | Serial No: None                                                            |
|                               | Source:                                                                    |
|                               |    file: /var/lib/nova/instances/14fc2b93-e8e6-43dc-8a21-274659f048f7/disk |
|                               |                                                                            |
+-------------------------------+----------------------------------------------------------------------------+

Instance detail for file: instance-06-sriov
+-------------------------------+--------------------------------------------------------+
| Field                         | Value                                                  |
+-------------------------------+--------------------------------------------------------+
| Name                          | instance-000007f7                                      |
| Domian Id                     | 14                                                     |
| Instance UUID                 | 803949f8-0b32-4577-bb01-d5f50d343fef                   |
| Instance Name                 | rvm1-c1a598e6-af65-448a-8a9e-721088a0cf7a              |
| Flavor                        | SMALL_1 (1024  MB, 1 VCPUs, 1024 GB)                   |
| Image ID                      | 7411ee9f-7147-4f95-af10-dd72e494ff1d                   |
| CPU Pining                    | None                                                   |
| Huge Pages                    | None                                                   |
| No of Interfaces              | 1                                                      |
| Interface (fa:xx:xx:xx:xx:xx) | Interface Type: hostdev                                |
|                               | MAC: fa:xx:xx:xx:xx:xx                                 |
|                               | Driver: vfio                                           |
|                               | Address Type: pci                                      |
|                               | Domain: 0x0000                                         |
|                               | Bus: 0x00                                              |
|                               | Slot: 0x04                                             |
| No of Disks                   | 1                                                      |
| Disk (vda)                    | Disk Type: network                                     |
|                               | Driver Type: raw                                       |
|                               | Device Path: vda                                       |
|                               | Bus: virtio                                            |
|                               | Serial No: None                                        |
|                               | Source:                                                |
|                               |    protocol: rbd                                       |
|                               |    name: vms/803949f8-0b32-4577-bb01-d5f50d343fef_disk |
|                               |                                                        |
+-------------------------------+--------------------------------------------------------+
```
