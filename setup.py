# Copyright (c) 2020, RTE (http://www.rte-france.com)
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup

setup(
    name='pypowsybl',
    version='1.0.0',
    description='PowSyBl for Python',
    license='Mozilla Public License 2.0 (MPL 2.0)',
    url='https://www.powsybl.org',
    python_requires='>3.0.0',
    install_requires=[
        'JPype1'
    ],
    include_package_data=True,
    packages=[
        'pypowsybl',
        'pypowsybl.lib'
    ],
    package_dir={
        'pypowsybl': '../pypowsybl',
        'pypowsybl.lib': 'lib'
    },
    package_data={
        'pypowsybl.lib': ['*.jar']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
)
