'''
rom cx_Freeze import setup, Executable

setup(name = "main" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("__main__.py")])
'''
from distutils.core import setup
import py2exe

setup(console=['__main__.py'])
