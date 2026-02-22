# AI Portfolio - Gulabchandu Appana

A modern, responsive portfolio website showcasing Gen AI and Agentic AI projects, built with FastAPI and Tailwind CSS.

## Features

- 🎨 Modern, responsive design with dark mode support
- 🤖 Showcase of AI/ML projects
- 📝 Contact form integration
- 🔗 Social media links (LinkedIn, GitHub)
- ⚡ Fast FastAPI backend
- 📱 Mobile-friendly

## Local Setup

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd portfolio
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
python app.py
```

5. Open your browser and visit:
```
http://localhost:8000
```

## Deployment on Railway

### Steps:

1. **Create GitHub Repository:**
   - Push this project to GitHub
   - Include all files (app.py, templates/, static/, requirements.txt)

2. **Deploy on Railway:**
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub"
   - Connect your GitHub account
   - Select this repository
   - Railway auto-detects Python project
   - Deploy!

3. **Your portfolio will be live at:**
   - `https://<your-app-name>.railway.app`

### Environment Variables (if needed on Railway):
- No API keys required for basic deployment
- Add `.env` file for any API integrations later

## Project Structure

```
portfolio/
├── app.py                 # FastAPI application
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
├── templates/
│   └── templates.html    # Portfolio HTML
└── static/
    └── images/
        └── profile.jpg   # Profile picture
```

## Technologies Used

- **Backend:** FastAPI, Uvicorn
- **Frontend:** HTML, CSS (Tailwind), JavaScript
- **Icons:** Lucide Icons
- **Hosting:** Railway

## Contact

- **Email:** gulabchanduappana30@gmail.com
- **LinkedIn:** [Gulabchandu Appana](https://www.linkedin.com/in/gulabchandu-appana-b1a604377)
- **GitHub:** [gulabchanduappana30-star](https://github.com/gulabchanduappana30-star)

---

Built with ❤️ by Gulabchandu Appana
