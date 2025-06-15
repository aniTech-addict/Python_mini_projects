import os
import subprocess

#subprocess.run("py main.py", shell=True)

path = os.path.join("..","Currency_converter_app","main.py")
subprocess.run(["python",path])