# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "dlt[sqlalchemy]",
#     "trino[sqlalchemy]",
# ]
#
# [[tool.uv.index]]
# url = "https://codeartifact.aws.redwoodmaterials.com/pypi/d/redwood-250982523368/redwood-pypi/simple/"
# ///

from typing import Any, Dict, Iterator

import dlt


@dlt.resource(name="sample_data")
def generate_sample_data() -> Iterator[Dict[str, Any]]:
    """
    A simple data source that generates sample records.
    """
    # Generate some sample data
    sample_records = [
        {"id": 1, "name": "Alice", "department": "Engineering"},
        {"id": 2, "name": "Bob", "department": "Marketing"},
        {"id": 3, "name": "Carol", "department": "Sales"},
    ]

    for record in sample_records:
        yield record


def run_pipeline():
    """
    Main function to run the dlt pipeline with sqlalchemy destination.
    """
    pipeline = dlt.pipeline(
        pipeline_name="sample_sqlalchemy_pipeline",
        destination="sqlalchemy",
        dataset_name="sample_dataset",
        progress=dlt.progress.log(
            log_period=10,
        ),
    )

    load_info = pipeline.run(generate_sample_data())

    for job in load_info.jobs:
        print(
            f"  - {job.job_file_info.table_name}: {job.job_file_info.file_size} bytes"
        )

    return load_info


if __name__ == "__main__":
    run_pipeline()
