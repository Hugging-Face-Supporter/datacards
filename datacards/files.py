#!/usr/bin/env python3

import glob
import os
from typing import Dict, List, Optional

import yaml

from datacards.types import DATASETS_DIR, SortingStrategy


def get_tmp_yaml_filename(path: str) -> str:
    return path.replace(DATASETS_DIR, "/tmp/").replace(".md", ".yaml")


def write_yaml(yaml_str: List[str], path: str = "/tmp/README.yaml") -> None:
    """Write yaml object to file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w+") as f:
        for line in yaml_str:
            f.write(line)


def read_yaml(path: str = "/tmp/README.yaml", sort=False) -> Dict:
    """Read yaml file and content."""
    yaml_obj = {}
    with open(path, "r") as f:
        try:
            yaml_obj = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)

    if sort:
        yaml_obj = dict(sorted(yaml_obj.items()))
    return yaml_obj


def traverse(
    path: str,
    target: Optional[str] = None,
    recursive: bool = False,
    sorting: SortingStrategy = SortingStrategy.name,
) -> List[str]:
    """Traverse and find files in a given path."""
    files = sorted(glob.glob(f"{path}", recursive=recursive), key=sorting)
    if target is not None:
        return [match for match in files if target in match]
    return files


def get_readme_files(path: str) -> List[str]:
    """Traverse a path and find all README files."""
    files = []
    for idx, dataset in enumerate(traverse(f"{path}/*")):
        for paths in traverse(f"{dataset}/*", target="README.md", recursive=True):
            files.append(paths)
    return files
