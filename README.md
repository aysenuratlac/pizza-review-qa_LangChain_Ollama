# 🍕 Pizza Restaurant Review Q\&A System

This project builds a system that answers **natural language questions** about a pizza restaurant based on customer reviews.
It uses LangChain, Ollama, and Chroma to store reviews in a vector database and retrieve the most relevant ones to generate answers with a language model.

---

## 📌 Features

* **Load data from CSV**: Realistic restaurant reviews are loaded from a CSV file.
* **Vector database**: Persistent storage using Chroma (`persist_directory`).
* **Embedding**: Texts are transformed into numerical vectors using `OllamaEmbeddings`.
* **Retriever**: Retrieves the top relevant reviews (`k=5`).
* **Q\&A**: Answers are generated with `OllamaLLM` (llama3.2).
* **Interactive CLI**: Continuously accepts user questions.

---

## 🛠 Requirements

* **Python 3.9+**
* Ollama (local LLM server)
* Internet connection (to download models)
* Python packages:

  * `langchain`
  * `langchain-ollama`
  * `langchain-chroma`
  * `pandas`

Install dependencies using `requirements.txt`.

---

## 📥 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/username/pizza-review-qa.git
   cd pizza-review-qa
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source ./venv/bin/activate   # Mac/Linux
   venv\Scripts\activate        # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install and run Ollama**

   * Download from [Ollama official site](https://ollama.ai)
   * Start Ollama in the terminal:

     ```bash
     ollama serve
     ```

5. **Pull required models (mxbai-embed-large and llama3.2)**

   ```bash
   ollama pull mxbai-embed-large
   ollama pull llama3.2
   ```

---

## ▶️ Usage

1. **Run the main script**

   ```bash
   python main.py
   ```

2. **Ask a question**

   ```
   -------------------------------
   Ask your question (q to quit): What do people say about the pizza quality?
   ```

3. **Exit**

   ```
   q
   ```

---

## 📂 Project Structure

```
.
├── chrome_langchain_db     # DB
├── main.py                 # Main Q&A application
├── vector.py               # Vector DB creation and retriever
├── realistic_restaurant_reviews.csv  # Example review data
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## 🧠 How It Works

1. **Load Data** → Read reviews from CSV.
2. **Embedding** → Convert texts to vectors using `OllamaEmbeddings`.
3. **Vector Database** → Store them persistently in Chroma.
4. **Retriever** → Get the most relevant reviews for a question.
5. **LLM** → Generate an answer using `OllamaLLM` based on retrieved reviews.

---

## 💡 Notes

* The first run will take longer due to embedding generation.
* Once the database is created, embeddings are reused for faster queries.
* You can replace `realistic_restaurant_reviews.csv` with your own dataset.
