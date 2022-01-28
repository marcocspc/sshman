from setuptools import setup

setup(
    name = "sshman",
    entry_points = {
        "console_scripts": ['sshman=sshman.sshman_cmd:main']
        },
    packages = ["sshman"],
    version = "0.4",
    license='gpl-3.0',        
    description = "A simple, pure-python, SSH Connection manager.",
    author = "Marco Antonio",
    author_email = "marcocspc@hotmail.com",
    url = "https://github.com/marcocspc/sshman",
  download_url = '',    
  keywords = ['ssh', 'connection', 'manager'],   
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3.0',
    'Programming Language :: Python :: 3',   
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
