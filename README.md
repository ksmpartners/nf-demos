# Introduction
This project contains sample configuration and input files to run the nf-core pipelines fetchngs, hlatyping, and rnaseq.  Each subdirectory contains a .config file with environment and hardware configurations which are used by Nextfuse to run Nextflow jobs in Domino.

## /fetchngs
This directory contains instructions for environment setup and execution of the nf-core/fetchngs pipeline. Additionally, the directory contains a sample configuration file with required compute environments image and associated input data .csv files.

## /hlatyping
This directory contains instructions for environment setup and execution of the nf-core/hlatyping pipeline. Additionally, the directory contains a sample configuration file with required compute environments images.

## /rnaseq
This directory contains instructions for environment setup and execution of the nf-core/rnaseq pipeline. Additionally, the directory contains a sample configuration file with required compute environments images. Rnaseq also contains a local.config file which configures the pipeline to run with appropriate compute and memory resources.