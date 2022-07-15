from panos.firewall import Firewall
import re
import sys

f = open(sys.argv[1], 'r')



fw = Firewall('192.168.1.245', 'admin', 'Asd_12345')

for line in f:
	url = line.strip('\n')
	response = fw.op("<test><url>{}</url></test>".format(url), cmd_xml=False)

	value = response.find('./result').text

	# parse the url category

	content_line = value.split('\n')[1]

	print("{} => {}".format(url, content_line.split(" ")[1]))
