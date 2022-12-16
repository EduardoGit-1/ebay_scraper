import sys
import subprocess

def check_requirements():
    try:
        import bs4
        import pandas
        import requests
        import fuzzywuzzy
    except:
        install_packages()


def install_packages():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "bs4"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "lxml"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "fuzzywuzzy"])