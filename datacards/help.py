from datacards.meta import (
    known_creators,
    known_language_codes,
    known_licenses,
    known_multilingualities,
    known_size_categories,
    known_task_ids,
)

langs = known_creators["language"]
annots = known_creators["annotations"]
lang_codes = known_language_codes
licenses = known_licenses

# mono, multi, translation
multiling = known_multilingualities
# n<1K, 10K<n<100K
sizes = known_size_categories
# "text-classification"
tasks = [k for k in known_task_ids.keys()]
subtasks = known_task_ids
for task, d in known_task_ids.items():
    d.pop("description")

if __name__ == "__main__":
    print(subtasks)
    print(known_multilingualities)

    # TODO: send information over to main
    # pp(known_task_ids)
    # pp(known_creators["annotations"])
