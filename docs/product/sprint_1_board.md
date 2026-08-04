# 📋 Sprint 1 Board — Baseline Vision-Language Platform

## 🎯 Sprint Goal
> Build the first end-to-end inference pipeline for a Vision-Language Model capable of understanding documents, establishing the baseline for all future fine-tuning and AI services.

---

## 📍 Sprint Objective
By the end of Sprint 1, VeriDoc AI should be able to:
1. Load a Vision-Language Model.
2. Accept a document image.
3. Process the image.
4. Answer questions about the document.
5. Expose the functionality through a FastAPI endpoint.

> [!NOTE]
> There is **no fine-tuning** in this sprint. The goal is to build a reusable **inference platform** infrastructure.

---

## 🏆 Success Criteria
Sprint 1 is complete when:
*   [ ] Baseline VLM selected and documented.
*   [ ] Model loads successfully on RTX 5050 (8 GB).
*   [ ] Inference works on at least one benchmark document.
*   [ ] FastAPI endpoint returns model responses.
*   [ ] Docker container runs successfully.
*   [ ] End-to-end demo works.

---

## 🗂️ Epic [E1] Baseline Vision-Language Platform (#58)
**Description**: Establish the first production-ready Vision-Language inference pipeline that serves as the foundation for future LoRA fine-tuning, evaluation, and enterprise document intelligence services.

### Feature [F1.1] Model Evaluation & Selection (#43)
**Goal**: Evaluate candidate Vision-Language Models and select the baseline architecture for VeriDoc AI.

*   **T1.1.1: Evaluate Candidate Vision-Language Models (#39)**
    *   **Priority**: Urgent | **Estimate**: 3 SP
    *   **Acceptance Criteria**: Compare candidate models, evaluate GPU requirements, evaluate licensing, evaluate document understanding capability, and document findings.
*   **T1.1.2: Select Baseline Model (#40)**
    *   **Priority**: Urgent | **Estimate**: 1 SP
    *   **Acceptance Criteria**: Architecture selected, decision documented, and Model Card created.
*   **T1.1.3: Create Model Card (#41)**
    *   **Priority**: Medium | **Estimate**: 2 SP
    *   **Acceptance Criteria**: Document architecture, parameters, context length, license, training strategy, hardware requirements, and known limitations.
*   **T1.1.4: Define Inference Strategy (#42)**
    *   **Priority**: High | **Estimate**: 2 SP
    *   **Acceptance Criteria**: Document prompt format, image preprocessing, generation parameters, memory optimization, and quantization strategy.

---

### Feature [F1.2] Baseline Inference Pipeline (#49)
**Goal**: Run the selected Vision-Language Model locally.

*   **T1.2.1: Download Baseline Model (#44)**
    *   **Priority**: Urgent | **Estimate**: 1 SP
    *   **Acceptance Criteria**: Model weights successfully downloaded and cached.
*   **T1.2.2: Implement Model Loader (#45)**
    *   **Priority**: Urgent | **Estimate**: 3 SP
    *   **Acceptance Criteria**: Model loads successfully, GPU is detected, and CPU fallback is supported.
*   **T1.2.3: Build Image Processing Pipeline (#46)**
    *   **Priority**: High | **Estimate**: 3 SP
    *   **Acceptance Criteria**: Accept PNG/JPG/PDF (if supported), convert to model input format, and handle preprocessing correctly.
*   **T1.2.4: Implement Inference Engine (#47)**
    *   **Priority**: Urgent | **Estimate**: 5 SP
    *   **Acceptance Criteria**: Accept prompt, accept image, return generated response, and ensure stable execution.
*   **T1.2.5: Memory Optimization (#48)**
    *   **Priority**: High | **Estimate**: 3 SP
    *   **Acceptance Criteria**: Implement 4-bit quantization, use Flash Attention (if supported), perform VRAM profiling, and guarantee no Out-Of-Memory (OOM) errors on target hardware.

---

### Feature [F1.3] API Layer (#54)
**Goal**: Expose the baseline model through a production-style inference API.

*   **T1.3.1: Initialize FastAPI Service (#50)**
    *   **Priority**: High | **Estimate**: 2 SP
    *   **Acceptance Criteria**: FastAPI application bootstrapped with routing structure.
*   **T1.3.2: Implement Prediction Endpoint (#51)**
    *   **Priority**: Urgent | **Estimate**: 5 SP
    *   **Acceptance Criteria**: Endpoint `POST /predict` accepts image and query, returns inference text.
*   **T1.3.3: Implement Health Endpoint (#52)**
    *   **Priority**: Medium | **Estimate**: 1 SP
    *   **Acceptance Criteria**: Endpoint `GET /health` returns status of application and loaded model.
*   **T1.3.4: API Validation (#53)**
    *   **Priority**: Medium | **Estimate**: 2 SP
    *   **Acceptance Criteria**: Implement input validation, error handling, and robust response schema.

---

### Feature [F1.4] Sprint Demo (#57)
**Goal**: Deliver the first working AI capability.

*   **T1.4.1: End-to-End Demo (#55)**
    *   **Priority**: Urgent | **Estimate**: 3 SP
    *   **Acceptance Criteria**: User uploads a document → Model answers a question → Response returned through API.
*   **T1.4.2: Technical Documentation (#56)**
    *   **Priority**: Medium | **Estimate**: 2 SP
    *   **Acceptance Criteria**: Document setup, model, GPU settings, API execution, and known issues.

---

## 📊 Sprint 1 Backlog Visual
```
Sprint 1
Epic: #58 E1 Baseline Vision-Language Platform
├── #43 F1.1 Model Evaluation & Selection
│   ├── #39 T1.1.1 [ ] Compare & evaluate candidate VLMs
│   ├── #40 T1.1.2 [ ] Select architecture & document
│   ├── #41 T1.1.3 [ ] Create Model Card
│   └── #42 T1.1.4 [ ] Define Inference Strategy
├── #49 F1.2 Baseline Inference Pipeline
│   ├── #44 T1.2.1 [ ] Download baseline model
│   ├── #45 T1.2.2 [ ] Implement loader (GPU/CPU)
│   ├── #46 T1.2.3 [ ] Build image processing pipeline
│   ├── #47 T1.2.4 [ ] Implement inference engine
│   └── #48 T1.2.5 [ ] Quantization & VRAM optimization
├── #54 F1.3 API Layer
│   ├── #50 T1.3.1 [ ] Initialize FastAPI service
│   ├── #51 T1.3.2 [ ] POST /predict endpoint
│   ├── #52 T1.3.3 [ ] GET /health endpoint
│   └── #53 T1.3.4 [ ] Input validation & error schemas
└── #57 F1.4 Sprint Demo
    ├── #55 T1.4.1 [ ] E2E demo workflow
    └── #56 T1.4.2 [ ] Technical deployment docs
```

---

[← Back to Main Documentation Index](file:///c:/Users/Mohmmed%20Aarif/projects/Ai%20ComputerVision/veridoc-ai/docs/README.md)
