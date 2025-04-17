import platform

# some methods of platform module
print(f"platform.processor() : {platform.processor()}")
print(f"platform.architecture() : {platform.architecture()}")
print(f"platform.machine() : {platform.machine()}")
print(f"platform.node() : {platform.node()}")
print(f"platform.platform() : {platform.platform()}")
print(f"platform.system() : {platform.system()}")
print(f"platform.uname() : {platform.uname()}")


# kind of use case
import os
if platform.system() == "Windows":
    os.system("dir")
elif platform.system() == "Linux":
    os.system("ls")
else:
    print("Unidentified OS")
