# 💼 Job Board Platform

A full-featured Job Board Platform built with **Flask** and **SQLite** as part of my **Backend Development Internship at CodeAlpha**.

---

## 🚀 Features

- ✅ Post & manage job listings
- ✅ Search jobs by title, category & location
- ✅ Apply for jobs with resume upload
- ✅ Track application status (Pending / Shortlisted / Rejected)
- ✅ Dashboard with real-time analytics
- ✅ Clean & modern responsive UI
- ✅ Employer & candidate management

---
## Project Structure

```
fyp-deepfake-detector/
├── api/
│   └── main.py              # FastAPI backend (image / audio / video / gradcam endpoints)
├── src/
│   ├── dataset.py           # Visual dataset loader (FaceForensics++, Celeb-DF, DFDC)
│   ├── train.py             # EfficientNet-B0 trainer
│   ├── train_xception.py    # XceptionNet trainer
│   ├── train_vit.py         # ViT-Small trainer
│   ├── ensemble.py          # Visual ensemble inference
│   ├── evaluate_ensemble.py # Visual ensemble evaluation
│   ├── audio_dataset.py     # ASVspoof2019 LA dataset loader
│   ├── train_audio.py       # LCNN trainer
│   ├── audio_classifier.py  # LCNN inference
│   ├── evaluate_audio.py    # Audio evaluation (EER, AUC)
│   ├── multimodal_fusion.py # MultimodalDetector — combines visual + audio
│   └── gradcam.py           # Grad-CAM explainability
├── frontend/
│   └── index.html           # Web UI (drag-drop, animated verdict, history, heatmap)
├── checkpoints/             # Model weights (not tracked in git)
├── logs/                    # Training/eval logs and JSON results
├── requirements-api.txt     # FastAPI dependencies
└── requirements-mlops.txt   # Training dependencies
```

---

### 1. Environment
```bash
python -m venv venv
source venv/bin/activate 
```

### 2.Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```

Open `http://127.0.0.1:5000`

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.14 | Backend logic |
| Flask | Web framework |
| SQLite | Database |
| Flask-SQLAlchemy | ORM |
| HTML + CSS | Frontend |
| Git & GitHub | Version control |

---

##  Team
| Name | 
|------|
| Taha Sohail| 

---
