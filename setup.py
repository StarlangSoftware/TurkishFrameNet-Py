from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='NlpToolkit-FrameNet',
    version='1.0.6',
    packages=['FrameNet', 'FrameNet.data'],
    package_data={'FrameNet.data': ['*.xml']},
    url='https://github.com/StarlangSoftware/TurkishFrameNet-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='FrameNet library',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
