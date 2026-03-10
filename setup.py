from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'imu_madgwick'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sebi',
    maintainer_email='spereira@ethz.ch',
    description='This launch file launches a microRos agent, which is used to interface a microcontroller with a pi/PC. It launches 3 nodes at once, the microRos agent, the filter node which uses the madgwick filter to estimate the orientation of an IMU and an Rviz application to vizualize the results',
    license='Apache License 2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
