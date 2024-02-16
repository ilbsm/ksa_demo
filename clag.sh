#!/bin/bash
#SBATCH --job-name="ClstAgnt"
#SBATCH --ntasks=1
#SBATCH --mem=1gb
#SBATCH --partition=long
#SBATCH --output=ClstAgnt_slurm.out
source $HOME/dev/ksa_demo/venv/bin/activate
cd $HOME/dev/ksa_demo
faust -A kafka_slurm_agent.cluster_agent -l info worker > logs/cluster_agent_out.txt
