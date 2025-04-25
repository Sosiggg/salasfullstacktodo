# 📝 SalasFullStackToDoApp Backend

This is the backend of the **SalasFullStackToDo** application. It is built using **FastAPI** and deployed on **Render**. It provides a RESTful API for managing tasks with full **CRUD** (Create, Read, Update, Delete) functionality.

## 🚀 Features

- FastAPI-based REST API  
- PostgreSQL database  
- Full CRUD operations for tasks  
- CORS enabled for frontend integration  
- Deployed on Render

## 🛠 Tech Stack

- **FastAPI**  
- **Uvicorn**  
- **SQLAlchemy**  
- **PostgreSQL**  
- **Render** (for deployment)

## ▶️ Running Locally

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/salasfullstacktodo-backend.git
cd salasfullstacktodo-backend
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set up environment variables** (e.g., in \`.env\` file or system environment):

```
DATABASE_URL=postgresql://user:password@localhost/dbname
```

4. **Run the app:**

```bash
uvicorn main:app --reload
```

## 🌐 Live API (Render)

You can access the deployed API here:  
👉 **[https://salasfullstacktodo.onrender.com/docs/](https://salasfullstacktodo.onrender.com/docs/)**

## 📮 API Endpoints

- \`GET /tasks/list/\` - List all tasks  
- \`POST /tasks/create/\` - Create new task  
- \`GET /tasks/detail/{task_id}/\` - Get task by ID  
- \`PUT /tasks/update/{task_id}/\` - Update task by ID  
- \`DELETE /tasks/delete/{task_id}/\` - Delete task by ID 

## 📌 Notes

- Make sure CORS is configured to allow requests from your frontend.  
- This backend is meant to be used with the **React Native Expo frontend** of the same app. 
