import os

MESSAGE = "The directory already exists"
TARGETDIR = "testdir"

try:
    home = os.path.expanduser(
        "~"
    )
    print(home)
    
    if not os.path.exists(
        os.path.join(home, TARGETDIR)
    ):
        os.makedirs(
            os.path.join(home, TARGETDIR)
        )
    else:
        print(MESSAGE)
except Exception as e:
    print(e)
        

