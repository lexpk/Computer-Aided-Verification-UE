This repository contains the code for the 2024 SS UE Computer Aided Verification at TU Wien.

## 1. Setup

### 1.1. Install NuSMV

As your task will be implemented bounded and unbounded model checking, you will want to familiarize yourself with an existing model checker. We will use NuSMV in exercise 1, a symbolic model checker for finite state systems. You can download it from the [NuSMV website](http://nusmv.fbk.eu/).

### 1.2. Setting up your Environment

You can implement the exercises in any programming language you like. However, we highly recommend using a language which tightly interfaces some SAT solver, such as Python, C, C++ or Java. You will be provided with Python templates and explanations for each exercise, which you can use as a starting point.

#### 1.2.1. (Optional) Install Python

We recommend using either virtualenv or conda to manage your python environment. You can install the required packages by running:

```bash
pip install -r requirements.txt
```
or 
```bash
conda install --file requirements.txt
```