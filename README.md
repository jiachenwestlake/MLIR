# MLIR
## Code for the paper "Meta-learning the invariant representation for domain generalization".

The code is built upon an open-source toolkit [DomainBed](https://github.com/facebookresearch/DomainBed).

### Requirements
```
python>=3.7 
torch>=1.8.1
torchvision
```
### Dataset Download
```
python scripts/download.py \
       --data_dir=data
```

### Sample Commands
**Train a model:**
```
python scripts/train.py \
    --data_dir=data/PACS/ \
    --output_dir=train_output/ \
    --algorithm DOML \
    --dataset PACS \
    --test_env 2 \
```

**Launch a sweep:**

The entire sweep trains many models (3 independent trials x 20 random hyper-parameter choices).
```
python scripts/sweep.py launch \
       --data_dir=data/PACS/ \
       --output_dir=train_output/ \
       --command_launcher MyLauncher \
       --algorithms DOML \
       --datasets PACS \
       --n_hparams 20 \
       --n_trials 3 \
```

**View the results:**
```
python scripts/collect_results.py \
       --input_dir=train_output/ \
```

## Cite:
If you use our code, please cite our paper as follows:
```
@article{jia2022-meta,
    title = "Meta-learning the invariant representation for domain generalization",
    author = "Jia, Chen  and  Zhang, Yue",
    journal = "Machine learning",
    year = "2022",
    publisher = "Springer Nature",
    eprint = "https://link.springer.com/content/pdf/10.1007/s10994-022-06256-y.pdf",
    pages = "1--21"
}
```
