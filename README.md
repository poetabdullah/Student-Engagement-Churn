# Students Churn Data Analysis

## 📊 Project Overview
This project aims to analyze student engagement and predict churn (dropout) for the Excelerate AI Data Analyst Internship program. The analysis spans four weeks of data-driven exploration, cleaning, and modeling to identify factors contributing to student engagement and disengagement. By leveraging data science techniques, the project provides actionable insights to enhance student retention and engagement strategies.

## 🗂 Repository Structure
```plaintext
├── Week 1 - Data Cleaning and Validation
│   ├── AI_internship_Week1.csv
│   ├── Week 1 Code.ipynb
│   ├── Week 1 Report.pdf
├── Week 2 - Exploratory Data Analysis
│   ├── Week 2 Code.ipynb
│   ├── Week 2 Report.pdf
├── Week 3 - Churn Analysis and Predictive Modeling
│   ├── Week 3 Code Module 1.ipynb
│   ├── Week 3 Code Module 2.ipynb
│   ├── Week 3 Dataset.csv
│   ├── Week 3 Report.pdf
├── Week 4 - Recommendations & Presentation
│   ├── Evaluation.docx
│   ├── Team Presentation Slides.pptx
│   ├── Team Presentation Video.mp4
│   ├── Week 4 Code.py
└── README.md
```

## 👥 Team Members
- Abdullah Imran
- Matthew Ojo
- Krishin Tharani
- Emani Likhita
- Sangeeta Sahoo
- John Syllah
- Tracy Reson
- Afra Falakh
- Eluit Cruz

---

## 📈 Week 1: Data Cleaning and Feature Engineering
### Overview
In the first week, we focused on cleaning the raw dataset to ensure it was suitable for further analysis. Key tasks included handling missing values, removing duplicates, correcting formatting issues, and standardizing data types. Feature engineering techniques were also applied to extract meaningful insights from existing data columns.

### Key Steps
- **Data Cleaning**:
  - Addressed missing values using imputation techniques.
  - Removed unnecessary columns and standardized data types.
  - Validated entries for accuracy, including dates, numerical fields, and categorical data.
- **Feature Engineering**:
  - Created new features such as "Age of Learner," "Engagement Duration," and "Time Since Last Engagement."
  - Implemented one-hot encoding for categorical variables.
  - Normalized engagement-related metrics to prepare for modeling.

### Tools & Libraries
- Python (Pandas, NumPy, Matplotlib)
- Jupyter Notebook

**[Week 1 Report](./Week%201%20-%20Data%20Cleaning%20and%20Validation/Week%201%20Report.pdf)**

---

## 🔍 Week 2: Exploratory Data Analysis (EDA)
### Overview
In the second week, we conducted an in-depth Exploratory Data Analysis (EDA) to uncover patterns and insights within the cleaned dataset. This phase laid the foundation for hypothesis generation and feature selection for predictive modeling.

### Key Analyses
- **Demographic Insights**:
  - Analyzed learner demographics like age, gender, and engagement patterns.
  - Identified high engagement among specific age groups (18-28 years).
- **Temporal Trends**:
  - Seasonal analysis of engagement scores, sign-up trends, and engagement duration.
  - Observed peak engagement in specific months (e.g., July) and days (e.g., Thursday).
- **Advanced Visualizations**:
  - Generated correlation heatmaps, PCA plots, and clustering (K-Means) to identify underlying data structures.
  - Conducted cohort analysis to track engagement over time.

### Tools & Libraries
- Python (Seaborn, Matplotlib, Scikit-learn)

**[Week 2 Report](./Week%202%20-%20Exploratory%20Data%20Analysis/Week%202%20Report.pdf)**

---

## 📊 Week 3: Churn Analysis & Predictive Modeling
### Overview
The focus of week three was to develop a robust predictive model for identifying students at risk of churn. The analysis aimed to uncover factors contributing to student drop-offs and to build a model capable of predicting churn with high accuracy.

### Key Steps
- **Data Preparation**:
  - Created new engagement metrics and defined churn indicators based on engagement duration, frequency, and inactivity.
  - Labeled students as "churned" or "non-churned" based on thresholds derived from EDA insights.
- **Model Training**:
  - Trained multiple models: Logistic Regression, Decision Tree, Random Forest, SVM, and Artificial Neural Networks (ANN).
  - Achieved the best results with an ensemble Voting Classifier, yielding 98% accuracy.
- **Model Evaluation**:
  - Evaluated models using metrics such as Precision, Recall, F1 Score, and Confusion Matrix.
  - The ANN model demonstrated high predictive power for complex engagement patterns.

### Tools & Libraries
- Python (Scikit-learn, TensorFlow, Keras)
- Google Colab

**[Week 3 Report](./Week%203%20-%20Chrun%20Analysis%20and%20Predictive%20Modeling/Week%203%20Report.pdf)**

---

## 📝 Week 4: Recommendations & Presentation
### Key Insights & Recommendations
- **Engagement Boost**:
  - Target interventions for age groups with lower engagement.
  - Increase support for underperforming opportunity categories.
- **Churn Reduction**:
  - Implement re-engagement strategies for users inactive for over 126 days.
  - Promote diverse learning opportunities to increase participation.
- **Future Enhancements**:
  - Leverage advanced models like Recurrent Neural Networks (RNN) for time-series engagement data.

**Deliverables**:
- [Team Presentation Slides](./Week%204%20-%20Recommendations%20&%20Presentation/Team%20Presentation%20Slides.pptx)
- [Team Presentation Video](./Week%204%20-%20Recommendations%20&%20Presentation/Team%20Presentation%20Video.mp4)

---

## 📊 Key Findings
1. **Top Factors for Churn**:
   - Low Engagement Score
   - Extended inactivity (Days Since Last Engagement > 126 days)
   - Limited Opportunity Participation (< 2 opportunities)
2. **Demographic Trends**:
   - Highest engagement among learners aged 18-28.
   - Significant interest from users in India, Nigeria, and the United States.
3. **Actionable Insights**:
   - Focus outreach on peak sign-up months to maximize engagement.
   - Address gaps in opportunity completion rates to reduce churn.

---

## ⚙️ How to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/poetabdullah/Students-Churn-Data-Analysis.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd Students-Churn-Data-Analysis
   ```

3. **Run the Jupyter Notebooks**:
   - Open `Week 1 Code.ipynb` to explore data cleaning.
   - Open `Week 2 Code.ipynb` for EDA.
   - Open `Week 3 Code Module 1.ipynb` & `Module 2.ipynb` for Churn Analysis.

---

## 📌 Conclusion
This project successfully utilized data science techniques to analyze student engagement and predict churn within an educational platform. The insights derived can be used to optimize retention strategies and enhance user experience.

Feel free to explore the repository and provide your feedback!
