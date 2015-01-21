import os
import platform
import shutil
import tempfile
if platform.system() == "Linux":
	cmds = ['sudo apt-get install libusb-1.0-0-dev freeglut3-dev libxmu-dev libxi-dev',
		'sudo adduser $USER video',
		'sudo cp %s /etc/udev/rules.d/51-kinect.rules' % os.path.join(bii.block_folder, 'platform/linux/udev/51-kinect.rules')]
	for cmd in cmds:
		print cmd
		os.system(cmd)
if platform.system() == "Darwin":
	dirpath = tempfile.mkdtemp()
	os.system('cd %s && sudo /bin/bash %s ' % (dirpath, os.path.join(bii.block_folder, 'depsinstaller/kinectdeps.sh')))
