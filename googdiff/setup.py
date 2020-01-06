from setuptools import setup

setup(
    name='googdiff',
    version='0.1',
    author='wixette',
    author_email='wixette@gmail.com',
    description='An executable wrapper of Google's diff-match-patch module.',
    scripts=['scripts/googdiff.py'],
    python_requires='>=3.6',
)
