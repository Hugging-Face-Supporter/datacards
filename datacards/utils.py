#!/usr/bin/env python3

import os

from datacards.types import DATASETS_DIR


def basename(path: str):
    return os.path.basename(path)


def dataset_name(path: str) -> str:
    dataset, file = path.replace(DATASETS_DIR, "").split("/")
    return dataset
