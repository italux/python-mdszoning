#!/usr/bin/python
# gen_smartzones.py - Italo Santos <italux.santos@gmail.com>

import sys
sys.path.append("./library")
import argparse
import ConfigParser

# built-in libraries functions
from time import sleep
from getpass import getuser
from os import path, getenv

# custom libraries
from utils import *
from na_funcs import *
from cisco_funcs import *

# Global

# http://www.cisco.com/c/en/us/td/docs/switches/datacenter/mds9000/sw/6_2/configuration/guides/config_limits/b_mds_9000_configuration_limits_6_2.html
# Table 2 Fabric-level Fibre Channel Configuration Limits
# Note: The preferred number of members per zone is 2, and the maximum recommended limit is 50.
SMARTZONE_MEMBERS_LIMIT = 50

def generate_smartzones(config, zoneset, vsan, fabric, switch=None, check=False, mds=None):

        if switch:
            print bcolors.OKGREEN + "\nGenerating commands to switch %s ... \n" % switch + bcolors.ENDC
        else:
            print bcolors.OKGREEN + "\nGenerating commands to FABRIC %s ... \n" % fabric + bcolors.ENDC
        sleep(3)

        print "config t\n"

        if config.get('device-aliases').get('create') or config.get('device-aliases').get('rename'):
            print "device-alias database"

            for pwwn, hosts in config.get('device-aliases').get('rename').iteritems():
                print "  device-alias rename %s %s" % (hosts.get('from'), hosts.get('to'))

            for pwwn, host in config.get('device-aliases').get('create').iteritems():
                print "  device-alias name %s pwwn %s" % (host, pwwn)

            print "device-alias commit\n"

        for zone, hosts in config.get('hosts_per_zone').iteritems():
            if len(zone) > 1:
                print "zone name %s vsan %s" % (zone.strip(), vsan)
                for host in hosts:
                    print "  member device-alias %s initiator" % host.strip()
                print "exit\n"

        print "zoneset activate name %s vsan %s\n" % (zoneset, vsan)

        print "copy running-config startup-config\n"

def load_config(config_file, fabric):
    """ Prompts yes or no response to user user.
    Returns True for yes and False for no """

    # validate if configuration file path exists
    if not path.exists(config_file):
        raise OSError("%s: file not found" % config_file)

    # load configuration file if something goes wrong
    # an exception will raise and the script will exit
    try:
        config = ConfigParser.ConfigParser()
        config.read(config_file)
    except Exception, e:
        print bcolors.FAIL + "Error reading config file!" + bcolors.ENDC
        print bcolors.BOLD + "Exception:" + bcolors.ENDC + "\n%s" % e
        exit(1)

    configuration = { 'hosts':{}, 'zones': {} }
    hosts_per_zone = {}

    for host in config.sections():
        configuration['hosts'].update({ host: config.get(host, fabric) })
        for zone in config.get(host, 'zones').split(','):
            hosts_per_zone[zone.strip()] = []

    for host in config.sections():
        for zone in config.get(host, 'zones').split(','):
            hosts_per_zone[zone.strip()].append(host)

    configuration.update({ 'zones': hosts_per_zone.keys(),'hosts_per_zone': hosts_per_zone })
    return configuration

