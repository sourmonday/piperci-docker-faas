#! /usr/bin/env python

from setuptools import find_packages, setup


try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements

from glob import glob


def load_requirements(glob_pattern):
    req_files = glob(glob_pattern)
    reqs = set()

    for f in req_files:
        for ir in parse_requirements(f, session="test"):
            reqs.add(str(ir.req).split('@')[0])

    return list(reqs)


__name__ == "__main__" and setup(
    use_scm_version=True,
    license='MIT License',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=["setuptools-scm"],
    install_requires=load_requirements('piperci-*/requirements.txt'),
    dependency_links=['git+https://github.com/AFCYBER-DREAM/python-piperci.git#egg=piperci'],
    name="piperci-docker",
)
