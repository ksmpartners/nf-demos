# Introduction
This directory contains assets required to run the [nf-core/fetchngs](https://github.com/nf-core/fetchngs) pipeline (release tag 1.11.0) in [Domino®](https://domino.ai/). For more information about this pipeline, see its [Github repository](https://github.com/nf-core/fetchngs).

This pipeline requires [Nextflow®](https://www.nextflow.io/) 0.7.1 or higher.

# Compute Environment Prerequisites
Prior to running the pipeline, all of the environments named in [fetchngs.config](./fetchngs.config) must be installed in the local [Domino®](https://domino.ai/) instance.
Additionally, a [NextFlow with Nextfuse](https://ksmpartners.atlassian.net/wiki/spaces/Nextfuse/pages/2870804483/Installing+Nextfuse#Installing-into-an-Existing-Compute-Environment) compute environment should be available to the user as a Workspace base environment. 

# Running the Pipeline in a VS Code Workspace
Start a VS Code Workspace in Domino using the [NextFlow with Nextfuse](https://ksmpartners.atlassian.net/wiki/spaces/Nextfuse/pages/2870804483/Installing+Nextfuse#Installing-into-an-Existing-Compute-Environment) compute environment and open a terminal  

## Configure Plugin Version 

Right-click the Code section of the VS Code window and add the /mnt directory to the workspace

Open /mnt/imported/code/nf-demos/fetchngs/fetchngs.config

Add the nextfuse version installed in your organization's [NextFlow with Nextfuse](https://ksmpartners.atlassian.net/wiki/spaces/Nextfuse/pages/2870804483/Installing+Nextfuse#Installing-into-an-Existing-Compute-Environment) compute environment like below:
```
plugins {
  id 'nextfuse@0.12.0'
}
```

Prior to running the pipeline, set the following shell variables. This is not strictly necessary, but it does make it easier to read the `nextflow` command provided below.
```bash
# outputdir is the directory parent of the [Nextflow®](https://www.nextflow.io/) work directory. It must be in shared storage, such as a [Domino®](https://domino.ai/) dataset directory or an external data volume.
outputdir=/mnt/data/fetchngs

# fetchngsdir is the directory that contains the fetchngs [Nextflow®](https://www.nextflow.io/) pipeline. If this is not available locally, it can be loaded directly from the web by specifying fetchngsdir=nf-core/fetchngs
fetchngsdir=/mnt/code

# configdir is the location of the directory that contains this README
configdir=/mnt/imported/code/nf-configs/fetchngs
```
After setting the above shell variables, run [Nextflow®](https://www.nextflow.io/):
```bash
nextflow -trace nextfuse run $fetchngsdir \
  -c $configdir/fetchngs.config \
  -w $outputdir/work \
  --input $configdir/sra_ids_short.csv \
  --outdir $outputdir/outdir
```
The above runs the Fetchngs workflow with a single SRA ID. To run with multiple (10, in fact), try replacing `--input $configdir/sra_ids_short.csv` in the above command with `--input $configdir/sra_ids_test.csv`. This included file is identical to the [example input file](https://raw.githubusercontent.com/nf-core/test-datasets/fetchngs/sra_ids_test.csv) named in the [Fetchngs README](https://github.com/nf-core/fetchngs).
