import pypandoc
import os
import fs

# Read the markdown README
doc = pypandoc.convert('README.md', 'rst')

# Write a rST README for long_description
fs.write('README.txt', doc)

# Run the register command
os.system("python setup.py register sdist upload")

# Remove the rST README
fs.rm('README.txt')