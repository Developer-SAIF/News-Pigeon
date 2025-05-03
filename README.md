# Project Structure

my-react-app/
├── frontend/                   # Frontend (React/Vite app)
│   ├── public/
│   ├── src/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── netlify.toml
│   └── .gitignore
├── backend/                    # Backend (Flask API)
│   ├── api/
│   │   ├── extract_news.py
│   │   ├── news_api.py
│   │   └── requirements.txt
│   ├── vercel.json
│   └── .gitignore
├── README.md                   # General project documentation
└── .gitignore                  # Root-level ignores (optional)

## Deployment

### Frontend (Netlify)
1. Navigate to the `frontend/` directory:
   ```sh
   cd frontend