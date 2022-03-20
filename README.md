# Datacard

This repo aims to find and update the missing model cards for Hugging face datasets.

If you find this a worth while pursute, feel free to reach out and let's try to make the Hugging face datasets complete :wink:

## Setup

```shell
# install poetry
git clone --recurse-submodules --remote-submodules git@github.com:Hugging-Face-Supporter/datacards.git
cd datacards
git submodule update

poetry install
```

## Run

```shell
poetry shell
python datacards/main.py
```

## WIP

- [x] Look into how to provide multiple answers in model card (ex. Glue dataset)
- [x] Find the datasets that are missing information by parsing the README
- [x] Find ways to know what categories are valid answers
- [x] Create method to filter for missing datasets
- [ ] Incorporate the argparse to filter for certiain things
- [ ] Toggle between datasets to annotate.
- [x] Save modified files to the README again
- [ ] Once done, find ways to create automatic PR to Hugging face datasets
- [ ] Incorporate the [Huggingface Hub API](https://github.com/huggingface/huggingface_hub/blob/b5ed1420c3f3db7b8f0652efa2a3497698150b0a/src/huggingface_hub/hf_api.py#L582)
