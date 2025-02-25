# ACI Ops
(Pervious know as: Better ACI CLI Tools)
Tools to enhance CLI experience replacing slower ACI show commands with additional information.</br></br>
<strong>WARNING</strong>: Sandbox (sandboxapicdc.cisco.com) for APIC doesn't fully work with ACI Ops, this is due to the fact that the APICs and Fabric are virtual and don't have all the API object returns relating to real equipment.</br></br>
Tested in 4.0(3d), 4.1(2m) and 4.2(1j) APIC/ACI</br>
This program fully supports Python2 and will be updated to Python3 when ACI's internal platform migrates from Python2.</br></br>
The entire program uses Python2 Standard Library!  </br><b>No 3rd party modules to import and update!</b></br>
Program can run on Windows, Mac, and Linux.</br></br>
Can be ran on local computer or on APIC itself.  If on the APIC you can store the program in you home directory.</br>
# New Features!
1.) Picture showing interfaces like available in GUI with colors reflecting interface status, role, errors</br>
2.) Show recent ports down</br>
3.) Show all endpoints on interface</br>
4.) Auto create span to server session</br>
5.) Option to select EGPs to remove from interfaces</br>
6.) Option to tag or untag EPGs added to interfaces</br>
 </br>
# Features in Development!
1.) Clone access, trunk, or VPC/PC to new interfaces [Admin state, EPGs (selection possible), Same Leaf selector]</br>
2.) Deploy Access, Trunk, or VPC/PC (EPGs, physical, AEP) in single flow</br>
3.) Endpoint Search display physical location if endpoint resides on VPC/PC</br>
4.) Display every contract between EPGs (vrf contracts, Taboo, and Normal EPGs) and filters in detail; in both directions</br>
5.) Show all static routes </br>
6.) Interface Description update (Option for csv to change multiple interfaces)</br>
# Screen Shots:
![Image of Main Menu](https://github.com/settlej/Better_ACI_CLI_Tools/blob/master/images/main_menu.JPG)</br></br>
# Important Fault Summary
![Image of fault_summary](https://github.com/settlej/Better_ACI_CLI_Tools/blob/master/images/fault_summary_example.JPG)</br></br>
# Add EPGs to Multiple Interfaces
![Image of add epgs](https://github.com/settlej/Better_ACI_CLI_Tools/blob/master/images/add_vlans.JPG)</br></br>
# Remove EPGs from Multiple Interfaces
![Image of remove_epgs](https://github.com/settlej/Better_ACI_CLI_Tools/blob/master/images/remove_epgs.JPG)</br></br>
# Better 'show interface status'
![Image of showinterfaces](https://github.com/settlej/Better_ACI_CLI_Tools/blob/master/images/show%20interfaces.JPG)</br></br>
# Find Endpoints with Additional Information
![Image of ip search](https://github.com/settlej/Better_ACI_CLI_Tools/blob/master/images/ipsearch.PNG)</br></br>
# Find Endpoints even when Powered Off
![Image of poweroff](https://github.com/settlej/Better_ACI_CLI_Tools/blob/master/images/vm_poweredoff.PNG)</br></br>
# Gather all logs in timeframe
![Image of time](https://github.com/settlej/Better_ACI_CLI_Tools/blob/master/images/time_example.JPG)
</br>Original Auther: Settlej
