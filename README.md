# django-coins-transfer

[![Build Status](https://travis-ci.org/suranig/django-coins-transfer.svg?branch=master)](https://travis-ci.org/suranig/django-coins-transfer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## Description
Coins transfer API via Django.

## Build and run via docker
```console

foo@bar:~$ docker-compose build && docker-compose up

```

## Code testing via docker

```console

foo@bar:~$ docker-compose run app pytest

```
## Rest Api

### GET / -- Swagger docs rest api
### GET /api/v1/users/ -- Users list for auth users
### GET /api/v1/users/ID -- Details for ID user
### GET /api/v1/transfers/ -- History of coins transfers for current user
### POST /api/v1/transfers/{"amount": 5, "receiver": 4} -- Send coins by current user to receiver

## Used technologies:
* Django;
* Docker;
* Postegresql.

## TODO:
* more tests for transfer module;
* fix swagger problem (swagger can't see params for TransferPostSerializer).

