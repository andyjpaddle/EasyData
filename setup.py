# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from io import open
from setuptools import setup


def get_requirements():
    with open('requirements.txt', encoding="utf-8-sig") as f:
        requirements = f.readlines()
    return requirements


setup(
    name='easydata-python',
    packages=['easydata', 'easydata.deploy'],
    package_dir={
        'easydata': 'python_whl',
        'easydata.deploy': 'deploy'
    },
    include_package_data=True,
    entry_points={"console_scripts": ["easydata=easydata.easydata:main"]},
    version='0.0.0',
    install_requires=get_requirements(),
    license='Apache License 2.0',
    description=
    'A toolkit for processing data powered by PaddlePaddle, which include data augmentation, data cleaning and data annotation.',
    long_description=
    'EasyData aims to create a universal, leading and practical data processing toolkit, that supports automatic data augmentation and cleaning, and provides data annotation tools and a collection of open source datasets to help developers obtain high-quality training and inference data more easily, thereby promoting the practical effect of AI algorithms.',
    long_description_content_type='text/markdown',
    url='https://github.com/PaddlePaddle/EasyData',
    download_url='https://github.com/PaddlePaddle/EasyData.git',
    keywords=[
        'PaddlePaddle',
        'PP-DataAug',
        'PP-DataClean',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9', 'Topic :: Utilities'
    ],
)
