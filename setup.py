from distutils.core import setup

# Read the long description
with open('README.md') as file:
    long_description = file.read()

setup(
    name='fs',
    version='0.0.1',
    description='a pythonic file system wrapper for humans',
    long_description=long_description,
    author='Christoph Koerner',
    author_email='office@chaosmail.at',
    url='https://github.com/chaosmail/python-fs',
    download_url='https://github.com/chaosmail/python-fs/releases',
    py_modules=['fs'],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Operating System',
        'Topic :: Utilities',
    ],
)