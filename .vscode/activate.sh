#!/bin/bash
# Ensure conda functions are available
if [ -f "$HOME/miniconda3/etc/profile.d/conda.sh" ]; then
    source "$HOME/miniconda3/etc/profile.d/conda.sh"
fi
# Force activation of ML_Learning environment
conda activate ML_Learning
