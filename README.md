# 🌾 Agribot – AI-Powered Agriculture Assistant 🤖

Agribot is a web-based AI/ML solution designed to assist Indian farmers in making informed agricultural decisions. It delivers **intelligent crop recommendations** and **real-time farming support** through a chatbot — leveraging machine learning and NLP to empower sustainable and productive farming practices.

> 🔗 Live LinkedIn Project Post: [See the Announcement](https://www.linkedin.com/posts/renjish-k-s-13669b2b6_ai-machinelearning-agritech-activity-7355444681071112193-wsnN?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEvri_oBXCIQ98AFEIFRY4uK-qnoXT4ju3U)

---

## 👥 Team

- 👨‍💻 [Renjish K. S](https://www.linkedin.com/in/renjish-k-s-13669b2b6/)
- 👩‍💻 Santa Saji  
**MCA Final Year Students**  
Mar Athanasius College of Engineering (2023–2025)

---

## 🚀 Project Highlights

| Module | Description |
|--------|-------------|
| 🌱 **Crop Recommendation** | Built using **Random Forest Classifier**, suggests the most suitable crops based on soil and weather inputs. |
| 💬 **NLP Chatbot** | Powered by **BART model**, trained on agricultural Q&A dataset to answer real-time farming queries. |
| 🌐 **Web App** | Built using **Python + Django** backend and **HTML/CSS/JavaScript** frontend. |
| ☁️ **Offline-Ready** | Designed for **rural accessibility** and offline deployment. |
| 📈 **Performance** | ML accuracy ~99%, Chatbot BLEU/ROUGE improved steadily over 25 epochs. |

---

## 🛠️ Tech Stack

- Python
- Django
- HTML, CSS, JavaScript
- Scikit-learn
- PyTorch Lightning
- Hugging Face Transformers (`facebook/bart-base`)
- Google Colab (for training)
- Kaggle Datasets

---

## 📊 Key Features

### 🌾 Crop Recommendation System
- Inputs: `N, P, K, Temperature, Humidity, pH, Rainfall`
- Model: **Random Forest Classifier**
- Accuracy: **~99%**
- Dataset: [Kaggle Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

### 🧠 Chatbot Assistant
- NLP Model: **BART** fine-tuned on real agricultural Q&A
- Dataset: [Kaggle - Combined Dataset (JSON)](https://www.kaggle.com/datasets/eraydikyololu/combined-dataset?select=concatenated_output.json)
- Evaluated with BLEU and ROUGE metrics

---

## 🧪 Training & Inference

### 📂 Model Training Code
🔗 [Training Notebook (Google Drive)](https://drive.google.com/file/d/1pQntItTpO2-39e_2G35nK8l9GnG0BN6q/view?usp=drive_link)

### 📦 Download Trained Chatbot Model
🔗 [Trained BART Model Path](https://drive.google.com/file/d/1TdC8-ZtmYUYew2NucMX1iu2iHa9R74IC/view?usp=drive_link)

> You can download this and load it directly into your chatbot system using Hugging Face’s `BartForConditionalGeneration`.



---

## 📁 Project Structure
Agribot/
│
├── crop_model/ # Random Forest Model (saved as .pkl)
├── chatbot_model/ # Trained BART Model
├── templates/ # HTML pages
├── static/ # CSS & JS files
├── chatbot/ # NLP logic
├── recommendation/ # ML logic
├── train/ # Training scripts
├── manage.py # Django entry point
└── README.md




---

## 🧠 Future Enhancements

- Multilingual chatbot for local language support
- Integration with live weather and crop disease APIs
- Mobile app interface for offline-first access
- Crop health image classification via deep learning

---

## 🤝 Let's Collaborate

This project is open for feedback, contributions, and collaboration opportunities in the AgriTech space. If you're interested in working on AI for agriculture — feel free to reach out!

---

## 📬 Contact

📌 **Renjish K. S**  
📧 Email: renjishksimon@gmail.com  
📱 Phone: +91 9567225114  
🔗 [LinkedIn](https://www.linkedin.com/in/renjish-k-s-13669b2b6/)

---

> 🌟 If you like this project, please give it a star on [GitHub](https://github.com/Renjish-k-s/Agribot)!


