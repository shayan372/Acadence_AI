# 🎓 Acadence AI

> **An AI-powered academic workload management and prioritization platform for students.**

Acadence AI is an intelligent academic productivity application designed to help students organize their academic tasks, understand their workload, and determine which tasks should receive attention first.

By combining **AI-powered recommendations** with a structured academic priority system, Acadence AI helps students make better decisions about assignments, exams, quizzes, projects, and other academic responsibilities.

---

## 🚀 Key Features

### 📋 Academic Task Management

* Add and manage academic tasks
* Track assignments, quizzes, exams, and projects
* Record deadlines and estimated workload
* Organize academic responsibilities in one place

### 🧠 AI-Powered Recommendations

* Uses **Groq AI** to generate intelligent academic recommendations
* Analyzes current tasks and workload
* Provides actionable suggestions based on academic priorities
* Helps students determine what to work on first

### ⭐ Smart Priority System

Acadence AI evaluates academic tasks using factors such as:

* Deadline
* Task priority
* Estimated workload
* Academic urgency
* Current workload

The system helps students identify tasks that require immediate attention.

### 📊 Workload Analysis

* Analyzes the student's academic workload
* Helps identify periods of high workload
* Supports better academic planning
* Provides useful workload insights

### 🤖 AI Academic Assistant

The AI assistant provides personalized academic guidance based on the student's current tasks and workload.

### 💾 Data Management

Acadence AI uses **SQLite** for task storage and **Pandas** for data processing and workload analysis.

### ☁️ Cloud Deployment

The application can be deployed through **Streamlit Cloud**, allowing students to access the application without complex local setup.

---

# 🎯 Problem Statement

Students often have to manage multiple academic responsibilities simultaneously, including assignments, quizzes, exams, projects, and presentations.

When several deadlines overlap, students may struggle to determine:

* What should be completed first?
* Which task is most urgent?
* How much workload is currently pending?
* How should available study time be distributed?

Traditional task-management systems mainly show students **what they need to do**, but they do not necessarily help them understand **what they should prioritize**.

Acadence AI addresses this problem by combining academic task management, workload analysis, priority evaluation, and AI-powered recommendations in one platform.

---

# 💡 Solution

Acadence AI provides students with a centralized academic management system where they can enter their academic tasks and receive intelligent recommendations.

The system:

1. Collects academic task information.
2. Stores and organizes the student's workload.
3. Evaluates task priorities.
4. Analyzes the overall workload.
5. Uses Groq AI to generate personalized recommendations.
6. Presents actionable academic guidance to the student.

This transforms a simple task list into an **intelligent academic planning assistant**.

---

# 🏗️ High-Level Architecture

```text
                    ┌─────────────────────┐
                    │       Student       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Streamlit UI     │
                    │       app.py        │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
     ┌────────────────┐ ┌───────────────┐ ┌────────────────┐
     │ Task & Data    │ │ Priority      │ │ Workload       │
     │ Management     │ │ Engine        │ │ Analyzer       │
     │ database.py    │ │ priority_     │ │ workload_      │
     │                │ │ engine.py     │ │ analyzer.py    │
     └────────┬───────┘ └───────┬───────┘ └───────┬────────┘
              │                 │                 │
              └─────────────────┼─────────────────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │   AI Assistant     │
                     │  ai_assistant.py   │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │     Groq AI        │
                     │ Recommendations    │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │ Student receives  │
                     │ recommendations   │
                     └────────────────────┘
```

---

# 🛠️ Technology Stack

| Technology          | Purpose                               |
| ------------------- | ------------------------------------- |
| **Python**          | Core application development          |
| **Streamlit**       | Web application interface             |
| **Groq AI**         | AI-powered academic recommendations   |
| **SQLite**          | Academic task and data storage        |
| **Pandas**          | Data processing and workload analysis |
| **GitHub**          | Source code management                |
| **Streamlit Cloud** | Application deployment                |

---

# 📂 Project Structure

