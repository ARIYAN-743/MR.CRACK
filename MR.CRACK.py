import os, sys
os.system("git pull")
try:
    __import__("XTX").ARIYAN()
except Exception as e:
    exit(str(e))
