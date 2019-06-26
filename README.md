# PiedPiper Docker Function

[![Build Status](https://travis-ci.com/sourmonday/piperci-docker-faas.svg?branch=master)](https://travis-ci.com/sourmonday/piperci-docker-faas)
[![codecov.io](https://codecov.io/github/sourmonday/piperci-docker-faas/coverage.svg?branch=master)](https://codecov.io/github/sourmonday/piperci-docker-faas?branch=master)

### Table of Contents

* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Installing](#installing)
* [Inputs and Outputs](#inputs-and-outputs)
* [Running the Tests](#running-the-tests)
* [Contributing](#contributing)
* [Versioning](#versioning)
* [Authors](#authors)
* [License](#license)
* [Acknowledgements](#acknowledgments)

## Getting Started

To deploy this function you must have OpenFaaS installed. To create a development environment see 
https://github.com/AFCYBER-DREAM/ansible-collection-pidev.

### Prerequisites

OpenFaaS

### Installing

To install this function on OpenFaaS do the following after authentication:

```bash
git clone https://github.com/sourmonday/piperci-docker-faas.git
cd piperci-docker-faas
faas build
faas deploy
```

To validate that your function installed correctly you can run the following:

```bash
faas ls
```

## Inputs and Outputs


## Running the tests

```bash
tox -e lint
```

### Test Prerequisites

Tox must be installed and an OpenFaaS environment must be available locally.
You must also deploy the image to OpenFaaS.

There is an simple bash script which can be used to turn a local machine into
an OpenFaaS development environment. This can be found in `tools/scripts/setup-env.sh`.
This is the script that is being used by Travis-CI to deploy the test environment.

We also have an Ansible role available to setup the OpenFaaS environment. This
can be found [here](https://github.com/AFCYBER-DREAM/ansible-collection-pidev)

## Contributing

Please read [CONTRIBUTING.md](https://github.com/AFCYBER-DREAM/piedpiper-picli) for details on our code of conduct, and 
the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the 
[tags on this repository](https://github.com/piperci-docker-faas/tags).

## Authors

See also the list of [contributors](https://github.com/sourmonday/piperci-docker-faas/contributors) who participated 
in this project.

## License

MIT
