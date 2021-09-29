from setuptools import setup
setup(
    name='dotfig',
    version='0.0.2',
    packages=['dotfig'],
    entry_points={
        'console_scripts': [
            'dotfig=dotfig.dotfig:run'
        ]
    }
)
