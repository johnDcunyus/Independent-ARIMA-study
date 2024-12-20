# -*- coding: utf-8 -*-
"""IndependentFinalStudy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v9bah_5Subvnjs07yQbW345OHMYANCc8

# **Abstract**

This analysis forecasts future Consumer Price Index (CPI) values—a critical indicator of inflation—using historical time-series data. The study applies the ARIMA model, recognized for its effectiveness in identifying patterns in economic indicators. Two configurations are utilized: ARIMA (0,2,3) for capturing short-term volatility and ARIMA (2,2,1) for long-term trends. Both configurations were selected through automated processes provided by the pmdarima library. Spanning data from January 1960 to January 2020 for validation, the study demonstrates ARIMA's utility in predicting CPI trends and informing economic policy, particularly during economic disruptions like the COVID-19 recession.



# **Introduction**
Inflation, as measured by the Consumer Price Index (CPI), plays a pivotal role in economic planning and analysis. It reflects changes in the cost of goods and services over time, influencing decisions related to monetary policy, wage adjustments, and purchasing power. Policymakers, businesses, and households rely on CPI forecasts to make informed financial decisions. Without effective forecasting, economies risk instability, as unchecked inflation can erode purchasing power and deepen inequality, while deflation suppresses production and employment. Both scenarios are detrimental to the economy and can affect other factors, such as the employment rate or the value of the dollar. To combat rising inflation, the Federal Reserve employs several tools to assess and address its trajectory.

Various forecasting tools have proven instrumental in addressing this need. Forecasting models have been used extensively to analyze and predict the direction of time-series data. The ARIMA model used in this analysis enables the modeling of time-series data by incorporating past data patterns, applying differencing to remove trends, and accounting for random noise. Its parameters—p, d, and q— determine how well the model adapts to specific datasets, making it suitable for complex economic contexts. ARIMA's reliance on time-series data makes it a viable option for utilizing records from the Federal Reserve.

By leveraging ARIMA to forecast U.S. CPI trends, this study demonstrates the model’s ability to anticipate inflationary pressures and provide actionable insights for economic stabilization.



## International Examples of CPI detriments:

The global significance of accurate inflation forecasting is evident in past economic crises. In Peru during the 1970s, inflation averaged 25% annually, but by the early 1990s, it had spiraled beyond 300%, leading to economic collapse. Reforms such as eliminating wage indexation and adopting a market-driven exchange rate eventually stabilized inflation at under 4% by 1999, but at a steep cost to the nation [Mohanty & Klau, 2001].

Conversely, Venezuela’s hyperinflation offers a stark reminder of the consequences of inaction. Poor fiscal management and resource misallocation devastated the Bolivar and plunged millions into poverty. Meanwhile, Japan’s struggle with deflation during the 1997–1998 banking crisis highlights the risks of stagnation in a low-price environment [Ito & Mishkin, 2004]. These cases underscore the critical need for accurate forecasting tools to prevent economic crises before they escalate. One such tool, renowned for its role in assessing inflation trends, is the Phillips Curve—a cornerstone of macroeconomics. Its development, along with advancements in other forecasting metrics, has significantly simplified the process of evaluating the trajectory of inflation within a country.

## **Importance of CPI Forecasting**
CPI forecasting benefits governments, businesses, and households alike. Policymakers use it to anticipate inflationary or deflationary trends, enabling timely adjustments in interest rates, fiscal measures, and public spending. Businesses rely on CPI trends to refine pricing strategies, optimize supply chains, and plan for the long term. Similarly, households benefit from forecasts by using them for budgeting and financial planning. Its value is especially significant when considering the cost of our livelihoods.

Failing to address inflation carries severe consequences. Rising inflation erodes purchasing power and destabilizes financial markets, while prolonged deflation stifles investment and employment. Learning from past mistakes and instances of poor monetary decisions, forecasting models have become essential tools for broader financial institutions, such as the United States Federal Reserve. These models help predict the direction of inflation, enabling policymakers to make informed decisions that benefit the economy. Without such tools, multiple economic catastrophes could arise, further increasing the cost of everyday living. Models like ARIMA allow analysts to identify inflationary pressures early, enabling proactive measures to sustain growth and stabilize economies.

## Background of Time-Series Data and ARIMA
Time-series data is a vital resource for professionals across disciplines, including statisticians, economists, and data scientists. Unlike datasets that rely on random sampling, time-series data is sequentially ordered, with observations recorded chronologically. This temporal structure allows analysts to uncover unique features such as serial correlation, trends, seasonality, and patterns, which are essential for understanding and predicting future behavior. By identifying these elements, time-series analysis provides a clearer perspective on underlying dynamics. Techniques like differencing are often applied to remove non-stationarity—unpredictable trends that obscure meaningful patterns—ensuring a stable and reliable analytical foundation.

Time-series analysis has become indispensable in fields such as financial forecasting, healthcare analytics, and crime analytics, where accurate predictions significantly influence decision-making and outcomes.

## ARIMA: A Key Model for Time-Series Forecasting

One of the most commonly used methods for time-series forecasting is the AutoRegressive Integrated Moving Average (ARIMA) model, developed by George Box and Gwilym Jenkins. Known widely as the Box-Jenkins model, ARIMA has become a critical tool in economic forecasting, supporting businesses in analyzing financial data and predicting stock price movements. Beyond economics, ARIMA has been applied in public health to monitor disease outbreaks and evaluate population health disturbances. Its versatility extends to fields such as crime analytics, computer programming, and beyond [Islam, 2020].

ARIMA consists of three core components:

* AR (AutoRegressive): Captures relationships between a current value and its past observations, represented by the parameter p.

* I (Integrated): Accounts for the degree of differencing (d) required to make the data stationary.

* MA (Moving Average): Reflects how past forecast errors (q) influence current values.

This combination enables ARIMA to model complex time-series data, providing robust insights into future trends.

# **Modeling**

This study utilizes the Auto-Regressive Integrated Moving Average (ARIMA) model to forecast the Consumer Price Index (CPI) based on historical data. Before discussing ARIMA in detail, it is important to understand its simpler predecessor, the Autoregressive Moving Average (ARMA) model, which forms the foundation of ARIMA modeling.

### **The ARMA Model $(p, q)$**

The ARMA model is designed for stationary time-series data and combines two components: Autoregressive (AR) and Moving Average (MA). Represented as $ ARMA(p, q)$ , the structure accounts for dependencies between data points and random errors.

- **Autoregressive (AR) Component**: The AR component models the current value $(x_t)$ as a function of $(p)$ lagged observations:

  $
  x_t = c + \phi_1 x_{t-1} + \phi_2 x_{t-2} + \cdots + \phi_p x_{t-p} + w_t
  $

  Here, $(c)$ is a constant, $(\phi)$ are the coefficients of past observations, and $(w_t)$ represents white noise.

- **Moving Average (MA) Component**: The MA component models the current value $(x_t)$ as a function of past $(q)$ error terms:

  $
  x_t = c + w_t + \theta_1 w_{t-1} + \theta_2 w_{t-2} + \cdots + \theta_q w_{t-q}
  $

  where $(\theta)$ are coefficients of past errors.

Combining these two components, the ARMA model effectively predicts stationary series by using past observations and their associated errors to estimate the present value of the data. *(nyoni2019arima)*

---

### **The ARIMA Model $(p, d, q)$**

Many economic time series, including CPI, are non-stationary, meaning they exhibit trends or seasonality over time. ARIMA extends ARMA by incorporating differencing to make the data stationary. The resulting model is expressed as $ARIMA(p, d, q)$, where:

- $(p)$: The number of lagged observations in the AR component,
- $(d)$: The degree of differencing to achieve stationarity,
- $(q)$: The number of lagged error terms in the MA component.

The integration (I) component, represented by $(d)$, involves transforming the data through differencing:

$
y_t = x_t - x_{t-1}
$


This process eliminates trends and makes the data suitable for ARMA modeling. The ARIMA model thus accounts for both stationary and non-stationary elements, making it well-suited for economic data analysis.

By combining AR, MA, and differencing components, the ARIMA model is represented mathematically as:

$
x_t = c + \phi_1 x_{t-1} + \cdots + \phi_p x_{t-p} + \theta_1 w_{t-1} + \cdots + \theta_q w_{t-q} + w_t
$

---

### **Implementation and Forecasting**

This study employs Auto-ARIMA from Python's `pmdarima` library to identify optimal parameter values for ARIMA. Auto-ARIMA iteratively tests configurations of $(p)$, $(d)$, and $(q)$, selecting the model that minimizes Akaike Information Criterion (AIC) and ensures accuracy while avoiding overfitting. This automated approach expedites the model selection process while maintaining the rigor of traditional Box-Jenkins methodology.

For this analysis:
- **ARIMA (0,2,3)** is chosen for its robust handling of short-term CPI volatility, as indicated by its lower AIC score.
- **ARIMA (2,2,1)** is selected for its ability to capture long-term inflation trends, particularly during periods of economic instability like the COVID-19 recession.

The selected models are validated through residual analysis and diagnostic tests, as described in the results section.
"""

