# 📊 CORD-19 Metadata Analysis & Streamlit App

This project analyzes the **CORD-19 research dataset (metadata.csv)** and presents findings in a simple **Streamlit app**.

## 🚀 Features
- Load and clean research paper metadata
- Analyze publications by year, journal, and source
- Generate word cloud of titles
- Interactive Streamlit dashboard

## 📂 Project Structure
- `data/metadata.csv` → dataset
- `notebooks/analysis.ipynb` → exploration & cleaning
- `app.py` → Streamlit app
- `requirements.txt` → dependencies

## 🛠️ Installation
```bash
git clone https://github.com/<your-username>/Frameworks_Assignment.git
cd Frameworks_Assignment
pip install -r requirements.txt
```
▶️ Run Streamlit App
```bash
Copy code
streamlit run app.py
```
📈 Insights
Research output spiked in 2020 due to COVID-19

Certain journals dominated early COVID publications

Common words in titles highlight pandemic-related themes

✍️ Reflection
This project improved my skills in:

Data wrangling with Pandas

Visualization with Matplotlib/Seaborn

Building interactive apps with Streamlit


---

## ✅ Next Steps
1. Put `metadata.csv` in `/data/`  
2. Save `analysis.ipynb` in `/notebooks/`  
3. Run `jupyter notebook` for exploration  
4. Run the app:  
   ```bash
   streamlit run app.py
