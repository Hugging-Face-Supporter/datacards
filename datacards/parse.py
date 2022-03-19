#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import Dict, List

from datacards.files import get_tmp_yaml_filename, read_yaml, write_yaml


def parse_readme_table(path: str) -> List[str]:
    """The tables start and end with '---' and are based on yaml."""
    with open(path, "r+") as f:
        d = f.readlines()[1:]

    table = []
    for line in d:
        if line == "---\n" or line == "### Contributions\n":
            break
        table.append(line)
    return table


def parse_yaml(yaml_str: List[str], path: str, sort=True) -> Dict:
    """Convert every README table from strings to yaml."""
    tmp_path = get_tmp_yaml_filename(path)
    write_yaml(yaml_str, path=tmp_path)
    return read_yaml(path=tmp_path, sort=sort)


@dataclass
class DatasetREADME:
    """
    ---
    annotations_creators:
    - no-annotation
    language_creators:
    - found
    languages:
    - en
    licenses:
    - unknown
    multilinguality:
    - monolingual
    size_categories:
    - 100K<n<1M
    source_datasets:
    - original
    task_categories:
    - question-answering
    task_ids:
    - abstractive-qa
    - open-domain-qa
    paperswithcode_id: eli5
    pretty_name: ELI5
    ---


    ---
    annotations_creators:
    - found
    language_creators:
    - found
    languages:
      all_languages:
      - de
      - en
      - es
      - fr
      - ja
      - zh
      de:
      - de
      en:
      - en
      es:
      - es
      fr:
      - fr
      ja:
      - ja
      zh:
      - zh
    licenses:
    - other-amazon-license
    multilinguality:
      all_languages:
      - multilingual
      de:
      - monolingual
      en:
      - monolingual
      es:
      - monolingual
      fr:
      - monolingual
      ja:
      - monolingual
      zh:
      - monolingual
    size_categories:
      all_languages:
      - 1M<n<10M
      de:
      - 100K<n<1M
      en:
      - 100K<n<1M
      es:
      - 100K<n<1M
      fr:
      - 100K<n<1M
      ja:
      - 100K<n<1M
      zh:
      - 100K<n<1M
    source_datasets:
    - original
    task_categories:
    - conditional-text-generation
    - sequence-modeling
    - text-classification
    - text-scoring
    task_ids:
    - language-modeling
    - sentiment-classification
    - sentiment-scoring
    - summarization
    - topic-classification
    paperswithcode_id: null
    pretty_name: The Multilingual Amazon Reviews Corpus
    ---

    ---
    annotations_creators:
    - crowdsourced
    language_creators:
    - crowdsourced
    languages:
    - en
    licenses:
    - cc-by-4.0
    multilinguality:
    - monolingual
    size_categories:
    - 100K<n<1M
    source_datasets:
    - extended|other-flicker-30k
    - extended|other-visual-genome
    task_categories:
    - text-classification
    task_ids:
    - natural-language-inference
    paperswithcode_id: snli
    pretty_name: Stanford Natural Language Inference
    ---
    # Dataset Card for SNLI
    """

    annotations_creators: str = field(default=None)
    language_creators: str = field(default=None)
    languages: str = field(default=None)
    licenses: str = field(default=None)
    multilinguality: str = field(default=None)
    size_categories: str = field(default=None)
    source_datasets: str = field(default=None)
    task_categories: str = field(default=None)
    task_ids: str = field(default=None)
    paperswithcode_id: str = field(default=None)  # Should exist
    pretty_name: str = field(default=None)  # Should exist