!pip install pandas statsmodels fredapi matplotlib pmdarima  #Installing the ARIMA modelset

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from pmdarima import auto_arima
from google.colab import userdata
from fredapi import Fred

# Initialize FRED API with your API key
fred = Fred(api_key=userdata.get('FREDAPI'))

# Pull CPI data from FRED
cpi_data = fred.get_series('CPIAUCSL', observation_start='1960-01-01')

# Convert it to a DataFrame
cpi_data = pd.DataFrame(cpi_data, columns=['CPI'])
cpi_data.index = pd.to_datetime(cpi_data.index)

# Set frequency to 'MS' (month start) to avoid frequency inference warning
cpi_data = cpi_data.asfreq('MS')  # Set frequency to month start

# Visualize the CPI data
cpi_data.plot(title='CPI (Inflation) Over Time', figsize=(10, 6))
plt.show()

# Use auto-arima to determine the best (p, d, q) order
auto_model = auto_arima(
    cpi_data['CPI'],
    seasonal=False,  # Set to True if you suspect seasonality
    stepwise=True,
    trace=True,      # Prints progress and results of the search
    suppress_warnings=True,
    error_action="ignore",
    max_p=5, max_q=5, d=None  # Restrict search space for speed
)
print(auto_model.summary())

# Extract the optimal (p, d, q) order
optimal_order = auto_model.order

