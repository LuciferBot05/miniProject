# ♻️ AI-Powered Smart E-Waste Management & Recycling Intelligence System

## 📌 Overview

Electronic waste (E-Waste) is one of the fastest-growing environmental problems in the modern world. Improper disposal of e-waste leads to serious health hazards and environmental pollution.

This project presents an **AI-based smart system** that automatically detects, classifies, and sorts electronic waste using **Artificial Intelligence, Computer Vision, and Arduino-based hardware**.

The system improves recycling efficiency, reduces human effort, and supports sustainable waste management.

---

## 🚀 Features

* 🔍 Automatic detection of e-waste using Infrared Proximity Sensor
* 🤖 AI-based classification of waste types
* ⚙️ Arduino-controlled servo motor for sorting
* ♻️ Automated waste segregation into different bins
* 📊 Efficient and real-time processing system

---

## 🛠️ Tech Stack

### Hardware

* Arduino Uno
* Infrared Proximity Sensor
* Servo Motor
* Jumper Wires

### Software

* Python
* OpenCV
* TensorFlow / Keras
* Arduino IDE

---

## ⚙️ System Workflow

1. Object is placed in the smart bin
2. Infrared Proximity Sensor detects object
3. AI model classifies type of e-waste
4. Signal is sent to Arduino
5. Servo motor rotates accordingly
6. Waste is sorted into the appropriate bin

---

## 🧠 AI Model

The system uses a **Convolutional Neural Network (CNN)** model to classify different types of electronic waste such as:

* Batteries
* Cables
* Circuit Boards
* Mobile Devices

The model is trained using image datasets and provides high accuracy in classification.

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/LuciferBot05/miniProject.git
cd miniProject
```

### 2️⃣ Install Dependencies

```bash
pip install opencv-python tensorflow numpy
```

### 3️⃣ Run the AI Model

```bash
python predict.py
```

### 4️⃣ Upload Arduino Code

* Open Arduino IDE
* Upload `.ino` file to Arduino board

---

## 📊 Output

* Detects and classifies e-waste
* Controls servo motor for sorting
* Displays classification results

(Add screenshots/images here)

---

## 🏗️ Project Structure

```
miniProject/
│
├── ai_model/
├── arduino_code/
├── backend/
├── tests/
├── predict.py
├── train_model.py
└── README.md
```

---

## 📈 Performance

* Accuracy: ~90%
* Fast response time
* Reliable sorting mechanism

---

## ⚠️ Limitations

* Limited dataset may affect accuracy
* Prototype-based implementation
* Not fully optimized for large-scale deployment

---

## 🔮 Future Scope

* IoT integration for real-time monitoring
* Mobile app for system control
* Cloud-based data analytics
* Improved AI model accuracy

---

## 📚 References

* Arduino Official Website
* OpenCV Documentation
* TensorFlow Documentation
* Kaggle Datasets
* UNEP E-Waste Report

---

## 👨‍💻 Team Members

* Satyarth Dahiya
* Tumesh Saini
* Dhairya Goyal

---

## ⭐ Conclusion

This project demonstrates how **AI and embedded systems** can be combined to solve real-world problems like e-waste management. It provides a smart, efficient, and scalable solution for modern waste handling systems.
