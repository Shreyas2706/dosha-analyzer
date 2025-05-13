# 🧠 Dosha Analysis API

> A lightweight and efficient FastAPI-based backend service to analyze Ayurvedic **Dosha profiles** (Vata, Pitta, Kapha) using user-submitted physical and lifestyle data.

---

## 🚀 Live Endpoint

**POST Endpoint:**  
[`https://dosha-analyzer.onrender.com/log_data`](https://dosha-analyzer.onrender.com/log_data)

This API accepts health and wellness-related user data and returns the predicted Dosha dominance based on Ayurvedic principles.

---

## 🔧 Tech Stack

- **🧠 FastAPI** — Modern, fast (high-performance), web framework for APIs  
- **🔢 Pydantic** — For data validation and schema enforcement  
- **🤖 ML Model** — Vector-based Dosha prediction engine trained on Ayurvedic attributes  

---

## 📦 API Usage

### 📮 Endpoint

```http
POST /log_data
Content-Type: application/json
```

### ✅ Sample Payload

```json
{
  "bodyFrame": "Thin",
  "skinType": "Dry",
  "hairType": "Soft",
  "digestivePattern": "Irregular",
  "energy": "Erratic",
  "sleep": "Interrupted",
  "emotion": "Anxious",
  "physicalActivity": "Irregular",
  "diet": "Light",
  "ageGroup": "20-30",
  "sex": "Female",
  "city": "Bhopal",
  "country": "India",
  "mainHealthGoal": "Reduce anxiety",
  "medicalCondition": "None",
  "foodAllergies": ["Oats", "Ghee"]
}
```

### 📤 Sample Response

```json
{
  "dominant_dosha": "Vata",
  "confidence_scores": {
    "Vata": 0.83,
    "Pitta": 0.12,
    "Kapha": 0.05
  },
  "suggestions": [
    "Eat warm, cooked, grounding foods",
    "Follow a consistent daily routine",
    "Practice gentle yoga and calming meditation"
  ]
}
```

---

## 🧪 Run Locally

```bash
git clone https://github.com/CARBOnauts/dosha-analyzer.git
cd dosha-analyzer
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 📁 Project Structure

```
📦 dosha-analyzer
├── main.py               # FastAPI application entry point
├── model/                # ML models or logic (if separated)
├── schemas.py            # Pydantic models for request validation
├── utils.py              # Utility functions for scoring & logic
├── requirements.txt      # Dependencies
└── README.md             # You're reading it 🙂
```

---

## 🛡️ Disclaimer

This API is built for educational and wellness support use only.  
It does **not** substitute professional medical advice, diagnosis, or treatment.

---

## 🔗 Related

- 🌿 [AyurWell App (Frontend)](https://ayurwell.onrender.com)  
- 📁 [GitHub Repo (Frontend)](https://github.com/aAdi0103/AyurWell)

---

## 🙌 Contributing

We welcome contributions to improve the Dosha prediction model, optimize API performance, or add more endpoints!  
Feel free to fork and raise a PR.

---

## 📫 Contact

For questions, feedback, or collaboration:

📩 Email: [shreyassingh4453@gmail.com](mailto:shreyassingh4453@gmail.com)
