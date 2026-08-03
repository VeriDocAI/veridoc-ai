# VeriDoc AI — Configuration Management

This directory manages configuration parameters for environments, models, training workflows, inference services, and orchestration pipelines.

## 📂 Configuration Directories

*   **`environments/`**: System-level and environment-specific settings (e.g., local, dev, staging, prod, hardware configurations like CPU/GPU/TPU configs).
*   **`models/`**: Hyperparameters, model architecture definitions, and prompt templates for specific Vision-Language Models (e.g., `qwen2.5-vl-3b.yaml`).
*   **`training/`**: Training pipeline configurations, including batch sizes, learning rates, optimizers, loss functions, epoch counts, and evaluator settings.
*   **`inference/`**: Configuration for production serving endpoints, batch inference jobs, auto-scaling thresholds, and decoding parameters.
*   **`pipelines/`**: Orchestration and data preprocessing pipeline settings, ETL configurations, and end-to-end task mapping parameters.

## 📝 Conventions

1.  Configurations should prefer readable formats such as YAML or JSON.
2.  Environment-specific secrets (e.g. database credentials, API keys) must **never** be checked in here; load them from environment variables via a configuration manager (e.g., Pydantic Settings).
