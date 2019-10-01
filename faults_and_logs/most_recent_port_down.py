#!/bin//python

import re
try:
    import readline
except:
    pass
import urllib2
import json
import ssl
import os
import datetime
from localutils.custom_utils import *


def askrefresh():
    while True:
        refresh = custom_raw_input("Return to event list? [y=default|n]:  ") or 'y'
        if refresh[0].lower() == 'y':
            return True
        elif refresh[0].lower() == 'n':
            return False
        else:
            continue
    

def gatheranddisplayrecentevents():
    while True:
        #getCookie()
        clear_screen()
        current_time = get_APIC_clock(apic,cookie)
        print("Current time = " + current_time)
        print("\nEvents loading...\n")
        url = """https://{apic}/api/node/class/eventRecord.json?query-target-filter=or(eq(eventRecord.cause,"port-up"),eq(eventRecord.cause,"port-down"),eq(eventRecord.cause,"port-pfc-congested"),eq(eventRecord.cause,"port-security-config-not-supported"),eq(eventRecord.cause,"update-remote-port-to-dbgrelem-failed"),eq(eventRecord.cause,"addor-del-uplink-port-group-failed"),eq(eventRecord.cause,"addor-del-vtep-port-group-failed"),eq(eventRecord.cause,"port-state-change"),eq(eventRecord.cause,"port-pfc-congested"))&order-by=eventRecord.created|desc&page=0&page-size=100""".format(apic=apic)
        result = GetResponseData(url,cookie)
        clear_screen()
        print("Current time = " + current_time)
        print('\n{:>5}   {:26}{:20}{:24}{}'.format('#','Time','Time Difference', 'Port','Event Summary'))
        print('-'*100)
        eventdict = {}
        for num,event in enumerate(result,1):
            if event.get('eventRecord'):
                eventdescr = event['eventRecord']['attributes']['descr'].split()
                eventdescr = ' '.join(eventdescr)
                if len(eventdescr) > 120:
                     summaryeventdescr = eventdescr[:120] + '...'
                else:
                    summaryeventdescr = eventdescr
                eventcreated = ' '.join(event['eventRecord']['attributes']['created'].split('T'))
                eventtrig = event['eventRecord']['attributes']['trig']
                eventuser = event['eventRecord']['attributes']['user']
                eventdn = event['eventRecord']['attributes']['dn']
                eventcode = event['eventRecord']['attributes']['code']
                eventchangeset = event['eventRecord']['attributes']['changeSet']
                if 'eth' in eventdn and not 'extpaths' in eventdn:
                    leaf = re.search(r'(node-[0-9]{1,3})|(paths-[0-9]{1,3})', eventdn).group()
                    if leaf.startswith('paths'):
                        leaf = leaf.replace('paths', 'leaf')
                    elif leaf.startswith('node'):
                        leaf = leaf.replace('node', 'leaf')
                    interface = re.search(r'eth.*\/[0-9]{1,3}\]', eventdn).group()
                    portinterfaces = '{} {}'.format(leaf,interface[:-1])
                elif re.search(r'po[0-9]*\]', eventdn):
                    leaf = re.search(r'node-[0-9]{1,3}', eventdn).group()
                    leaf = leaf.replace('node', 'leaf')
                    interface = re.search(r'po[0-9]*\]', eventdn).group()
                    portinterfaces = '{} {}'.format(leaf,interface[:-1])
                #elif 'rsoosPath' in eventdn and not 'extpaths' in eventdn:
                #    leaf = re.search(r'protpaths-[0-9]{3}-[0-9]{3}', eventdn).group()
                #    leaf = leaf.replace('protpaths', 'VPC node')
                #    interface = re.search(r'pathep-.*\]', eventdn).group()
                #    interface = interface.replace('pathep-', "")
                #    portinterfaces = '{} {}'.format(leaf,interface[:-1])
                #elif 'rsoosPath' in eventdn and 'extpaths' in eventdn:
                #    leaf = re.search(r'paths-[0-9]{3}', eventdn).group()
                #    leaf = leaf.replace('paths','node')
                #    fex = re.search(r'extpaths-.*\]', eventdn).group()
                #    interface = re.search(r'eth[0-9]{1,3}/[0-9]{1,3}', eventdn).group()
                #    portinterfaces = '{} {} {}'.format(leaf,fex,interface)
                else:
                    portinterfaces = ""
                diff_time = time_difference(current_time,eventcreated[:-6])
                eventdict[num] = [eventcreated[:-6],eventcode,eventuser,eventdn,eventdescr,eventchangeset]
                print('{:5}.) {:26}{:20}{:24}{}'.format(num,eventcreated[:-6],diff_time,portinterfaces,summaryeventdescr))
        while True:
            refresh = False
            while True:
                moredetails = custom_raw_input("\nMore details, select number [refresh=Blank and Enter]:  ")
                if moredetails == '':
                    break
                if moredetails.isdigit() and eventdict.get(int(moredetails)):
                    break
                else:
                    print('\x1b[41;1mInvalid, number does not exist...try again\x1b[0m\n') 
            if moredetails == '':
                refresh = True
            if refresh:
                break
            diff_time = time_difference(current_time,eventdict[int(moredetails)][0])
            print('\n\n{:26}{:20}{:18}{:18}{}\n'.format('Time','Time Difference', 'Code','User','Object-Affected'))
            print('-'*120)
            print('{:26}{:20}{:18}{:18}{}'.format(eventdict[int(moredetails)][0],diff_time, eventdict[int(moredetails)][1],eventdict[int(moredetails)][2],'/'.join(str(eventdict[int(moredetails)][3]).split('/')[:-1])))
            print('')
            print('Event Details')
            print('-'*15)
            print(eventdict[int(moredetails)][4])
            print('')
            print('Event ChangeSet')
            print('-'*15)
            print(eventdict[int(moredetails)][5])
            print('\n')
            #refresh = askrefresh()
            #if refresh == True:
            #    continue
            #else:
            #    print('\nEnding Program...\n')
            #    break
        refresh = False
        

def main(import_apic,import_cookie):
    global apic
    global cookie
    cookie = import_cookie
    apic = import_apic
    gatheranddisplayrecentevents()

    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as k:
        print("\n\nExiting Program....")
        exit()
