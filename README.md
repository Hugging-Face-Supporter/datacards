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
- [ ] Create method to filter for missing datasets
- [ ] Create [tool to annotate the datasets](https://huggingface.co/spaces/huggingface/datasets-tagging/blob/main/tagging_app.py)
- [ ] Toggle between datasets to annotate.
- [ ] Save modified files to the README again
- [ ] Once done, find ways to create automatic PR to Hugging face datasets