# Fit ARIMA model using the optimal order
optimal_arima_model = ARIMA(cpi_data['CPI'], order=optimal_order)
optimal_arima_fit = optimal_arima_model.fit()

# Print model summary
print(optimal_arima_fit.summary())

# Forecast the next year (12 months)
forecast_steps = 12
forecast = optimal_arima_fit.get_forecast(steps=forecast_steps)
forecast_mean = forecast.predicted_mean
forecast_ci = forecast.conf_int()

# Create forecast index
forecast_index = pd.date_range(start=cpi_data.index[-1] + pd.DateOffset(months=1), periods=forecast_steps, freq='MS')

# Create a DataFrame for forecast results
forecast_results = pd.DataFrame({
    'Forecasted CPI': forecast_mean,
    'Lower CI': forecast_ci.iloc[:, 0],
    'Upper CI': forecast_ci.iloc[:, 1]
}, index=forecast_index)

# Display the forecasted CPI results
print("Forecasted CPI for the Next Year:")
print(forecast_results)

# Plot the actual CPI data and forecasted values
plt.figure(figsize=(12, 6))
plt.plot(cpi_data.index, cpi_data['CPI'], label='Actual CPI', color='blue')
plt.plot(forecast_index, forecast_mean, label=f'Forecasted CPI (ARIMA {optimal_order})', color='red')
plt.fill_between(forecast_index, forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1], color='pink', alpha=0.3)
plt.title(f'CPI Forecast using Optimal ARIMA{optimal_order} Model (1-Year Forecast)')
plt.xlabel('Date')
plt.ylabel('CPI')
plt.legend()
plt.show()

