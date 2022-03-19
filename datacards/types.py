#!/usr/bin/env python3

import os
from enum import Enum
from typing import Callable

DATASETS_DIR = "datasets/datasets/"


class SortingStrategy(Enum):
    name: Callable = os.path.basename
    time: Callable = os.path.getmtime
    size: Callable = os.path.getsize
