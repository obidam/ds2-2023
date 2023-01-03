# Python environment check-up, don't modify these lines
"""
import httpimport
with httpimport.github_repo('operatorequals', 'covertutils', branch = 'master'):
    import covertutils

import urllib.request
a = urllib.request.urlopen("https://raw.githubusercontent.com/obidam/ds2-2023/main/utils.py")
eval(a.read())
"""
def check_up_env():
    import os
    import warnings
    from IPython import get_ipython
    from subprocess import Popen, PIPE
    import sys

    def execute_this(cmd, prt=True):
        process = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)
        try:
            while True:
                line = process.stdout.readline()
                if not line:
                    break
                if prt:
                    print(line.decode("utf-8"))
                sys.stdout.flush()
            return True
        except:
            print("Error:", sys.exc_info()[0])
            return False

    if 'google.colab' in str(get_ipython()):
        # If we run this notebook at colab.research.google.com, we need to install more packages:
        # !pip install --upgrade dask distributed xarray zarr gcsfs cftime nc-time-axis intake intake-xarray
        warnings.warn(
            "\nRunning on Google Colab\nBe aware that your changes won't be saved unless you save this "
            "Notebooks on your G-Drive")
        execute_this("pip install --upgrade dask distributed xarray zarr gcsfs cftime nc-time-axis intake intake-xarray",
                     prt=False);
    elif os.getenv('BINDER_SERVICE_HOST'):
        warnings.warn("\nRunning on a Binder instance\nBe aware that your changes won't be saved")
    else:
        warnings.warn("\nRunning on your own environment")
