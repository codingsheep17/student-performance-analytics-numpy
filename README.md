# 🎓 Student Performance Analytics Tool (NumPy + Matplotlib)

A data analytics project built with **NumPy** (no Pandas!) and **Matplotlib** to analyze and visualize student performance data.  
This project simulates a real-world analytics pipeline: from raw CSV → calculations → reporting → visualization.

---

## 🔧 Features

- 📊 **Basic Statistics**: Mean, median, min, max, std for Math, Reading, Writing  
- 🏆 **Top Students**: Top 5/10 performers per subject & overall leaderboard  
- ✅ **Per-Student Report**: Total score, average score, pass/fail classification  
- 📂 **CSV Export**: Generates clean summary file with derived columns  
- 📈 **Visualizations**:
  - Bar chart → Subject averages  
  - Histogram → Score distribution  
  - Pie chart → Pass vs Fail ratio  
  - Scatter plot → Correlation between subjects  
  - Leaderboard → Top 10 students’ total scores  
  - Boxplot → Score spread across subjects  

---

## 📂 Project Structure

student-performance-analytics-numpy/
│── students.csv # Dataset (1000+ records)
│── bruh.py # Main CLI script
│── student_summary.csv # Generated summary file
│── charts/ # Saved plots (PNG)
│ ├── bar_chart.png
│ ├── histogram.png
│ ├── pass_fail_pie.png
│ ├── scatter_plot.png
│ ├── leaderboard.png
│ └── boxplot.png
└── README.md

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/student-performance-analytics-numpy.git
   cd student-performance-analytics-numpy
Install dependencies:

pip install numpy matplotlib
Run the tool:


python bruh.py
📊 Example Outputs
CLI Output

===== Basic Statistics =====
Subject   Mean   Median   Min   Max   Std
Math      66.09  67.00    38    90    14.55
Reading   73.22  74.00    43    95    12.34
Writing   71.33  72.00    39    93    13.12


📊 Subject Averages (Top 5 Students)

📌 Key Learnings
Practiced NumPy array slicing, indexing, and vectorized calculations
Created a data pipeline without Pandas
Applied Matplotlib for insights-driven visualizations
Built a resume-worthy project from raw dataset → insights

🏷️ Tech Stack
Python 3
NumPy
Matplotlib

🤝 Contributing
Pull requests are welcome! Feel free to fork this repo and add new visualizations or metrics.

