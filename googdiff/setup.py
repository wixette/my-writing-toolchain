import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='googdiff',
    version='0.2.1',
    author='wixette',
    author_email='wixette@gmail.com',
    description='A wrapper of Google\'s diff-match-patch module.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['diff-match-patch'],
    license='apache-2.0',
    packages=setuptools.find_packages(),
    url='https://github.com/wixette/my-writing-toolchain/tree/master/googdiff',
    scripts=['googdiff'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ]
)
