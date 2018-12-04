#!/usr/bin/python3
import shutil
from shutil import move
import os
import subprocess
import re
import sys
import logging

logging.basicConfig(
    filename='backup.log',
    filemode='a',
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt="%H:%M:%S")
    #,stream=sys.stdout)


def runCmd(cmd):
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,shell=True)
    out,err = p.communicate()
    if p.returncode != 0:
        logging.error("Command: {} failed with {}".format(cmd,err))
        return p.returncode,err
    else:
        logging.info("Command: {} ran successfully".format(cmd))
        return p.returncode,out

def main(jenkins,backup_path):

    cmd="find /data/{}/ -path '*/builds/*' -and -not -path '*/timestamper*' -type d -daystart -mtime +30".format(jenkins)
    ret, out = runCmd(cmd)
    if ret != 0:
        sys.exit(ret)
    logging.info("Parse the output of find")
    backup_list = out.split("\n")
    path_pattern = re.compile(r"^/data/{}/jobs/(.*)/.*?$".format(jenkins))
    for item in backup_list:
        path_match = path_pattern.search(item)
        if path_match:
            path = path_match.group(1)
            logging.debug("Checking path "+backup_path+path+" for backup")
            os.makedirs(backup_path+path,exist_ok=True)
            logging.debug("Moving "+item+" to "+backup_path+path)
            try:
                move(item,backup_path+path)
            except shutil.Error:
                logging.error("Could not move item "+item+" to "+backup_path+path)
                break
            #cmd= "cp -r {} {}".format(item,backup_path+path)
            #print(cmd)
            #os.system(cmd)
        #break
    return 0

if __name__== "__main__":
    jenkins_1 = "jenkins_home"
    backup_path_1 = "/mnt/nfs_infra/jenkins_backup/jenkins8080/"
    sys.exit(main(jenkins_1,backup_path_1))
    jenkins_2 = "jenkins_home_ftl"
    backup_path_2 = "/mnt/nfs_infra/jenkins_backup/jenkins8083/"
    sys.exit(main(jenkins_2,backup_path_2))