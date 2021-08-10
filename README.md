# rest-fizzbuzz

A modified fizzbuzz rest api server for practice purposes

## Usage

The makefile contains the main commands needed to work with the project

## Running the tests

While docker-compose is running, run the following command: `docker-compose exec backend pytest`

This will execute all the tests and compute the test coverage of the rest_fizzbuzz module.

## Contributing

Follow these steps before pushing new code :
- run the `make qa` command to apply the qa checks

## Todo

- [X] Makefile
- [X] Install DRF
- [X] Install Pytest
- [X] Create requirements files (base, tests)
- [X] Create basic endpoint
- [X] Split code in utils
- [X] Create basic tests
- [X] Create Request Model
- [X] create Dockerfile
- [X] create docker-compose file
- [X] Add postgres
- [X] Create statistics endpoint
- [ ] Add tests
- [ ] Polish project
- [ ] Polish README