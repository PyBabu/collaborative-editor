# 📝 Collaborative Document Editor with Grammar Check

This Django-based project allows users to collaboratively edit rich-text documents in real-time while receiving grammar suggestions powered by LanguageTool. It supports user registration, authentication (including social login), document creation, and live editing via WebSockets.

---

## 🚀 Features

- ✅ User Registration & Login
- 🔐 Social Authentication (Google, GitHub)
- 📄 Create, View, and Edit Documents
- 🤝 Real-time Collaboration (WebSockets)
- ✏️ Grammar Checking (via LanguageTool API)
- 💾 Auto-save with timestamp
- 👥 View online collaborators

---

## 📷 Screenshots
### Home View 
![Home](HOME page.jpg)
### Register View 
![Register](register.jpg)
### login View 
![Login](signin.jpg)
### About View 
![About](about dev.jpg)
### Dashboard View  
![Dashboard](suggestion.jpg)
### Editor with Grammar Suggestions  
![Editor](suggestion.jpg)


---

## ⚙️ Getting Started

### Prerequisites

- Python 3.8+
- Django 4.x
- Redis (for WebSocket support via Django Channels)
- Git

### Installation Steps

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/collab-editor.git
cd collab-editor