```text
Acadence_AI/
│
├── .gitignore
├── ai_assistant.py
├── app.py
├── database.py
├── priority_engine.py
├── requirements.txt
├── workload_analyzer.py
└── README.md
```

### Core Files

| File                   | Purpose                                                   |
| ---------------------- | --------------------------------------------------------- |
| `app.py`               | Main Streamlit application and user interface             |
| `ai_assistant.py`      | AI-powered academic recommendations                       |
| `database.py`          | Database operations and task storage                      |
| `priority_engine.py`   | Academic task priority calculation                        |
| `workload_analyzer.py` | Workload analysis and academic insights                   |
| `requirements.txt`     | Python dependencies                                       |
| `.gitignore`           | Prevents unnecessary/sensitive files from being committed |

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/shayan372/Acadence_AI.git
cd Acadence_AI
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure the Groq API Key

Configure your Groq API key using the method implemented in the application.

For local development, use an environment variable or appropriate secrets configuration.

Example:

```text
GROQ_API_KEY=your_api_key_here
```

> ⚠️ **Never commit API keys or other sensitive credentials to GitHub.**

## 5. Run the Application

```bash
streamlit run app.py
```

The application will then be available in your browser.

---

# ☁️ Deployment

Acadence AI is designed for deployment using **Streamlit Cloud**.

### Deployment Steps

1. Push the project to GitHub.
2. Connect the GitHub repository to Streamlit Cloud.
3. Select `app.py` as the main application file.
4. Configure the required secrets/API key.
5. Deploy the application.
6. Access the generated application URL.

---

# 🔐 Security

Acadence AI follows basic security practices for application development:

* API keys should be stored securely.
* Sensitive credentials should never be committed to GitHub.
* `.gitignore` should be used to exclude local secrets and unnecessary files.
* Streamlit Secrets or environment variables should be used for deployment credentials.

---

# 🌟 Why Acadence AI?

Students don't just need a list of academic tasks — they need help deciding **what to do next**.

Acadence AI combines:

**Task Management + Priority Analysis + Workload Analysis + AI Recommendations**

This provides students with a more intelligent approach to managing their academic workload.

---

# 🔮 Future Enhancements

Possible future improvements include:

* 📅 Calendar integration
* 🔔 Smart deadline notifications
* 📱 Dedicated mobile application
* 📈 Advanced academic analytics
* 🧠 More personalized AI recommendations
* 📚 Automated study-plan generation
* 🔄 Intelligent task scheduling
* 👥 Student collaboration features
* ☁️ Improved cloud-based data synchronization

---

# 👥 Team Members

| # | Team Member           | Role                          | Contribution                                                                                                       |
| - | --------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 1 | **Saad Ali Siddiqui** | **Team Lead**                 | Project coordination, system planning, team management, and overall project direction                              |
| 2 | **Muhammad Shayan**   | **AI & Full-Stack Developer** | Application development, Groq AI integration, academic prioritization system, database integration, and deployment |
| 3 | **Owais**             | **Backend & Data Developer**  | Backend functionality, data handling, database operations, and integration of core application features            |
| 4 | **Faheem Yar Khan**   | **UI & Documentation**        | User interface improvements, presentation materials, documentation, and project testing                            |
| 5 | **Salman Sheikh**     | **Testing & Project Support** | Application testing, feature validation, troubleshooting, and overall project support                              |

---

# 🏆 Project

**Acadence AI** is a collaborative AI-powered academic productivity project developed to help students better organize, understand, and prioritize their academic workload.

The project combines traditional academic task management with intelligent AI-based recommendations to provide a more useful and personalized student experience.

---

# 📄 License

This project is developed for **educational and hackathon purposes**.

---

## 👨‍💻 Built With

**Python • Streamlit • Groq AI • SQLite • Pandas • GitHub • Streamlit Cloud**

---

⭐ **If you find Acadence AI useful, consider giving the repository a star!**

**GitHub Repository:**
https://github.com/shayan372/Acadence_AI
