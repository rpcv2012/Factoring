from setuptools import setup, find_packages

setup(name='factoringtemp',
      version='0.1',
      description='factoring numbers',
      #url='http://github.com/storborg/funniest',
      author='TR',
      #author_email='flyingcircus@example.com',
     # license='MIT',
      packages=find_packages(),
      zip_safe=False)

#packages=['factoringtemp'],


##sources for "setup"
##Partly from here:
##    https://python-packaging.readthedocs.io/en/latest/minimal.html
##    modified by "Minimal example" from here:
##        https://stackoverflow.com/questions/4740473/setup-py-examples



##from setuptools import setup, find_packages
##
##VERSION = '0.0.1' 
##DESCRIPTION = 'My Python package for factoring'
##LONG_DESCRIPTION = 'My Python package for factoring numbers'
##
### Setting up
##setup(
##       # the name must match the folder name 'verysimplemodule'
##        name="factoringtemp", 
##        version=VERSION,
##        author="TR",
##        #author_email="<youremail@email.com>",
##        #description=DESCRIPTION,
##        #long_description=LONG_DESCRIPTION,
##        packages=['factoringtemp'])
        #install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
##        keywords=['python', 'first package'],
##        classifiers= [
##            "Development Status :: 3 - Alpha",
##            "Intended Audience :: Education",
##            "Programming Language :: Python :: 2",
##            "Programming Language :: Python :: 3",
##            "Operating System :: MacOS :: MacOS X",
##            "Operating System :: Microsoft :: Windows",



       # packages=find_packages(),
##        ]
#)


##some useful pip commands
##python 3 on windows:
##    py -3 -m ensurepip
##    py -3 -m pip install factoringtemp
