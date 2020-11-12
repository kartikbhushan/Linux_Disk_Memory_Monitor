#!/use/bin/python3

import sys
import os
import pandas as pd

class Disk_monitor:
    
    def __init__(self,path = "/home"):
         self.path = path

    # Invoked only for directories.
    # Loops through the entire directory and gets total size of the directory
    def get_size(self,path):
        total_size = 0
        for path, dirs, files in os.walk(path):
                for f in files:
                        fp = os.path.join(path, f)
                        total_size += os.path.getsize(fp)
        return total_size/(1024*1024)
    
    # Makes CSV entries and outputs a final CSV file.
    def make_csv(self, entry_path,total_size):
        paths.append(entry_path)
        usage.append(total_size)
        usage_dict = {
            'directory' : paths,
            'usage' : usage,
            'Size format ' : 'MB'
        }
        df = pd.DataFrame(usage_dict)
        df.to_csv("disk_usage.csv")

    def totalsize(self):
        df = pd.read_csv("disk_usage.csv")
        total = df['usage'].sum()
        return total

# Main function.
if __name__ == "__main__":
        path = "/home"
        # accepting command line arguments for specified directory entries
        directory = sys.argv[1] if len(sys.argv) >= 2 else path
        paths = []
        usage = []
    # Class Disk_monitor Object
        obj = Disk_monitor(directory)

        # Main loop
        for entry in os.scandir(directory):
        # if the Entry is a directory send to get_size() function
                if (entry.is_dir(follow_symlinks = False)):
                        total_size = obj.get_size(entry.path)
                        obj.make_csv(entry.path, total_size)
        # if the Entry is a file get file size using os.stat()
                else:
                        total_size = os.stat(entry).st_size
                        total_size = total_size/(1024*1024)
                        obj.make_csv(entry.path, total_size)
        print("Disk_usage.csv has been created")
        print("Total Size of the Directory is : " + str(obj.totalsize()) + " MB")
        