# 🧾 Transaction Webhook Service

## Fast, Reliable & Idempotent Webhook Processing System

A backend service built using **Python and FastAPI** that receives transaction
webhooks from external payment providers and processes them asynchronously.
The system is designed to acknowledge webhooks immediately while handling
transaction processing reliably in the background.

This project focuses on real-world backend concerns such as **performance,
idempotency, and reliability**, which are critical in payment and event-driven
systems.

---

## 🚀 What This Project Does

When a transaction webhook is received:

1. Validates the incoming webhook payload  
2. Stores the transaction with `PROCESSING` status  
3. Immediately responds with `202 Accepted`  
4. Triggers background processing with a simulated delay  
5. Updates the transaction status after processing completes  
6. Ensures duplicate webhooks do not cause duplicate processing  

---

## 🏗 Architecture Overview
    External Payment Provider
            ↓POST /v1/webhooks/transactions
    FastAPI Application
            | Validate & store transaction (PROCESSING)
            | Respond immediately (202 Accepted)
            ↓
    Background Task
            ↓(30s delay)
    PostgreSQL (Status Updated - PROCESSED)
            ↓
    Status Query Endpoint
            ↓
           END




The webhook acknowledgment is intentionally decoupled from processing logic to
avoid timeouts, retries, and duplicate events.

---

## 🧩 Core Components

### 🔹 Webhook API
Receives transaction events and responds immediately with `202 Accepted`.

### 🔹 Service Layer
Encapsulates business logic such as idempotency checks, transaction creation,
and status updates.

### 🔹 Background Processor
Handles delayed transaction processing without blocking the request lifecycle.

### 🔹 Database Layer
Persists transaction state and enforces idempotency using a unique
`transaction_id`.

### 🔹 Status API
Allows querying the current state of a transaction for verification.

---

## ⚙️ Tech Stack

- Python 3.12  
- FastAPI  
- SQLAlchemy (2.0)  
- PostgreSQL  
- FastAPI BackgroundTasks  
- Uvicorn  

---

## 🧠 Technical Decisions

- **FastAPI** was chosen for its high performance and async-first design.
- **PostgreSQL** is used for persistent storage and strong consistency.
- **Database-level idempotency** is enforced via a unique constraint on
  `transaction_id`.
- **Background processing** ensures webhook responses remain fast.
- **Request-scoped database sessions** prevent connection leaks.
- **Lifespan-based startup handling** is used for clean application lifecycle
  management.

---

## 🛠 How to Run Locally

### 1️⃣ Clone Repository and Add .env:
    git clone <your-github-repo-url>
    cd <repo>
    In .env add the following:
    DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/transactions_db


### 2️⃣ Create Virtual Environment:
    python -m venv venv
    
    # macOS / Linux
    source venv/bin/activate
    
    # Windows
    venv\Scripts\activate


### 3️⃣ Install Dependencies:
    pip install -r requirements.txt


### 4️⃣ Run FastAPI Server:
    uvicorn app.main:app 


## 🎯 Key Guarantees

- Single Transaction: Send one webhook → verify it's processed after ~30 seconds\
- Duplicate Prevention: Send the same webhook multiple times → verify only one transaction is processed\
- Performance: Webhook endpoint responds quickly even under processing load\
- Reliability: Service handles errors gracefully and doesn't lose transactions


## 👤 Author

**Sweety Sharma**

  
    

