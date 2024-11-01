# Analysis of Linear Regression

## Table of Contents
- [Introduction](#introduction)
- [Example Applications of Linear Regression](#example-applications-of-linear-regression)
- [Objective](#objective)
- [Assumptions of Linear Regression](#assumptions)
- [Key Terms](#key-terms)
  - [Centroid](#1-centroid)
  - [Observed Value](#2-observed-value)
  - [Residuals](#3-residuals)
  - [Error](#4-error)
  - [Sum of Squared Errors (SSE)](#5-sum-of-squared-errors-sse)
  - [Total Sum of Squares (SST)](#6-total-sum-of-squares-sst)
  - [Mean Squared Error (MSE)](#7-mean-squared-error-mse)
  - [Correlation](#8-correlation)
  - [Coefficient of Determination](#9-coefficient-of-determination)
  - [Adjusted R2](#10-adjusted-r2)
  - [Standard Error (SE)](#11-standard-error)
- [Hypothesis Testing on Linear Regression](#hypothesis-testing)

## Introduction
Linear regression is a technique in regression analysis used to model the relationship between a dependent variable and one or more independent variables. It fits a linear equation to observed data, assuming a linear relationship between variables.

## Example Applications of Linear Regression
- Analyzing trends and sales forecasts
- Salary prediction
- Real estate price prediction
- Traffic ETA estimation

## Assumptions of Linear Regression
1. Linear relationship: The relationship between the independent and dependent variable are assumed to be linear
2. Independence: If there are more than two independent variables each of the variable must be independent(No autocorrelation).
3. Homoscedasticity: The residuals have constant variance at every point in the
linear model.
4. Multivariate Normality: The residuals of the model are normally distributed. 

**NB** Basic linear regression model consist of dependent and independent variables
with assumptions error terms are normally distributed, mean zero and constant
variance.

## Objective
The goal of linear regression is to find the best-fit line that minimizes the sum of squared residuals (SSE).
- The line is expressed as:
- *ŷ = b₀ + b₁x + ε*

Where:
- **ŷ** is the predicted value of **y**,
- **b₀** is the y-intercept,
- **b₁** is the slope,
- **ε** is the error term.

## Key Terms
To better understand linear regression, let's use the sample dataset:

| Independent (x) | Actual (y) |
|-----------------|------------|
| 1               | 4          |
| 2               | 2          |
| 3               | 5          |
| 4               | 7          |
| 5               | 3          |

### 1. Centroid
- The centroid is the mean of the x-values divided by mea of y-values.
- The best-fit line must pass through this point.

- [ sum(x)]/5 = 1 + 2 + 3 + 4 + 5 = 15/5
- [ sum(y)]/5 = 4 + 2 + 5 + 7 + 3 = 21/5

Thus, the centroid for this dataset is **(3, 4.2)**.

### 2. Observed Value
- Calculated using the regression equation:

*ŷ = b₀ + b₁x + ε*

For our dataset:

```
Sum of 𝑥𝑦 = (1 * 4) + (2 * 2) + (3 * 5) + (4 * 7) + (5 * 3) = 4 + 4 + 15 + 28 + 15 = 66
Sum of 𝑥^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 1 + 4 + 9 + 16 + 25 = 55
Slope (𝑏_1) = (5 * 66 - 15 * 21) / (5 * 55 - 15^2) = (330 - 315) / (275 - 225) = 15 / 50 = 0.3
Y-intercept (𝑏_0) = (21 - 0.3 * 15) / 5 = (21 - 4.5) / 5 = 16.5 / 5 = 3.3
y_hat= 3.3 + 0.3 * x
```

- Y-intercept:  
  ![intercept](Assets/image-1.png)
- Slope:  
  ![slope](Assets/image.png)

| Independent (x) | Actual (y) | Predicted (ŷ )           |
|-----------------|------------|--------------------------|
| 1               | 4          | 3.6                      |
| 2               | 2          | 3.9                      |
| 3               | 5          | 4.2                      |
| 4               | 7          | 4.5                      |
| 5               | 3          | 4.8                      |

### 3. Residuals
- The difference between the observed value (y) and the predicted value (ŷ).
- \[
ε = y - ŷ 
\]

### 4. Error
- The residuals represent the error, the difference between observed values and predicted values.

### 5. Sum of Squared Errors (SSE)
- A measure of the difference between observed and predicted values:
- Calculated by summing the squared differences between each observed value and its corresponding predicted value.

```
SSE = Σ ε^2
SSE = (0.4)^2 + (-1.9)^2 + (0.8)^2 + (2.5)^2 + (-1.8)^2
SSE = 0.16 + 3.61 + 0.64 + 6.25 + 3.24
SSE = 13.9
```

### 6. Total Sum of Squares (SST)
- Measures the total variation in the dependent variable from the mean:
```
y_bar = 21 / 5 = 4.2
SST = Σ (y_i - y_bar)^2
SST = (4 - 4.2)^2 + (2 - 4.2)^2 + (5 - 4.2)^2 + (7 - 4.2)^2 + (3 - 4.2)^2
SST = (-0.2)^2 + (-2.2)^2 + (0.8)^2 + (2.8)^2 + (-1.2)^2
SST = 0.04 + 4.84 + 0.64 + 7.84 + 1.44
SST = 14.8
```

### 7. Mean Squared Error (MSE)
- Calculates the average of the squares of the errors, or differences, between actual and predicted values in a regression problem.
- A lower MSE indicates that the model's predictions are closer to the actual values, implying better performance.

- MSE = SSE / n = 
- 13.9 / 5 = 2.78

![Mean Squared Error](Assets/MSE.png)


### 8. Correlation
- Measures the strength and direction of a linear relationship between two variables.
- Ranges from -1 to +1.  
- Positive Correlation: Both variables increase or decrease together.
- Negative Correlation: One variable increases while the other decreases.
- A correlation coefficient closer to 0 indicates there is no correlation.
- A correlation coefficient closer to 1 indicates a strong positive correlation,
meaning when one variable increases, the other proportionally increases. 
- If it is closer to –1 then it indicates a strong negative correlation, which means
as one variable increases the other proportionally decreases.
  ![Correlation](Assets/correlation.png)

### 9. Coefficient of Determination (R²)
- The square of the correlation coefficient. Represents the proportion of variance in the dependent variable explained by the independent variable. 
- It indicates the strength of the relationship between the two variables by showing how much change in y is explained by the independent variable
- R² has a limitation. Its value gets inflated or stay the same as more predictors are added even if the added predictors are insignificant.
- Reason for inflation of R² is that R² measures the proportion of the variance in the dependent variable explained by the independent variables, but it does not penalize for the number of predictors added to the model. 

  ![R²]Assets/(r_squared.png)

### 10. Adjusted R²
- Adjusted R-squared is a modified version of R-squared that accounts for predictors that are not significant in a regression model. 
- It is ussually used in multiple regression
- It penalizes the addition of predictors that do not improve the model significantly
- A higher adjusted R²  indicates a better-fitting model that accounts for the number of predictors.
- Addition of predictors(x) in the model can affects adjusted R2. Decreases adjusted R2 indicates addition of irrelevant predicors while its increment is the vice versa.

 ![Ajusted r2](Assets/adjusted_r2.png)

### 11. Standard Error (SE)
- Measures the accuracy of the regression model's predictions. The smaller the SE, the more accurate the predictions.  

 ![Standard Error](Assets/Se.png)

## Hypothesis Testing on Linear Regression
- Hypothesis testing in linear regression is used to test the significance of the slope(x-vars).
- Normally a two tailed test is conducted with the hypothesis.
- The regression line would be y=β0+β1+ε
- Our hypotheses are: 
  - H0:β1=0 (there is not a linear relationship between  x and y)
  - H1:β1≠0 (here is a significant linear relationship between x and y)
  - For multiple linear regression atleast one of the βi≠0
- The hypothesis can be perform by either t-test or F-test considering y being normally distributed

- After identifying the null and alternative hypothesis. Calcualate the test statistic using below formula
 ![t.test](Assets/t-statistic.png)

- Finally, compare this t-statistic with a critical value from the t-distribution table or use a p-value to assess significance. Make decision then conclude your hypothesis