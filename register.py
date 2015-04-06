import pandoc
import os
import fs

pandoc.core.PANDOC_PATH = '/usr/bin/pandoc'

# Create New Pandoc Document
doc = pandoc.Document()

# Read the markdown README
doc.markdown = fs.read('README.md')

# Write a rST README for long_description
fs.write('README.txt', doc.rst)

# Run the register command
os.system("python setup.py register")

# Remove the rST README
fs.rm('README.txt')