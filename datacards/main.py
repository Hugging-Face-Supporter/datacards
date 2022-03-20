#!/usr/bin/env python3
import os
import pprint
from argparse import ArgumentParser

from datacards.files import get_readme_files
from datacards.meta import (
    CustomDatasetMetadata,
    DatasetMetadata,
    MetaDataValidationError,
    YamlDuplicateKeysError,
    YamlMultipleConfigsError,
    YamlParsingError,
    known_creators,
    parse_missing_attributes,
)
from datacards.types import HF_DATASETS_DIR, METADATA_ATTR


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "--include_all",
        action="store_true",
        default=False,
        help="Make the search include datasets that have their tags",
    )
    parser.add_argument(
        "--search",
        choices=[k for k in METADATA_ATTR],
        nargs="+",
        help="Select what tags to search for",
    )
    # TODO:
    parser.add_argument(
        "--tags",
        choices=[],
        nargs="+",
        help="Print allowed tags datasets expects",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    dataset_paths = get_readme_files(path=HF_DATASETS_DIR)

    num_correct = 0
    num_incorrect = 0
    non_data_folders = []
    all_datasets = []
    correct_datasets = []
    incorrect_dataset = {}
    incorrect_dataset_dict = {k: [] for k in METADATA_ATTR}

    # Find missing attributes in the data
    for path in dataset_paths:
        try:
            metadata = CustomDatasetMetadata.from_readme(path=path)
            metadata.path = path
            all_datasets.append(metadata.__dict__)

            # Try to get the dataset readme tags
            try:
                _ = DatasetMetadata.from_readme(path=path)
                num_correct += 1

            # Get datasets missing core tags
            except TypeError as e:
                missing_attr = parse_missing_attributes(e)
                num_incorrect += 1
                for k in missing_attr:
                    if k in METADATA_ATTR:
                        incorrect_dataset_dict[k].append(path)
                    else:
                        print(k)

        # The path pointed to was not a dataset path
        except (
            MetaDataValidationError,
            YamlDuplicateKeysError,
            YamlMultipleConfigsError,
            YamlParsingError,
        ):
            non_data_folders.append(path)

    # Display metadata needed to annotate the missing tags in the datasets
    # TODO: Add search and filtering from argparse
    pp = pprint.PrettyPrinter(indent=2, compact=False).pprint
    pp(incorrect_dataset_dict["task_categories"])

    print("------------------------------------")
    print("\nNumber of incorrect README:\t", num_incorrect)
    print("Number of datasets total:\t", num_correct)
    print("\n------------------------------------")
