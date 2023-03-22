# this script will check to see if all of the environment variables I require are set

import os

# set the variable confdir from the os environment variable
confdir = os.getenv(
    "my_config"
)

# set the variable conffile
conffile = "env_check.conf"
# set the variable conffilename by joining confdir and conffile together
conffilename = os.path.join(confdir, conffile)

# open the config file and read all the settings
for env_check in open(conffilename):
    # set the variable as itself, but strip the extra text out
    env_check = (
        env_check.strip()
    )
    print("[{}]".format(env_check)) # format the output to be in square brackets
    # set the variable newenv to get the settings from the OS what is currently set for the settings out the configfile
    newenv = os.getenv(env_check)

    if newenv is None: # if it doesn't exist
        print(env_check, "is not set") # print it is not set
    else: # else if it does exist
        # print out the details
        print(
            "Current setting for {}={}\n".format(env_check, newenv)
        )
