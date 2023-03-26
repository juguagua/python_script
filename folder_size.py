# this will scan the current directory and all subdirectories and display the size

import os
import sys

try:
    directory = sys.argv[1]

except IndexError:
    sys.exit("Must provide an argument")

dir_size = 0
fsizedicr = {
    "Bytes": 1,
    "Kilobytes": float(1) / 1024,
    "Megabytes": float(1) / (1024 * 1024),
    "Gigabytes": float(1) / (1024 * 1024 * 1024),
}

# Walk through all the directories
for (path, dirs, files) in os.walk(directory):
    for file in files:  # get all the files
        filename = os.path.join(path, file)
        # add the size of each file in the root dir to get the total size
        dir_size += os.path.getsize(filename)

fsizeList = [  
    str(round(fsizedicr[key] * dir_size, 2)) + " " + key for key in fsizedicr
]  # list of units

if dir_size == 0:
    print("File Empty")
else:
    for units in sorted(fsizeList)[
        ::-1
    ]:
        print("Folder Size: " + units)