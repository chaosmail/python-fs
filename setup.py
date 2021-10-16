from distutils.core import setup
import fs

try:
    long_description = fs.read('README.txt')
except IOError:
    long_description = fs.read('README.md')

setup(
    name='pyfs',
    packages=['fs'],
    version='0.0.8',
    description='a pythonic file system wrapper for humans',
    long_description=long_description,
    author='Christoph Koerner',
    author_email='office@chaosmail.at',
    url='https://github.com/chaosmail/python-fs',
    download_url='https://github.com/chaosmail/python-fs/releases',
    license='MIT',
    keywords= ['fs', 'file system', 'filesystem', 'wrapper'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Operating System',
        'Topic :: Utilities',
    ],
)
