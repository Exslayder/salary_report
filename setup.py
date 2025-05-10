from setuptools import setup, find_packages

setup(
    name='payroll_report',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'payroll-report=main:main',
        ],
    },
    install_requires=[],
    author='Your Name',
    description='A simple payroll reporting tool',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
