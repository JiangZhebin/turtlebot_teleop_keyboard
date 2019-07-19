

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    scripts=['bin/joint_controller', 'bin/joint_client' , 'bin/Teleop_key'],
    packages=['teleop_base_arm'],
    package_dir={'': 'src'},
    requires=['rospy']
    )

setup(**d)
