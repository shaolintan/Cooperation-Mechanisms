#!c:\Python26\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ipython==0.13.2','console_scripts','ipython'
__requires__ = 'ipython==0.13.2'
import sys
from pkg_resources import load_entry_point

sys.exit(
   load_entry_point('ipython==0.13.2', 'console_scripts', 'ipython')()
)
