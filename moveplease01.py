 #!/usr/bin/env python3
import shutil 
import os     
os.chdir('/home/student/mycode/')
shutil.move('/home/student/mycode/raynor.obj', '/home/student/mycode/ceph_storage/')
xname = input('What is the new name for kerrigan.obj? ')
shutil.move('/home/student/mycode/ceph_storage/kerrigan.obj', '/home/student/mycode/ceph_storage/' + xname)
