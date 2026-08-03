# VeriDoc AI — Experiment Management

This directory manages configurations, checkpoint files, and logs for local machine learning training and evaluation runs.

## 📂 Folder Conventions

Local experiments should be organized under subfolders named by timestamp and experiment ID:
```text
training/experiments/
└── YYYYMMDD-HHMMSS_<model-name>_<experiment-slug>/
    ├── config.yaml          # Backup of the configuration used for this run
    ├── checkpoints/         # Model weights saved during training
    ├── logs/                # TensorBoard event files, standard output, and warnings
    └── evaluations/         # Predictions and evaluation reports generated at checkpoints
```

## 📝 Rules & Best Practices

1.  **Reproducibility**: Always backup the full configuration used for the run into the experiment directory.
2.  **Tracking**: Later, these directories can be synced to Weights & Biases (W&B) or MLflow.
3.  **Large Files**: Model checkpoint files (`*.bin`, `*.pt`, `*.safetensors`) must **never** be committed to Git. They are automatically excluded by the repository's `.gitignore` rules.
