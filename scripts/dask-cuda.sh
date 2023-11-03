#!/bin/bash
#SBATCH -N1 --tasks-per-node=4
#SBATCH -p boost_usr_prod 
#SBATCH -t 30:00
#SBATCH --mem=100GB
#SBATCH --gres=gpu:4
#SBATCH -A cin_staff

module load cuda
prog="run-dask.py"
datafile="$CINECA_SCRATCH/very_huge.csv"
#source $HOME/modin/bin/activate
. "/leonardo/home/userinternal/aemerson/mambaforge/etc/profile.d/conda.sh"
. "/leonardo/home/userinternal/aemerson/mambaforge/etc/profile.d/mamba.sh"
mamba activate rapids-23.08
python ../src/run-dask-cuda.py -f $datafile > very_huge.out
