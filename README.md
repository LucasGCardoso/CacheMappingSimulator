# CacheMappingSimulator
This repo is a work from college, which consists in simulating both associative and direct cache mapping.

## Proposed Problem
The objective of this work is to implement an algorithm for simulating both associative and direct cache mapping, for learning proposes. In this scenario I used 16 bit words, but this can be changed in the variables.

## Configuration
### Dependencies
In order to properly run this code, you will need to have installed [Python3](https://www.python.org/downloads/) in your computer.

### Configurating the cache
The variables you should change in order to change the cache and the addresses configurations are:
- num_linhas: Number of lines the cache should have
- num_palavras: Number of words the cache should have in each line
- tag: The number of bits the tag has in each address
- linha: The number of bits the line has in each address - only change the raw number, it must always sum with the tag
- palavra: The number of bits the words have in each address - only change the raw number, it must always sum with the tag