"""## Covid-19 backtesting, seeing if the model can project the Data of the COVID-19 recession:"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima
from google.colab import userdata
from fredapi import Fred

# Initialize FRED API with your API key
fred = Fred(api_key=userdata.get('FREDAPI'))

# Pull CPI data from FRED
cpi_data = fred.get_series('CPIAUCSL', observation_start='1960-01-01')

# Convert it to a DataFrame
cpi_data = pd.DataFrame(cpi_data, columns=['CPI'])
cpi_data.index = pd.to_datetime(cpi_data.index)

# Set frequency to 'MS' (month start) to avoid frequency inference warning
cpi_data = cpi_data.asfreq('MS')  # Set frequency to month start

# Visualize the CPI data
cpi_data.plot(title='CPI (Inflation) Over Time', figsize=(10, 6))
plt.show()

# Train ARIMA model on data up to December 2019
training_data = cpi_data[:'2019-12-01']

# Use auto-arima to determine the best (p, d, q) order
auto_model = auto_arima(
    training_data['CPI'],
    seasonal=False,  # Set to True if seasonality is suspected
    stepwise=True,
    trace=True,      # Displays the search process
    suppress_warnings=True,
    error_action="ignore"
)
print("Selected ARIMA Order:", auto_model.order)

# Fit ARIMA model using the optimal order from auto-arima
optimal_order = auto_model.order
arima_model = ARIMA(training_data['CPI'], order=optimal_order)
arima_fit = arima_model.fit()

# Forecast from January 2020 onward
forecast_start_date = '2020-01-01'
forecast_steps = len(cpi_data[forecast_start_date:])  # Number of months to forecast
forecast = arima_fit.get_forecast(steps=forecast_steps)

# Extract forecast results
forecast_mean = forecast.predicted_mean
forecast_ci = forecast.conf_int()

# Create forecast index (January 2020 onward)
forecast_index = cpi_data[forecast_start_date:].index

# Create a DataFrame for forecast results
forecast_results = pd.DataFrame({
    'Forecasted CPI': forecast_mean,
    'Lower CI': forecast_ci.iloc[:, 0],
    'Upper CI': forecast_ci.iloc[:, 1]
}, index=forecast_index)

# Plot the actual CPI and forecast results with confidence intervals
plt.figure(figsize=(12, 6))

# Plot Actual CPI
plt.plot(cpi_data.index, cpi_data['CPI'], label='Actual CPI (1960-Present)', color='blue')

# Plot Forecasted CPI and Confidence Intervals
plt.plot(forecast_results.index, forecast_results['Forecasted CPI'], label=f'Forecasted CPI (ARIMA {optimal_order}) From Jan 2020', color='red', linestyle='dashed')
plt.fill_between(
    forecast_results.index,
    forecast_results['Lower CI'],
    forecast_results['Upper CI'],
    color='pink',
    alpha=0.3,
    label='Forecast Confidence Interval'
)

# Add Title and Labels
plt.title(f'CPI Forecast (Jan 2020 Onward) Trained on Data from 1960-2019 (ARIMA {optimal_order})')
plt.xlabel('Date')
plt.ylabel('CPI')
plt.legend()
plt.grid()
plt.show()

"""---

# **Results and Findings of the Data**

### **Model Fit**

The ARIMA (0,2,3) model demonstrates strong performance, achieving the lowest AIC value (786.305) among tested configurations. This indicates it balances complexity with predictive accuracy effectively for the dataset. The model’s BIC score (804.922) and Hannan-Quinn Information Criterion (HQIC, 793.467) further validate its suitability for forecasting CPI.

---

### **Significance of Parameters**

The summary statistics for the ARIMA (0,2,3) model indicate all coefficients—$(ma.L1)$, $(ma.L2)$, and $(ma.L3)$—are statistically significant ($(p)$-values < 0.05). This demonstrates that the moving average terms significantly enhance the model’s forecasting capability. Small standard errors and high z-scores associated with these terms further underline their reliability in capturing patterns within the dataset.

---

### **Residual Analysis and Model Diagnostics**

- **Ljung-Box Test**: A $(p)$-value of 0.92 indicates no significant autocorrelation in the residuals, affirming that the model successfully captures the underlying patterns in CPI data. The residuals are uncorrelated and consistent with white noise, validating the model’s adequacy.
- **Jarque-Bera Test**: Residual analysis reveals non-normality ($(p < 0.001)$, skewness = -1.05, kurtosis = 14.19). These results suggest external shocks, such as the COVID-19 recession, introduce volatility not fully accounted for by the model.

---

### **Non-Normality and External Influences**

The heteroskedasticity observed in the residuals $(H = 25.65)$ reflects varying CPI volatility across periods. While this does not violate forecasting assumptions, it highlights periods of economic instability, such as the 2008 financial crisis and the COVID-19 recession, where external factors significantly impacted inflation.

---

### **Forecasting Accuracy**

- **Projection Reliability**: The model forecasts a steady upward trend in CPI, with confidence intervals ranging from 316.29 to 325.57 over one year. While promising, these predictions do not account for external factors like fiscal policy or commodity price shocks, which could affect long-term accuracy.
- **Backtesting Results**: The pre-COVID dataset (1960–2019) produced an ARIMA (2,2,1) model, reflecting stable inflation trends. In contrast, the full dataset (1960–present) exhibits greater volatility, attributed to external shocks such as the pandemic. These results underscore the importance of adaptive modeling in dynamic economic conditions.

