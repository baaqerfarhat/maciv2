from setuptools import find_packages, setup
from os.path import join, dirname
from glob import glob

package_name = 'maciv2'

def get_all_files_in_path(glob_string, path_string):
    return [(join(path_string, dirname(g)), [g]) for g in glob(glob_string, recursive=True)]

def create_datafiles():
    df = [
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        (join('share/', package_name, 'launch'), glob('launch/*.py')),
        (join('share/', package_name, 'config'), glob('config/*.*')),
        ('share/' + package_name, ['package.xml']),
    ]
    for complex_path in ['robot_description', 'models', 'maciv2']:
        res = get_all_files_in_path(glob_string=f'{complex_path}/**/*.*', path_string=join('share', package_name))
        df.extend(res)
    return df

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=create_datafiles(),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='53981711+baaqerfarhat@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gripper = maciv2.maciv2:main',
            'node = maciv2.simple:main',
            "moveit = maciv2.moveit:main"
        ],
    },
)
