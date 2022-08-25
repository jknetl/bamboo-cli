from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'bamboo-cli',
    version = '0.0.1',
    author = 'Jakub Knetl',
    author_email = 'knetl.j@gmail.com',
    license = 'Apache-2.0 license',
    description = 'CLI for operating Atlassian Bamboo',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/jknetl/bamboo-cli',
    py_modules = ['src'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        bcli=src.main:main
    '''
)