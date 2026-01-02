from setuptools import setup

setup(
    name='pykst',
    version='0.3',
    py_modules=['pykst', 'pykstplot'],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'PyQt5',
    ],
    extras_require={
        'dotenv': ['python-dotenv'],
    },
    description='Python interface to KST plotting application',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
