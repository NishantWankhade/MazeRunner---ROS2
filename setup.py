from setuptools import find_packages, setup
from glob import glob

package_name = 'minor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/world/xacro', glob('world/xacro/*.xacro')),
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