---

### **Broader Context and Insights**

- **Dataset Size**: The extensive dataset (778 observations) provides a comprehensive view of long-term CPI trends but inflates AIC and other criteria. This is expected and does not detract from the model’s utility.
- **Economic Implications**: The model’s upward CPI forecast highlights persistent inflationary pressures. Policymakers must address these trends proactively, as seen in recent Federal Reserve actions targeting a 2% inflation rate.

### **Results and Findings of the Data**

#### **Model Fit**  
The ARIMA (0,2,3) model demonstrates strong performance, achieving the lowest AIC value (786.305) among all tested configurations. This indicates a well-balanced trade-off between complexity and predictive accuracy for the dataset. Furthermore, the model's BIC score (804.922) and Hannan-Quinn Information Criterion (HQIC, 793.467) further validate its suitability for forecasting CPI. Due to the size of the model, the forecasting metrics exhibit significantly large values, which can be attributed to the extensive sample size of the time-series data. The recorded instances of multiple volatility patterns and trends in the dataset represent decades of economic occurrences and shocks, spanning from the 1960s to the present day. This demonstrates a significant correlation between forecasting metrics and sample size.



#### **Significance of Parameters**  
Summary statistics for the ARIMA (0,2,3) model reveal that all coefficients—($ma.L1$), ($ma.L2$), and ($ma.L3$)—are statistically significant $((p)values < 0.05$). This confirms the importance of the moving average terms in enhancing the model's forecasting ability. The coefficients' small standard errors and high z-scores underline their reliability in capturing key patterns within the dataset. Patterns such as monetary decisions or policies are captured through the moving averages, which show more complex volatility within the base time series data. This could be from it's capture of the covid-19 recession which significantly spiked our inflation rate, which added more volatility within our time series data.  

#### **Residual Analysis and Model Diagnostics**  
- **Ljung-Box Test:** A (p)-value of 0.92 indicates no significant autocorrelation in the residuals, affirming the model's success in capturing underlying CPI patterns. The residuals are uncorrelated and consistent with white noise, validating the model's adequacy.  
- **Jarque-Bera Test:** The residual analysis identifies non-normality ($p<0.001$, skewness = -1.05, kurtosis = 14.19). This suggests that external shocks, such as the COVID-19 recession, introduced volatility not fully accounted for by the model.  

## **Non-Normality and External Influences**

Heteroskedasticity in the residuals $(H=25.65)$ reflects variations in CPI volatility across different periods. While this does not violate the core forecasting assumptions, it highlights moments of economic instability, such as the 2008 financial crisis and the COVID-19 recession. External factors significantly impact inflation, making it challenging for a univariate model like ARIMA to fully capture these dynamics.  

---

### **Forecasting Accuracy**

- **Projection Reliability:**  
  The ARIMA (0,2,3) model forecasts a steady upward trend in CPI, with confidence intervals ranging from 316.29 to 325.57 over the next year. While the results are promising, external factors such as fiscal policy changes or commodity price shocks are not considered, which could affect the long-term accuracy of these projections.  

- **Backtesting Results:**  
  When using pre-COVID data (1960–2019), the ARIMA (2,2,1) model demonstrated stable inflation trends and produced significantly lower AIC values compared to the full dataset analysis. This reflects smoother inflationary behavior in the absence of pandemic-driven disruptions. By contrast, the full dataset (1960–present) exhibits greater volatility, attributed primarily to shocks like the COVID-19 recession. These findings are important in regard to adaptive modeling in dynamic economic environments. Further improvement among the backtesting can be done in the form of different statistical approaches or hybrid modeling.
---

### **Broader Context and Insights**

1. **Dataset Size:**  
   The dataset's extensive range (778 observations) provides a comprehensive view of long-term CPI trends. However, it also inflates AIC and other evaluation criteria due to the higher complexity required to model diverse economic periods.  

2. **Economic Implications:**  
   The model's upward CPI forecast highlights persistent inflationary pressures. This suggests that policymakers must address these trends proactively, as demonstrated by recent Federal Reserve actions targeting a 2% inflation rate. The projected increase in inflation can be mitigated by raising the Federal Funds Rate. This is the Fed's primary tool for managing rapidly rising inflation. By increasing interest rates, the Fed can slow the rate of growth in the CPI, thereby stabilizing the economy.

