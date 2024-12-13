
---

# **CPI Forecasting with ARIMA Models**

## **Abstract**
This project forecasts the Consumer Price Index (CPI)—a key indicator of inflation—using historical time-series data. ARIMA models are employed to analyze short-term and long-term trends, demonstrating how external shocks like the COVID-19 recession affect CPI volatility. The study emphasizes the importance of accurate inflation forecasting for economic policy and decision-making.

---

## **Project Structure**

```
CPI_ARIMA_Forecasting/
│
├── data/                 # Contains raw and processed datasets
│   ├── raw_data.csv       # Raw CPI data downloaded from FRED
│   ├── processed_data.csv # Cleaned data ready for analysis
│
├── notebooks/            # Jupyter notebooks for the analysis
│   ├── arima_forecast.ipynb      # Main notebook for ARIMA modeling
│   ├── covid_backtesting.ipynb   # Notebook analyzing pre-COVID trends
│
├── src/                  # Python scripts for reusable components
│   ├── arima_analysis.py         # Functions for ARIMA modeling
│   ├── data_preprocessing.py     # Functions for data cleaning
│
├── results/              # Results of the analysis
│   ├── forecasts.csv            # Forecasted CPI values
│   ├── figures/                 # Plots from the analysis
│       ├── cpi_trend.png
│       ├── forecast_plot.png
│
├── README.md             # Project overview (this file)
├── requirements.txt      # List of Python dependencies
└── .gitignore            # Files to exclude from version control
```

---

## **Objectives**
1. Forecast CPI trends using ARIMA models.
2. Compare pre-COVID inflation trends to post-pandemic volatility.
3. Provide insights for policymakers to manage inflation effectively.

---

## **Methodology**
1. **Data Collection**:
   - CPI data was sourced from [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/) using the `fredapi` library.
   - Dataset spans from January 1960 to the present.

2. **Model Selection**:
   - Auto-ARIMA was used to select optimal ARIMA configurations.
   - Two models were identified:
     - **ARIMA (0,2,3)**: Captures short-term volatility, including the COVID-19 recession.
     - **ARIMA (2,2,1)**: Highlights long-term inflation trends in a stable economic environment.

3. **Backtesting**:
   - Pre-COVID data (1960–2019) was used to assess how well the model predicts inflation trends during the pandemic.

---

## **Results**
1. **Model Performance**:
   - **ARIMA (0,2,3)** achieved the lowest AIC (786.305) and effectively captured CPI fluctuations during volatile periods.
   - **ARIMA (2,2,1)** provided a smoother fit for pre-pandemic data.

2. **Forecasting**:
   - Projected CPI values for the next 12 months show a steady upward trend, with forecasts ranging from 316.29 to 325.57.

3. **Visualizations**:
   - **CPI Trends Over Time**:
     ![CPI Trend](results/figures/cpi_trend.png)
   - **Forecasted CPI**:
     ![Forecast Plot](results/figures/forecast_plot.png)

---

## **How to Run the Project**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/CPI_ARIMA_Forecasting.git
   cd CPI_ARIMA_Forecasting
   ```

2. **Install Dependencies**:
   Use the `requirements.txt` file to install necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Notebooks**:
   - Open `notebooks/arima_forecast.ipynb` to reproduce ARIMA modeling.
   - Open `notebooks/covid_backtesting.ipynb` for pre-COVID analysis.

---

## **Dependencies**
This project requires the following Python libraries:
- `pandas`
- `numpy`
- `matplotlib`
- `statsmodels`
- `pmdarima`
- `fredapi`

To install:
```bash
pip install -r requirements.txt
```

---

## **Limitations and Future Work**
1. **Univariate Model**:
   - ARIMA does not incorporate external variables (e.g., interest rates or commodity prices).
   - Future work could explore multivariate models like VAR or SARIMAX.

2. **Residual Analysis**:
   - Heteroskedasticity in residuals indicates potential improvements by integrating ARIMA-GARCH models to address variance.

3. **Hybrid Models**:
   - Exploring hybrid approaches combining machine learning and statistical models may enhance forecasting accuracy.

---

## **Credits**
- CPI Data: [FRED](https://fred.stlouisfed.org/)
- ARIMA Implementation: Python's `statsmodels` and `pmdarima` libraries.

---

