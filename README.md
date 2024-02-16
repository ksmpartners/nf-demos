
# Nextfuse Demos

This project contains sample configuration and input files to run the `nf-core` pipelines `fetchngs`, `hlatyping`, and `rnaseq`.  Each subdirectory contains a .config file with environment and hardware configurations which are used by Nextfuse to run [Nextflow®](https://www.nextflow.io/) jobs in [Domino](https://domino.ai/). Depending on the Nextfuse version used by your organization, make sure to use the code from the corresponding Git tag.

## /fetchngs
Instructions for environment setup and execution of the `nf-core/fetchngs pipeline`. Additionally, the directory contains a sample configuration file with required compute environments image and associated input data `.csv` files.

## /hlatyping
Instructions for environment setup and execution of the `nf-core/hlatyping pipeline`. Additionally, the directory contains a sample configuration file with required compute environments images.

## /rnaseq
Instructions for environment setup and execution of the `nf-core/rnaseq pipeline`. Additionally, the directory contains a sample configuration file with required compute environments images. Rnaseq also contains a `local.config` file which configures the pipeline to run with appropriate compute and memory resources.