---

### **Conclusion**  

This study demonstrates the effectiveness of ARIMA modeling for forecasting CPI trends using historical data. The ARIMA (0,2,3) configuration successfully captures short-term inflation volatility, while the ARIMA (2,2,1) model provides valuable insights into longer-term economic trends. These models prove particularly useful during periods of relative stability, but external shocks—such as the COVID-19 recession—pose significant challenges.  

Despite its strengths, the analysis reveals some limitations of ARIMA modeling. External shocks, such as economic recessions or unexpected Federal Reserve policy shifts, introduce volatility that the model cannot fully account for. The observed non-normality in residuals, as indicated by the Jarque-Bera test, further emphasizes the presence of outliers or structural breaks in the data. Additionally, the heteroskedasticity observed in the residuals highlights the need for models that can dynamically adapt to varying levels of volatility.  

---

### **Limitations and Potential Improvements**

1. **Univariate Focus:**  
   ARIMA models rely solely on a single dependent variable, as was the case in this analysis. This univariate approach omits critical factors such as interest rates, commodity prices, and fiscal policies, potentially leading to omitted variable bias. Incorporating these variables through a multivariate approach—such as Vector Autoregression (VAR)—could significantly enhance explanatory power and provide a more comprehensive analysis of inflationary trends.  

2. **Non-Normal Residuals and Long-Term Predictions:**  
   The non-normality in residuals suggests that the model does not fully capture all underlying patterns, an issue compounded by its univariate nature. Employing an ARIMA-GARCH model could address heteroskedasticity by accounting for variations in residual variance over time.  
   Regarding long-term predictions, the reliance on historical data limits accuracy. Exploring ensemble methods or incorporating stochastic trend components could improve model robustness and better account for long-term economic shifts.  

---

### **Final Thoughts**  

The ARIMA model provides valuable insights into CPI trends and proves to be a useful tool for economic forecasting and decision-making. However, addressing its limitations—particularly in handling external shocks and incorporating multivariate dynamics—could refine its application, especially in rapidly changing environments.  

Future work should explore hybrid forecasting models and multivariate approaches, such as VAR, to enhance model robustness and adaptability. Unlike ARIMA, which focuses on patterns within CPI data, VAR considers interdependencies between multiple variables, such as CPI and interest rates, potentially creating more accurate models.  

While this study serves as a foundational analysis, it also highlights areas for improvement and further research. The findings demonstrate the potential of using ARIMA for inflation trajectory analysis, offering a practical starting point for future advancements in economic forecasting.
"""

# Bibliography
!pip install bibtexparser

import bibtexparser
from bibtexparser.bwriter import BibTexWriter

bibtex_str = """
@article{dennis2006policy,
  title={The policy preferences of the US Federal Reserve},
  author={Dennis, Richard},
  journal={Journal of Applied Econometrics},
  volume={21},
  number={1},
  pages={55--77},
  year={2006},
  publisher={Wiley Online Library}
}
@article{islam2020forecasting,
  title={Forecasting crime using ARIMA model},
  author={Islam, Khawar and Raza, Akhter},
  journal={arXiv preprint arXiv:2003.08006},
  year={2020}
}
@article{kumar2010arima,
  title={ARIMA forecasting of ambient air pollutants (O 3, NO, NO 2 and CO)},
  author={Kumar, Ujjwal and Jain, VK},
  journal={Stochastic Environmental Research and Risk Assessment},
  volume={24},
  pages={751--760},
  year={2010},
  publisher={Springer}
}
@article{nyoni2019arima,
  title={ARIMA modeling and forecasting of Consumer Price Index (CPI) in Germany},
  author={Nyoni, Thabani},
  year={2019}
}
@article{ito2004two,
  title={Two decades of Japanese monetary policy and the deflation problem},
  author={Ito, Takatoshi and Mishkin, Frederic S},
  year={2004},
  publisher={National Bureau of Economic Research Cambridge, Mass., USA}
}
@article{mohanty2001determines,
  title={What determines inflation in emerging market economies?},
  author={Mohanty, MS and Klau, Marc and others},
  journal={BIS Papers},
  volume={8},
  pages={1--38},
  year={2001}
}
"""
bib_database = bibtexparser.loads(bibtex_str)
writer = BibTexWriter()
writer.indent = '  '
bibtex_formatted = writer.write(bib_database)
print(bibtex_formatted)