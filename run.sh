#!/bin/bash

#gcc -static src/hello.c -o bin/hello
clang -coverage -O0  src/hello.c -o bin/hello
./bin/hello
