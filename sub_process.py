import subprocess
import os
# os.chdir("..\\")
# os.chdir("java")

# Without using shell = False
# javacompile = ["javac", "Palindrome.java"]
pythonrun = ["python", "auto-password.py"]
data = subprocess.run(pythonrun)
print(data)   
# subprocess.run(javacompile)
# subprocess.run(javadebug)

# With using shell = True
# compilejava = "javac Palindrome.java && java Palindrome"
# # debugjava = "java Palindrome"
# subprocess.call(compilejava,shell=True)




# Running a shell command with shell=True
# command = ['dir']
# result = subprocess.run(["dir"])  # Works on Windows

# print(result.stdout)
# ans = subprocess.call(["python", "--version"])
# if ans == 0:
#     print("Command executed")
# else:
#     print("Command failed")


