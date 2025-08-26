
# 📊 E-commerce Sales Insights


[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)](https://www.python.org/)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nivedya2000-superstore-sales-analysis.streamlit.app/)




An interactive **Sales Analysis Dashboard** built with **Python, Pandas, Plotly, Seaborn, and Streamlit**.
This project provides insights into **sales performance, profit trends, discount impact, and customer behavior** using the **Superstore dataset**.

---

## 📂 Project Structure

```text
superstore-sales-analysis/
│── data/                   # Dataset (Superstore CSV file)
│── plots/                  # Saved plots from EDA
│── reports/                # Generated reports and summaries
│── scripts/                # Python utility scripts (cleaning, EDA)
│   │── data_cleaning.py
│   │── EDA_visualization.py
│── app.py                  # Streamlit dashboard application
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
```

---

## 📑 Dataset

The **Superstore dataset** is a sample retail dataset widely used in data analytics.
It includes transactional data such as:

* Order Date, Ship Date
* Customer Information (ID, Name, Segment, Region)
* Product Details (Category, Sub-Category, Product Name)
* Sales, Quantity, Discount, Profit

This dataset enables **business intelligence-style analysis** to explore profitability, discounts, and customer segments.

---

## ⚙️ Installation & Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/Nivedya2000/superstore-sales-analysis.git
   cd superstore-sales-analysis
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate    # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit dashboard:

   ```bash
   streamlit run app.py
   ```

---

## 🚀 Deploy on Streamlit Cloud

Easily deploy the dashboard online with **Streamlit Community Cloud**.

[![Deploy Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/Nivedya2000/superstore-sales-analysis/main/app.py)

---

## 📊 Features & Insights

✔️ **Data Cleaning & Preprocessing**

* Handling missing values
* Removing duplicates
* Standardizing column formats

✔️ **Exploratory Data Analysis (EDA)**

* **Summary Statistics**: Shape, missing values, descriptive stats
* **Correlation Heatmap**: Relationships between numerical variables
* **Trend Analysis**: Monthly sales vs. profit
* **Category & Region Insights**: Which categories and regions drive sales/profit

✔️ **Interactive Dashboard**

* **Filters**: Segment, Region, Category
* **Charts**: Sales trends, profit distribution, discount vs. profit scatter plots
* **Top Products**: Identify best-selling and most profitable products

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Pandas, NumPy** → Data wrangling & preprocessing
* **Matplotlib, Seaborn, Plotly** → Visualization & analytics
* **Streamlit** → Interactive dashboard
* **VS Code / Jupyter Notebook** → Development environment

---


## 📌 Workflow

1. **Data Import & Cleaning** → Scripts in `scripts/data_cleaning.py`
2. **Exploratory Data Analysis** → Visuals from `EDA_visualization.py`
3. **Dashboard Development** → `app.py` with Streamlit
4. **Deployment** → Streamlit Cloud for sharing insights

---

## 🔮 Future Improvements

* Add predictive modeling (sales forecasting using ML)
* Include customer segmentation (RFM analysis, clustering)
* Automated report generation (PDF/Excel outputs)
* CI/CD pipeline for continuous deployment

---

## 📝 License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

---

## 👩‍💻 Author

**Nivedya K**
🌐 [LinkedIn](https://www.linkedin.com/in/nivedya-k) | [GitHub](https://github.com/Nivedya2000)


