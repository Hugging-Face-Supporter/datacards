#!/usr/bin/env python3

from datacards.files import get_readme_files
from datacards.parse import parse_readme_table, parse_yaml
from datacards.types import DATASETS_DIR
from datacards.utils import dataset_name

# TODO: Make smarter search
# Here we might want to search for those missing:
#   contributer, license, language, task_categories

"""
The most complete readme for a dataset!
---
annotations_creators:
- crowdsourced
extended:
- original
language_creators:
- crowdsourced
- found
languages:
- fr
licenses:
- cc-by-nc-sa-3.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- question-answering
- text-retrieval
task_ids:
- extractive-qa
- closed-domain-qa
paperswithcode_id: fquad
pretty_name: "FQuAD: French Question Answering Dataset"
---
"""

# NOTE: Many datasets have a `paperswithcode_id = None`
# NOTE: All of these datasets that lack info, contain 5 columns or less
# NOTE: These are 117 datasets out of 741 in total

if __name__ == "__main__":
    dataset_paths = get_readme_files(path=DATASETS_DIR)
    filter_key = 6  # TODO: Improve the filtering

    num_readmes_incorrect = 0
    non_data_folders = []
    correct_datasets = []
    datasets_to_fix = []
    for path in dataset_paths:
        # Find the info table in the begining of the READMEs
        table = parse_readme_table(path)
        dataset = dataset_name(path)

        # Some folders are there with readmes, but are not actual datasets
        if len(table) == 0:
            non_data_folders.append(dataset)
            continue

        yaml_obj = parse_yaml(yaml_str=table, path=path, sort=True)

        # Yaml object / python dict
        if len(yaml_obj.keys()) < filter_key:
            print(dataset)
            print(yaml_obj)
            print()
            datasets_to_fix.append(dataset)
            num_readmes_incorrect += 1
        else:
            correct_datasets.append(dataset)

    print("------------------------------------")
    print("\nNumber of incorrect README:\t", num_readmes_incorrect)
    print("Number of datasets total:\t", len(dataset_paths) - len(non_data_folders))
    # print(correct_datasets)
    print("\n------------------------------------")