if __name__ == "__main__":

    arguments = argparse.ArgumentParser(
        description='Generate SmartZone commands from input config file listing of short hostnames, pwwns and zones which each host will belongs.')
    arguments.add_argument(
        '-c','--config_hosts', required=True, type=str,
        help='Configuration file with hosts, pwwns and zones')
    arguments.add_argument(
        '--vsan', required=True, type=str,
        help='VSAN ID')
    arguments.add_argument(
        '--zoneset', required=True, type=str,
        help='ZoneSet name')
    arguments.add_argument(
        '-f','--fabric', required=True, type=str, choices=['impar', 'par'],
        help='Fabric side')
    arguments.add_argument(
        '--check',default=False, action='store_true',
        help='[optional] Start a validation process by connection on MDS switch of all params')
    arguments.add_argument(
        '-s','--switch', required=False, type=str,
        help='MDS switch fqdn or IP')
    arguments.add_argument(
        '-u','--username', required=False, type=str,
        help='[optional] Username to ssh into mds switch. Alternate: set environment variable MDS_USERNAME. If neither exists, defaults to current OS username') 
    arguments.add_argument(
        '-p','--password', required=False, type=str,
        help='[optional] Password to ssh into mds switch. Alternate: set environment variable MDS_PASSWORD. If unset use_keys defaults to True.') 
    arguments.add_argument(
        '--use_keys', required=False, action='store_true',
        help='[optional] Use ssh keys to log into switch. If set key file will need be pass as param') 
    arguments.add_argument(
        '--key_file', required=False, type=str, 
        help='[optional] filename for ssh key file')

    args = arguments.parse_args()

    config_file = args.config_hosts
    vsan = args.vsan
    zoneset = args.zoneset
    fabric = args.fabric
    switch = None
    config = load_config(config_file, fabric)

    if not args.check:
        # if the argument --check wasn't passed we'll
        # generate the commands without any validation

        aliases = {'rename': {}, 'create': {}}
        
        for host, pwwn in config.get('hosts').iteritems():
            aliases['create'].update({ pwwn: host })

        config.update({ 'device-aliases': aliases })
        
        generate_smartzones(config, zoneset, vsan, fabric)
    else:
        # loading all extra arguments if --check passed
        if args.password :
            use_keys = False
            password = args.password
        elif getenv('MDS_PASSWORD'):
            use_keys = False
            password = getenv('MDS_PASSWORD')
        else :
            use_keys = True
            password = ''

        if args.username :
            username = args.username
        elif getenv('MDS_USERNAME'):
            username = getenv('MDS_USERNAME')
        else:
            username = getuser()

        switch = args.switch

        # define netmiko params to connect to MDS
        mds = {
            'device_type': 'cisco_nxos',
            'ip': switch,
            'verbose': False,
            'username': username,
            'password': password,
            'use_keys': use_keys
        }

        print bcolors.OKGREEN + "Initiate validations ...\n" + bcolors.ENDC
        print bcolors.BOLD + "Validating ZoneSet %s and VSAN ID %s on MDS..." % (zoneset, vsan) + bcolors.ENDC

        zone_set = ZoneSet(mds)
        zoneset_existent = None

        if zone_set.exists(zoneset,vsan):
            zoneset_existent = True

        zone_set.close()

        if zoneset_existent is not True:
            print bcolors.FAIL + "\nZoneSet \"%s\" and/or VSAN ID %s doesn't exists!\nExiting...\n" % (zoneset, vsan) + bcolors.ENDC
            exit(1)

        device_alias = DeviceAlias(mds)
        aliases = {'rename': {}, 'create': {}}

        for host, pwwn in config.get('hosts').iteritems():
            print bcolors.BOLD + "Validating if device-alias exists with pwwn %s on MDS..." % pwwn + bcolors.ENDC
            if device_alias.exists(pwwn):
                alias = device_alias.exists(pwwn)
                if alias != host:
                    aliases['rename'].update({ pwwn: {'from': alias, 'to': host} })
            else:
                aliases['create'].update({ pwwn: host })

        config.update({ 'device-aliases': aliases })

        device_alias.close()

        smartzone = SmartZone(mds)
        non_existent_zones = []
        zone_members = {}

        for zone in config.get('zones'):
            print bcolors.BOLD + "Validating %s on MDS..." % zone.strip() + bcolors.ENDC
            if smartzone.exists(zone, vsan) is False:
                non_existent_zones.append(zone)

            print bcolors.BOLD + "Validating number of members of %s on MDS..." % zone.strip() + bcolors.ENDC
            zone_members[zone] = smartzone.count_members(zone)

        smartzone.close()

        # Checks before generate commands
        zone_over_limit = 0
        for zone, members in zone_members.iteritems():
            if members >= SMARTZONE_MEMBERS_LIMIT:
                zone_over_limit += 1
                print bcolors.FAIL + "Zone \"%s\" has more then %d members (%s)" % (zone.strip(), SMARTZONE_MEMBERS_LIMIT, members) + bcolors.ENDC

        if zone_over_limit > 0:
            if confirm("Are you sure you want to continue?"):
                pass
            else:
                print "Exiting..."
                exit(1)

        if len(non_existent_zones) > 0:
            print bcolors.WARNING + "\n### ATENTION! Some Zone(s) doesn't exists ... ###\n" + bcolors.ENDC
            for zone in non_existent_zones:
                print bcolors.FAIL + "Zone \"%s\" doesn't exists!" % zone.strip() + bcolors.ENDC

            if confirm("Are you sure you want to continue?"):
                pass
            else:
                print "Exiting..."
                exit(1)
        
        generate_smartzones(config, zoneset, vsan, fabric, switch=switch, check=True, mds=mds)
