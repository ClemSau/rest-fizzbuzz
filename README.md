# rest-fizzbuzz

A modified fizzbuzz rest api server for practice purposes.

## Endpoints

The application exposes two endpoints:
- `my-fizz-buzz/`: a custom implementation, which takes 5 mandatory query paramaters:
    - `int1: int`: the first number for which the multiples will be replaced by `string1`
    - `int2: int`: the second number for which the multiples will be replaced by `string2`
    - `limit: int`: the limit number for which we want to compute our custom fizzbuzz
    - `string1: str`: the first string by which will be replaced all the multiples of `int1`
    - `string2: str`: the second string by which will be replaced all the multiples of `int2` 
- `statistics/`: an endpoint which returns the most popular request, its count and its parameters.

## Usage

The MakeFile contains the main commands needed to work with the project.

You can list all the available MakeFile commands with `make help`

To start the application, you can simply use the command :
- `make run-compose` 

Or if you cannot use the MakeFile :
- `docker-compose up`

The application will then be available at [localhost:8000](localhost:8000) (this endpoint is not configured, so this will throw you an error) 

## Running the tests

While docker-compose is running both the database and the application, run the following command: 
- `make test`

Or if you cannot use the MakeFile : 
- `docker-compose exec backend pytest`

This will execute all the tests and compute the test coverage of the rest_fizzbuzz module.

## Contributing

Before pushing new code, make sure you follow the following:
- Manually test the new feature
- Run the qa tests
    - On linux, run `make qa`
    - On windows, you will have to run manually the commands in the qa command of the makefile (isort, black, flake8, mypy)
- Run the existing tests
- Add tests for the new functionality, and keep the code coverage above 90%. Make sure they work as expected

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