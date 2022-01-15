import re
import argparse

mobaline = "%22%[Work]%%-1%-1%%%%%-1%0%0%_ProfileDir_\.ssh\id_rsa%%0%0%0%0%%1080%%0%0%0#JetBrains Mono%10%0%0%-1%15%236,236,236%30,30,30%180,180,192%0%-1%0%%xterm%-1%-1%_Std_Colors_0_%80%24%0%1%-1%<none>%%0%0%-1#0# #-1"

parser = argparse.ArgumentParser(description='Find and replace')

parser.add_argument('-i', '--ansible', type=argparse.FileType('r'),
                    required=True, help='ansible inventory')
parser.add_argument('-o', '--out', help='output file', required=False)


args = parser.parse_args()

print('Ansible inventory: ' + args.ansible.name +
      ' Encoding: ' + args.ansible.encoding)
print('Out file: ' + args.out)

with open(args.ansible.name, args.ansible.mode, encoding='UTF-8') as file:
    data = file.read()

rename = re.compile("\d\w{2,}-s-\w{3,}")
readdr = re.compile("host=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

name = re.findall(rename, data)
ipaddr = re.findall(readdr, data)

if args.out is not None:
    with open(args.out, 'w', encoding='UTF-8') as file:
        for x in range(len(ipaddr)):
            line = re.sub(r"\w*-s-", "", name[x]) + "=#109#0%" + \
                ipaddr[x].lstrip("host=") + f"{mobaline}\n"
            file.write(line)
else:
    for x in range(len(ipaddr)):
        line = re.sub(r"\w*-s-", "", name[x]) + "=#109#0%" + ipaddr[x].lstrip("host=") + f"{mobaline}\n"
        print(line)
