#!/usr/bin/python

import subprocess
import sys

servers=["node0.myschool.net", "node1.myschool.net", "node2.myschool.net", "node3.myschool.net", "node4.myschool.net", "node5.myschool.net", "node6.myschool.net", "node7.myschool.net"]
#servers=["node7.myschool.net"]

for HOST in servers:
    # Ports are handled in ~/.ssh/config since we use OpenSSH
    COMMAND="systemctl status jamf.tomcat8 --no-pager | grep Active: | awk '{print $3}' | tr -d '()' | tr -d '\n'"

    ssh = subprocess.Popen(["ssh", "-t", "%s" % HOST, COMMAND],
                           shell=False,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        print >>sys.stderr, "ERROR: %s" % error
    else:
        print HOST, " is ", result
