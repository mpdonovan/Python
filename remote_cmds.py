#!/usr/bin/python

import subprocess
import sys

servers=["jss110.killeenisd.org", "jss111.killeenisd.org", "jss112.killeenisd.org", "jss113.killeenisd.org", "jss114.killeenisd.org", "jss115.killeenisd.org", "jss116.killeenisd.org", "jss117.killeenisd.org"]
#servers=["jss117.killeenisd.org"]

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
