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
    os.system('gnt-instance add --os-type {} --os-size {} --backend-parameters minmem={},maxmem={},vcpus={} --net=0:link={} {}'.format(ostype, disksize, minmem, maxmem, vcpus, network, instancename))

if __name__ == "__main__":
    main(sys.argv)

