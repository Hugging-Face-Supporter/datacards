#!/usr/bin/env python3

import os
from enum import Enum
from typing import Callable

from datacards.meta import DatasetMetadata

HF_DATASETS_DIR = "datasets/datasets/"
METADATA_ATTR = [key for key in DatasetMetadata.__dataclass_fields__.keys()]
METADATA_ATTR.append("extended")


class SortingStrategy(Enum):
    name: Callable = os.path.basename
    time: Callable = os.path.getmtime
    size: Callable = os.path.getsize
