from setuptools import setup
setup(
    name='dotfig',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'dotfig=dotfig:run'
        ]
    }
)
