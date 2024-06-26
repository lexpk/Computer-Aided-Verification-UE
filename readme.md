This repository contains the code for the 2024 SS UE Computer Aided Verification at TU Wien. You will find 3 exercises in their respective folders. The overarching goal is the implementation of a bounded model checker for Linear Temporal Logic (LTL).

## 1. Setup

### 1.1. Install NuSMV

As you will be implementing a model checker yourself, it will be useful to first familiarize yourself with an existing one. We will use NuSMV, a symbolic model checker for finite state systems. You can download it from the [NuSMV website](http://nusmv.fbk.eu/).

### 1.2. Setting up Python

We will be using [Python](https://www.python.org/downloads/) for the exercises. It is recommended using either virtualenv or conda to manage your python environment. You can install the required packages by running:

```bash
pip install -r requirements.txt
```
