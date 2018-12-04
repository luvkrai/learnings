import subprocess, select

proc = subprocess.Popen(['locate','a'], bufsize=8192, shell=False, \
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

with open('outpath', "wb") as outf:
    dataend = False
    while (proc.returncode is None) or (not dataend):
        proc.poll()
        dataend = False

        ready = select.select([proc.stdout, proc.stderr], [], [], 1.0)

        if proc.stderr in ready[0]:
            data = proc.stderr.read(1024)
            if len(data) > 0:
                handle_stderr_data(data)

        if proc.stdout in ready[0]:
            data = proc.stdout.read(1024)
            if len(data) == 0: # Read of zero bytes means EOF
                dataend = True
            else:
                outf.write(data)