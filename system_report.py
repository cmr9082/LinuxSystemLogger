#!/bin/python3
#Caleb Roberts
#6/21/2023
import subprocess
import datetime as dt

#Gather Data
currentDate = dt.date.today()
hostname = subprocess.check_output(['hostname','-s'])
domainname = subprocess.check_output(['hostname','-d'])
dfGate = str(subprocess.check_output(["ip","r"]))
DNS = str(subprocess.check_output('grep "nameserver" /etc/resolv.conf', shell=True))
OS = str(subprocess.check_output('grep "NAME" /etc/os-release', shell=True))
OSVer = str(subprocess.check_output('grep "VERSION" /etc/os-release', shell=True))
cpuModel = str(subprocess.check_output('lscpu | grep "Model name"', shell=True))
procNum = str(subprocess.check_output('lscpu | grep "CPU(s):"|head -n 1', shell=True))
coreNum = str(subprocess.check_output('lscpu | grep "Core(s)"', shell=True))
memTotal = str(subprocess.check_output(['grep','MemTotal','/proc/meminfo']))
memAvailable = str(subprocess.check_output(['grep','MemAvailable','/proc/meminfo']))
iostat = str(subprocess.check_output('iostat | head -n 1', shell=True))
netInfo = str(subprocess.check_output('ifconfig | head -n 2|tail -n 1', shell=True))
storageInfo = str(subprocess.check_output('iostat | head -n 7|tail -n 1', shell=True))

#Subprocess Strip
hostname = str(hostname)[2:(len(str(hostname))-3)]
domainname = str(domainname)[2:(len(str(domainname))-3)]
DNS = DNS[2:(len(str(DNS))-3)]
OS = OS[2:(len(str(OS))-3)]
OSVer = OSVer[2:(len(str(OSVer))-3)]
storageInfo = storageInfo[2:(len(str(storageInfo))-3)]
cpuModel = cpuModel[2:(len(str(cpuModel))-3)]
procNum = procNum[2:(len(str(procNum))-3)]
coreNum = coreNum[2:(len(str(coreNum))-3)]
memTotal = memTotal[11:(len(str(memTotal))-3)]
memAvailable = memAvailable[15:(len(str(memAvailable))-3)]
iostat = iostat[2:(len(str(iostat))-3)]
netInfo = netInfo[2:(len(str(netInfo))-3)]


#Format Data
dfGate = dfGate[14:27]
cpuModel= cpuModel[21:]
procNum = procNum[21:]
coreNum = coreNum[21:]
OSArr = OS.split('"')
OSVerArr = OSVer.split('"')
iostatArr =iostat.split(' ')
netInfoArr =netInfo.split(' ')
storageInfoArr =storageInfo.split(' ')
DNSArr = DNS.split('\\')
DNS1 = DNSArr[0]
DNS2 = DNSArr[1]

#Setup
subprocess.run('clear', shell=True)
print("         \033[91mSystem Report - "+str(currentDate)+"\033[0m\n")

#Device Info
print("\033[92mDevice Information\033[0m")
print("Hostname: "+hostname)
print("Domain: "+domainname)
print("\n")
#Network Info
print("\033[92mNetwork Information\033[0m")
print("IP Address: "+ netInfoArr[9])
print("Gateway: "+dfGate)
print("Network Mask: "+ netInfoArr[12])
print("DNS1: "+DNS1[11:])
print("DNS2: "+DNS2[12:])
print("\n")
#OS Info
print("\033[92mOS Information\033[0m")
print("Operating System: "+OSArr[1])
print("Operating Version: "+OSVerArr[1])
print("Kernel Version: "+iostatArr[1])
print("\n")
#Storage Info
print("\033[92mStorage Information\033[0m")
print("Hard Drive Capacity: "+storageInfoArr[39]+" kb")
print("Available Space: "+storageInfoArr[35]+" kb")
print("\n")
#Processor Info
print("\033[92mProcessor Information\033[0m")
print("CPU Model: "+cpuModel)
print("Number of Processors: "+procNum)
print("Number of Cores: "+coreNum)
print("\n")
#Memory Info
print("\033[92mMemory Information\033[0m")
print("Total RAM: "+memTotal)
print("Available RAM: "+memAvailable)
print("\n")

#Logging
log = open(hostname+"_system_report.log",'w')
log.write("         System Report - "+str(currentDate)+"\n")
#Device Info
log.write("Device Information\n")
log.write("Hostname: "+hostname+"\n")
log.write("Domain: "+domainname+"\n")
log.write("\n")
#Network Info
log.write("Network Information\n")
log.write("IP Address: "+ netInfoArr[9]+"\n")
log.write("Gateway: "+dfGate+"\n")
log.write("Network Mask: "+ netInfoArr[12]+"\n")
log.write("DNS1: "+DNS1[11:]+"\n")
log.write("DNS2: "+DNS2[12:]+"\n")
log.write("\n")
#OS Info
log.write("OS Information\n")
log.write("Operating System: "+OSArr[1]+"\n")
log.write("Operating Version: "+OSVerArr[1]+"\n")
log.write("Kernel Version: "+iostatArr[1]+"\n")
log.write("\n")
#Storage Info
log.write("Storage Information\n")
log.write("Hard Drive Capacity: "+storageInfoArr[39]+" kb\n")
log.write("Available Space: "+storageInfoArr[35]+" kb\n")
log.write("\n")
#Processor Info
log.write("Processor Information\n")
log.write("CPU Model: "+cpuModel+"\n")
log.write("Number of Processors: "+procNum+"\n")
log.write("Number of Cores: "+coreNum+"\n")
log.write("\n")
#Memory Info
log.write("Memory Information\n")
log.write("Total RAM: "+memTotal+"\n")
log.write("Available RAM: "+memAvailable+"\n")
log.write("\n")
log.close()
