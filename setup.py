import re
from pathlib import Path

from setuptools import find_packages
from setuptools import setup


here = Path(__file__).parent.resolve()

def find_version(file_path):
    """Search for a ``__version__`` string inside the provided file."""

    with open(file_path, mode='r') as f:
        contents = f.read()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", contents, re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError('Unable to find version string.')

version = find_version(Path(here / 'src' / 'ximea' / '__init__.py'))

setup(
    name='ximea',
    version=version,
    description='XIMEA camera api',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    zip_safe=False,
    python_requires='>=3.9',
    include_package_data=True,
    options={'bdist_wheel': {'universal': '1'}},
)
