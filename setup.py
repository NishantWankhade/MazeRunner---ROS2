from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'minor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # Adding files to Launch World
        ('share/' + package_name + '/world/xacro', glob('world/xacro/*.xacro')),
        ('share/' + package_name + '/world', glob('world/*.sdf')),
        ('share/' + package_name + '/world/stl', glob('world/stl/*.stl')),

        # Adding Launch file as an executable 
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ngw',
    maintainer_email='nishant.wankhade07@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
