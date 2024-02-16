#!/bin/bash
#SBATCH --job-name="ClstAgnt"
#SBATCH --ntasks=1
#SBATCH --mem=1gb
#SBATCH --partition=long
#SBATCH --output=ClstAgnt_slurm.out
KSA_DIR=$HOME/dev/ksa_demo
source $KSA_DIR/venv/bin/activate
cd $KSA_DIR
faust -A kafka_slurm_agent.cluster_agent -l info worker > logs/cluster_agent_out.txt
