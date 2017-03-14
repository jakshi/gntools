#!/usr/bin/python

from __future__ import print_function
import sys, os, yaml


def query_yes_no(question, default="yes"):
    # raw_input returns the empty string for "enter"
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])

    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        try:
            choice = raw_input().lower()
        except NameError:
            choice = input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            sys.stdout.write("Please respond with 'yes' or 'no'")

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
            virtualization = options["virtualization"]
            install = option["install"]
            if virtualization == "kvm":
                virtualization_switch = "-H kvm"
            else:
                virtualization_switch = ""
            if install == false:
                install_switch = "--no-install"
            else:
                install_switch = ""

        ganeti_command = 'gnt-instance add {} {} --os-type {} --os-size {} --backend-parameters minmem={},maxmem={},vcpus={} --net=0:link={} --disk-template {} --node-group {} {}'.format(virtualization_switch, install_switch, ostype, disksize, minmem, maxmem, vcpus, network, disk_template, node_group, instancename)
        print('Instance name {} creation plan:\nVirtualization type: {}\nOS type: {}\nInstall OS? {}}\nNode Group: {}\nDisk type: {}\nCPUs: {}\nMaxMem: {}\nMinMem: {}\nRoot disk size: {}\nNetwork: {}'.format(name, virtualization, ostype, install, node_group, disk_template, vcpus, maxmem, minmem, disksize, network))
        print('Ganeti commmand that will be executed:\n{}'.format(ganeti_command))
        if query_yes_no('Proceed?','no'):
            os.system(ganeti_command)

if __name__ == "__main__":
    main(sys.argv)

