import sys

# some methods and variavle of sys modules
print(f"sys.path : {sys.path}")
print(f"sys.platform : {sys.platform}")
print(f"sys.executable : {sys.executable}")
print(f"sys.modules : {sys.modules}")
print(f"sys.copyright : {sys.copyright}")


# kind of use case of sys module
print(f"\n{sys.argv[0]} executable file were in used for sys module")
print(f"Arguments entered in {sys.argv[0]} are:- ")
for args in sys.argv:
    print(args,end=", ")
    # sys.exit()