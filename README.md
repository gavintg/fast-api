<img align="right" src="docs/assets/elfo-round.png" width="172px" />

# FAST-API

The following project is a quick start for [fastapi](https://fastapi.tiangolo.com/) with end-to-end tests using [pytest](https://docs.pytest.org/en/7.1.x/getting-started.html) in [python](https://www.python.org/about/gettingstarted/).

## Project Setup 

<sub> :warning: **Safety First** - You should always check the contents of the script before running it [here](bin/setup-project). :warning: </sub>

To setup your project please do the following: 

```bash
bin/setup-project
```

## Saving Dependencies

<sub> :warning: **Safety First** - You should always check the contents of the script before running it [here](bin/save-dependencies). :warning: </sub>

If you have installed a new dependency for example: 

```bash 
pip install requests
```

Then please be sure to save your dependencies by running the following before commiting to git:

```bash
bin/save-dependencies
```

## Running MySQL

<sub> :warning: **Safety First** - You should always check the contents of the script before running it [here](bin/run-mysql). :warning: </sub>

Please run the following to make sure you have a local MySQL database instance: 

```bash
bin/run-mysql
```

## Running the API

<sub> :warning: **Safety First** - You should always check the contents of the script before running it [here](bin/run-api). :warning: </sub>

Please make sure you MySQL first:

```bash
bin/run-mysql
```

Please run the following command to execute the API: 

```bash
bin/run-api
```

## Running the Tests

<sub> :warning: **Safety First** - You should always check the contents of the script before running it [here](bin/run-tests). :warning: </sub>

Please make sure you MySQL and the API first:

```bash
bin/run-mysql
bin/run-api
```

Please run the following command to execute the Tests: 

```bash
bin/run-tests
```
