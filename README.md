# Overview
This repository contains assets for showcasing and evaluating KSM's Nextflow integration with Domino. It is meant to be added to a Git-based Domino project so that its assets can be used from there.

# Prerequisites
Prior to executing any of the showcases listed below, you will need a Domino Compute environment that has has Nextflow installed, along with KSM's Nextflow Domino plugin. See [these instructions](./prereq/README.md) to such an environment.

# Showcases
After completing the above prerequisites, click any of the following links to run Nextflow pipelines in Domino

1. [rnaseq-nf pipeline from nextflow.io](./showcases/rnaseq-nf/README.md). This is a relatively simple pipeline bundled with Nextflow (not part of nf-core) that uses common RNA seqencing tools to map a collection of read-pairs to a given reference genome and output the respective transcript model. It only has one required compute environment, and uses on-board data, making it ideal for a simple showcase.
1. nf-rnaseq quick test pipeline (TBD)
1. nf-rnaseq full test pipeline (TBD)