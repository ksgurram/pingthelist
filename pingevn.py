import subprocess
'-------------making a list of IPs-------------'
myiplist = []
with open('iplist.txt') as iplist:
    readiplist = iplist.readlines()
for i in readiplist:
    myiplist.append(i)

for ip in myiplist:
    nslookup = f"nslookup {ip}"
    norespondedlist = []
    try:
        nslookuplist = subprocess.check_output(nslookup, shell = True, text = True, timeout = 10)
        nslookuplist = nslookuplist.split('\n')
        [print(f"DNS name for the {ip} is :{i}") for i in nslookuplist if 'name' in i]
    except subprocess.CalledProcessError:
        norespondedlist.append(ip)
        #print(f"no valid response from DNS for the IP : {ip}")
print(norespondedlist)


finallist = list(map(lambda x:x.strip(), myiplist))
print(finallist)
'------------------------------------------------'
# Command to run
ping_count = input("how many pings:")


# Run the command and capture the output

command = (f"ping -c {ping_count} {ip}")

for ip in finallist:
    command = (f"ping -c {ping_count} {ip}")
    try:
        output = subprocess.check_output(command, shell=True, text=True, timeout=10)
        sai = output.split('\n')
        for i in sai:
            if "0.0% packet loss" in i:
                print(f"ping success with no loss for : {ip}")
    except subprocess.TimeoutExpired:
        print(f"ping failed for : {ip}")
    continue



