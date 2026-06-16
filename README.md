# Artificial Intelligence Internship - InternSpark (Alfido Tech)

Name: Sajal Sowna

This repository contains the internship tasks completed for the Artificial Intelligence Internship.

## Tasks Completed

### Task 2 - Deep Learning: Resume Classification

- Built a Resume Classification System
- Used NLP and Bidirectional LSTM
- Generated evaluation metrics and visualizations

Folder:

Task2_DeepLearning/

---

### Task 3 - Model Deployment

- Deployed the model using FastAPI
- Created prediction API endpoints
- Tested using Swagger UI

Folder:

Task3_Deployment/

---

### Task 4 - Responsible AI

- Performed fairness analysis
- Generated LIME explanations
- Proposed mitigation strategies

Folder:

Task4_ResponsibleAI/

## Environment Setup

Create virtual environment

```bash
python -m venv venv
```

Activate environment

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Task 3 API

```bash
cd Task3_Deployment

uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```
