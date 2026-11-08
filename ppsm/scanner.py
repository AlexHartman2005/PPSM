 # runs nmap / checks it's installed
# can use  shutil, subprocess, add it to requirements.txt?

import shutil, subprocess

#to run the scan: target is the ip you want to scan. 
# i added an optional argument, out_file, where you can specify where you output the file. By default it will output to scan.xml
def run_scan(target: str, out_file: str = "scan.xml") -> str:
    # check if it's there:
    if shutil.which("nmap") is None:
        raise RuntimeError("Nmap not found. Install it from https://nmap.org/download")

    #otherwise, run it.
    # references: https://nmap.org/book/man.html, https://nmap.org/book/man-output.html 
    # basically, -oX outputs to xml, -sV detect the version.
    # we can add more options if needed later. 
    subprocess.run(["nmap", "-sV", "-oX", out_file, target], check=True)
    return out_file