# 💳 Credit Card Fraud Detection  

🚀 **Live App:** [Streamlit Deployment](https://credit-card-fraud-detection-levv6hskbwbh9jncykytgc.streamlit.app/)  

---

## 📖 Project Overview 
 

This project demonstrates how **Machine Learning (ML)** can be applied to detect fraud in financial transactions. I developed, trained, and deployed a model that predicts whether a transaction is **legitimate or fraudulent**.  

It is not production-level software, but a **learning project** where I explored the full ML workflow — from dataset → model → deployment.  


---

## 🛠️ Skills & Concepts Demonstrated  

- 📂 **Data Handling:** Worked with the Kaggle Credit Card Fraud dataset.  
- 🧹 **Preprocessing:** Applied scaling and prepared features.  
- 🌲 **Model Training:** Trained a **Random Forest Classifier**.  
- 📊 **Evaluation:** Accuracy, Precision, Recall, Confusion Matrix.  
- 💾 **Model Persistence:** Saved trained model as `model.pkl`.  
- 🌐 **Deployment:** Created a **Streamlit web app** for live predictions.  
- 🔗 **Version Control & Deployment:** Used GitHub + Streamlit Cloud for deployment.  

This helped me gain **end-to-end ML project experience** — from dataset → model → deployment.  

---

## ⚙️ How the App Works  

1. User enters transaction details (Amount + features V1–V28).  
2. The trained ML model (`model.pkl`) is loaded.  
3. Model predicts:  
   - ✅ **Normal Transaction (0)**  
   - ⚠️ **Fraudulent Transaction (1)**  
4. The result is displayed in the app instantly.  

---

## 📊 Dataset Information  

- **Source:** [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)  
- **Total Records:** 284,807 transactions  
- **Fraud Cases:** 492 (~0.17% of the dataset)  
- **Features:**  
  - `V1–V28` (PCA-transformed features)  
  - `Amount` (transaction value)  
  - `Class` (0 = normal, 1 = fraud)  

---

## 📐 Model Details  

- **Algorithm:** Random Forest Classifier  
- **Reason for choice:**  
  - Works well on imbalanced data  
  - Handles nonlinear patterns  
  - Provides stable baseline performance  
- **Output:** Model stored as `model.pkl`, used directly by the app  

---

## 📚 Key Skills Gained  

- Designing a **machine learning workflow** (data → model → deployment)  
- Handling **imbalanced datasets** effectively  
- Saving & reusing ML models  
- Building **interactive Streamlit apps**  
- Managing projects with **Git & GitHub**  
- Deploying models to the cloud  

---

## ⚠️ Important Notes  

To get **accurate fraud predictions**, the model needs data that matches the **real dataset structure** (as provided in `creditcard.csv`).  

- The model was trained on real-world transaction patterns.  
- Random inputs may not reflect realistic fraud scenarios.  
- In production, fraud detection systems combine multiple factors such as:  
  - User behavior (time, location, device)  
  - Merchant details  
  - Risk scoring systems  
  - Continuous retraining with new data  

📌 This project is created for **educational and learning purposes** to demonstrate practical ML skills and end-to-end deployment.  


---

## 👤 Author  

**Rupesh Kumar Shah**  
- 🎯 Aspiring **AI/ML Engineer** 
- 🐙 GitHub: [iamrupesh1](https://github.com/iamrupesh1)  
- 💼 LinkedIn: [Rupesh Kumar Shah](https://linkedin.com/in/rupesh-kumar-shah)  

---

✨ **Takeaway:**  
This project highlights my ability to build a **complete ML solution** — from dataset preparation to deployment — while also understanding real-world challenges in fraud detection.  
