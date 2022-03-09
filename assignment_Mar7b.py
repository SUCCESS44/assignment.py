#!/home/ojokere/Development/python_project/bin/python
""" simple command line tool that users sys arg"""

import sys

def language(scripting, purpose):
    message = f'{scripting} {purpose}'
    print(message)

if __name__=="__main__":
    scripting = 'Bash'
    purpose =  'Automation'

if "--help" in sys.argv:
    help_message = f'Usage: {sys.argv[0]} --name <NAME> --scripting <SCRIPTING>'
    print(help_message)
    sys.exit()

if "--name" in sys.argv:
    name_index = sys.argv.index('--name') + 1
    if name_index < len(sys.argv):
        purpose = sys.argv[name_index]

if "--scripting" in sys.argv:
    scripting_index = sys.argv.index('--scripting') + 1
    if scripting_index < len(sys.argv):
        scripting = sys.argv[scripting_index]       

language(scripting, purpose)
