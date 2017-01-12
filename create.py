#!/usr/bin/python

import sys, os, yaml

def main(argv):
    if len(sys.argv) < 2:
        print('No config file provided. Exiting...') 
        exit(1)
    with open(sys.argv[1], 'r') as f:
        instances = yaml.load(f)
    for group, instance in instances.items():
        print('Installing {} instances'.format(group))
        for name, options in instance.items():
            instancename = name
            network = options["network"]
            ostype = options["ostype"]
            disksize = options["disksize"]
            minmem = options["minmem"]
            maxmem = options["maxmem"]
            vcpus = options["vcpus"]
            node_group = options["node-group"]
            disk_template = options["disk-template"]
    os.system('gnt-instance add --os-type {} --os-size {} --backend-parameters minmem={},maxmem={},vcpus={} --net=0:link={} --disk-template {} --node-group {} {}'.format(ostype, disksize, minmem, maxmem, vcpus, network, disk_template, node_group, instancename))

if __name__ == "__main__":
    main(sys.argv)

