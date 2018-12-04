#~/bin/python

from pexpect import pxssh
for i in range(4,16):
 try:
    s = pxssh.pxssh(timeout=1)
    server_name = "uls-ep-swtools-%s" % str(i).zfill(2)
    s.login(server_name, "root", "Coolbeans!")
    #s.sendline('ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | awk \'{ print $2 }\' | cut -f2 -d: | head -1')   # run a command
    print("Server: "+server_name+"\n")
    s.sendline("""
cat >/etc/netplan/50-cloud-init.yaml <<EOL
# This file is generated from information provided by
# the datasource.  Changes to it will not persist across an instance.
# To disable cloud-init's network configuration capabilities, write a file
# /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with the following:
# network: {config: disabled}
network:
  version: 2
  renderer: networkd
  ethernets:
      ens3f0:
          addresses: []
          dhcp4: false
          optional: true
      ens3f1:
          addresses: []
          dhcp4: false
          optional: true
  bonds:
    bond0:
      dhcp4: yes
      interfaces:
        - ens3f0
        - ens3f1
      parameters:
        mode: 802.3ad
        primary: ens3f0
        lacp-rate: fast
        mii-monitor-interval: 100
EOL""")
    s.sendline("netplan apply")
    s.prompt()             # match the prompt
    s.logout()
 except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
 except Exception as e:
    print("done")