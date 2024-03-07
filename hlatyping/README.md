# Introduction
This directory contains assets required to run the [nf-core/hlatyping](https://github.com/nf-core/hlatyping) pipeline (release tag 2.0.0) in [Domino®](https://domino.ai/). For more information about this pipeline, see its [Github repository](https://github.com/nf-core/hlatyping).

This pipeline requires [Nextflow®](https://www.nextflow.io/) 0.7.1 or higher.

# Compute Environment Prerequisites
Prior to running the pipeline, all of the environments named in [hlatyping.config](./hlatyping.config) must be installed in the local [Domino®](https://domino.ai/) instance.
Additionally, a [NextFlow with Nextfuse](https://ksmpartners.atlassian.net/wiki/spaces/Nextfuse/pages/2870804483/Installing+Nextfuse#Installing-into-an-Existing-Compute-Environment) compute environment should be available to the user as a Workspace base environment. 

# Running the Pipeline in a VS Code Workspace
Start a Workspace in Domino using the [NextFlow with Nextfuse](https://ksmpartners.atlassian.net/wiki/spaces/Nextfuse/pages/2870804483/Installing+Nextfuse#Installing-into-an-Existing-Compute-Environment) compute environment and open a terminal within.

Prior to running the pipeline, set the following shell variables. This is not strictly necessary, but it does make it easier to read the `nextflow` command provided below.
```bash
# outputdir is the directory parent of the [Nextflow®](https://www.nextflow.io/) work directory. It must be in shared storage, such as a [Domino®](https://domino.ai/) dataset directory or an external data volume.
outputdir=/mnt/data/hlatyping

# hlatypingdir is the directory that contains the hlatyping pipeline. If this is not available locally, it can be loaded directly from the web by specifying hlatypingdir=nf-core/hlatyping
hlatypingdir=/mnt/code

# configdir is the location of the directory that contains this README
configdir=/mnt/imported/code/nf-configs/hlatyping
```
After setting the above shell variables, run [Nextflow®](https://www.nextflow.io/):
```bash
nextflow -trace nextfuse run $hlatypingdir \
  -c $configdir/hlatyping.config \
  -w $outputdir/work \
  -profile test
  --outdir $outputdir/outdir
```
The above runs the hlatyping workflow with the test profile using a minimal dataset. To run with a full profile use -profile test_full
