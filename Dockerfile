# 1. Ξεκινάμε με μια "ελαφριά" έκδοση της Python
FROM python:3.11-slim

# 2. Ορίζουμε πού θα δουλεύουμε μέσα στο κοντέινερ
WORKDIR /app

# 3. Αντιγράφουμε το αρχείο με τις βιβλιοθήκες
COPY requirements.txt .

# 4. Εγκαθιστούμε τις βιβλιοθήκες
RUN pip install --no-cache-dir -r requirements.txt

# 5. Αντιγράφουμε όλο τον κώδικα μέσα στο κοντέινερ
COPY . .

# 6. Ανοίγουμε την πόρτα 8000
EXPOSE 8000

# 7. Η εντολή για να ξεκινήσει το API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]