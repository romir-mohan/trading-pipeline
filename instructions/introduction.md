# Introduction

Herein, you will be building your very first trading pipeline, sans execution. 
You will build a trading pipeline on Coinbase's BTC - we will use the REST API to simplify construction. The following components will be made:

- Data Ingest - Python, Then Cpp
- Feature Computation - Cpp
- Inference - Python
- Analysis - Python

At the end, you will have a working system that can bring in market data and make predictions, as well as be able to verify how performant 
(or unperformant) those predictions are. 

For everything to work, you must verify the following packages are installed on a UNIX or UNIX-like environment (NUFT Servers Recommended):

- GNU Make - Runs our tasks for us
- CMake - C++ Build system
- Ninja - C++ Build Generator
- Conan - C++ Dependency Management
- Poetry - Python Build System
- Mypy - Python Type Checker
- Ruff - Python Linter
- Python3.12 WITH DEVELOPMENT HEADERS
