# **Document Management and RAG-based Q&A API**  

## **Overview**  
This project is a **FastAPI-based backend** that allows users to:  
✅ Upload text documents 📄  
✅ Store and retrieve documents 📂  
✅ Perform similarity-based search using embeddings 🔍  

The application utilizes **FAISS (Facebook AI Similarity Search)** for efficient document retrieval and **Hugging Face Sentence Transformers** for generating vector embeddings.  

---

## **Features**  
- 📤 **Upload documents** and store them for later retrieval  
- 🔍 **Search documents** using a query, retrieving the most relevant results  
- 🚀 Built using **FastAPI**, ensuring a lightweight and high-performance backend  

---

## **Technologies Used**  
- **FastAPI** - Web framework for building APIs  
- **FAISS** - Efficient similarity search and clustering of dense vectors  
- **Hugging Face Sentence Transformers** - Embeddings for semantic search  
- **Uvicorn** - ASGI server for running FastAPI applications  

---

## **Installation & Setup**  

### **1️⃣ Prerequisites**  
Ensure you have **Python 3.9+** installed.  

### **2️⃣ Install Required Packages**  
Run the following command:  
```bash
pip install fastapi uvicorn langchain_community pydantic
```
*Note:* If `langchain_community` is not installed, update LangChain using:  
```bash
pip install -U langchain
```

### **3️⃣ Run the API Server**  
To start the FastAPI server, run:  
```bash
uvicorn main:app --reload
```
This will start the server on **http://127.0.0.1:8000/**  

---

## **API Endpoints & Usage**  

### **🏠 Home Route**
- **URL:** `/`
- **Method:** `GET`
- **Response:**  
```json
{
  "message": "Document Management and RAG-based Q&A API is running"
}
```

### **📤 Upload Document**  
- **URL:** `/upload/`  
- **Method:** `POST`  
- **Description:** Uploads a text document and stores it.  
- **Request Format:**  
  - `file`: UploadFile (Text file only)  
- **Response:**  
```json
{
  "message": "Document uploaded and processed successfully",
  "doc_id": 1
}
```
🔹 **Example CURL Request:**  
```bash
curl -X 'POST' 'http://127.0.0.1:8000/upload/' \
-H 'accept: application/json' -H 'Content-Type: multipart/form-data' \
-F 'file=@testfile.txt'
```

---

### **🔍 Search Documents**  
- **URL:** `/search/`  
- **Method:** `POST`  
- **Description:** Searches for relevant content in uploaded documents.  
- **Request Format:**  
  ```json
  {
    "query": "AI in Healthcare"
  }
  ```
- **Response Format:**  
  ```json
  {
    "query": "AI in Healthcare",
    "results": [
      {
        "content": "Artificial Intelligence (AI) is transforming the healthcare industry..."
      }
    ]
  }
  ```

🔹 **Example CURL Request:**  
```bash
curl -X 'POST' 'http://127.0.0.1:8000/search/' \
-H 'accept: application/json' -H 'Content-Type: application/json' \
-d '{"query": "AI in Healthcare"}'
```

---

## **📸 Example Outputs**
### **Uploaded Document Example**
```
Title: AI in Healthcare  

Artificial Intelligence (AI) is transforming the healthcare industry  
by improving diagnosis, patient care, and research.  
Machine learning models help detect diseases at an early stage...
```
### **Search Example Output**
```
Query: "AI in Healthcare"  
Results:  
1. "Artificial Intelligence (AI) is transforming the healthcare industry..."
```

---

## **Difficulties Faced (If Any)**  
While implementing this project, some challenges were encountered:  
1️⃣ **Dependency Issues:** The deprecation warnings in `langchain_community` required updating the imports.  
2️⃣ **Embedding Model Choice:** Initially, OpenAI embeddings were used, but switched to **Hugging Face** models to avoid API key dependencies.  
3️⃣ **API Testing:** Some issues were encountered with `curl` commands on Windows CMD.  
4️⃣ **Swagger UI Issues:** Clicking API endpoints directly on **http://127.0.0.1:8000/docs** sometimes resulted in `"Method Not Allowed"` due to incorrect method usage.  

---

## **Future Improvements** 🚀  
✔ Store documents in a **database** instead of in-memory storage  
✔ Improve **search ranking** by implementing more advanced ranking algorithms  
✔ Deploy on **Render or Railway** for public access  
✔ Implement **file type validation** to ensure only `.txt` files are processed  

---

## **Submission Details**  
- 📂 **File Name:** `Backend_Assignment_YourName.docx`  
 

---
  
### **Developed By: [Your Name]**  
**Date:** _(Submission Date)_  
🚀 _Backend API for document management and retrieval using FastAPI & FAISS_  

---

This README covers **everything** needed for submission! You can copy-paste and edit details as needed. 🚀
