import os
import platform
import shutil
import tempfile

current_path = os.getcwd()
if platform.system() == "Linux":
    cmds = "sudo apt-get install freeglut3-dev libxmu-dev libxi-dev wget libudev-dev"
    print cmds
    os.system(cmds)
    try:
        cmds = "sudo adduser $USER video"
        print cmds
        os.system(cmds)
    except:
        pass
    if not (os.path.exists("/usr/local/include/libusb-1.0/libusb.h")):
        filepath = os.path.join(bii.environment_folder, "libusb-1.0.19.tar.bz2")
        if  os.path.exists(filepath):
            os.system("rm %s" % filepath)
        filepath = os.path.join(bii.environment_folder, "libusb-1.0.19")
        if  os.path.exists(filepath):
            os.system("rm %s" % filepath)

        cmds = "cd %s ; " % bii.environment_folder +\
               "wget http://sourceforge.net/projects/libusb/files/libusb-1.0/libusb-1.0.19/libusb-1.0.19.tar.bz2 ; " +\
               "tar -xjvf libusb-1.0.19.tar.bz2 ; " +\
               "cd libusb-1.0.19 ; " +\
               "./configure && sudo make install ; " +\
               "cd %s" % current_path
        print cmds
        os.system(cmds)


    if not (os.path.exists("/etc/udev/rules.d/51-kinect.rules")):
        cmds = 'sudo cp %s /etc/udev/rules.d/51-kinect.rules' % os.path.join(bii.block_folder, 'platform/linux/udev/51-kinect.rules')
        print cmds
        os.system(cmds)

if platform.system() == "Darwin":

    if not (os.path.exists("/usr/local/include/bin/autoconf")):
        filepath = os.path.join(bii.environment_folder, "autoconf-2.69.tar.gz")
        if not os.path.exists(filepath):
            cmds = "cd %s ; " % bii.environment_folder +\
                   "curl -OL http://ftpmirror.gnu.org/autoconf/autoconf-2.69.tar.gz ; " +\
                   "tar -xzf autoconf-2.69.tar.gz ; " +\
                   "cd autoconf-2.69 ; " +\
                   "./configure && sudo make install ; " +\
                   "cd %s" % current_path
            print cmds
            os.system(cmds)

    if not (os.path.exists("/usr/local/include/bin/automake")):
        filepath = os.path.join(bii.environment_folder, "automake-1.14.tar.gz")
        if not os.path.exists(filepath):
            cmds = "cd %s ; " % bii.environment_folder +\
                   "curl -OL http://ftpmirror.gnu.org/automake/automake-1.14.tar.gz ; " +\
                   "tar -xzf automake-1.14.tar.gz ; " +\
                   "cd automake-1.14 ; " +\
                   "./configure && sudo make install ; " +\
                   "cd %s" % current_path
            print cmds
            os.system(cmds)

    if not (os.path.exists("/usr/local/include/bin/libtool")):
        filepath = os.path.join(bii.environment_folder, "libtool-2.4.2.tar.gz")
        if not os.path.exists(filepath):
            cmds = "cd %s ; " % bii.environment_folder +\
                   "curl -OL http://ftpmirror.gnu.org/libtool/libtool-2.4.2.tar.gz ; " +\
                   "tar -xzf libtool-2.4.2.tar.gz ; " +\
                   "cd libtool-2.4.2 ; " +\
                   "./configure && sudo make install ; " +\
                   "cd %s" % current_path
            print cmds
            os.system(cmds)

    if not (os.path.exists("/usr/local/include/libusb-1.0/libusb.h")):
        filepath = os.path.join(bii.environment_folder, "libusb-1.0.19.tar.bz2")
        if not os.path.exists(filepath):
            cmds = "cd %s ; " % bii.environment_folder +\
                   "curl -OL https://downloads.sourceforge.net/project/libusb/libusb-1.0/libusb-1.0.19/libusb-1.0.19.tar.bz2 ; " +\
                   "tar -xjvf libusb-1.0.19.tar.bz2 ; " +\
                   "cd libusb-1.0.19 ; " +\
                   "./configure && sudo make install ; " +\
                   "cd %s" % current_path
            print cmds
            os.system(cmds)