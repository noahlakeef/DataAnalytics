#multiple linear regression
import pandas as pd
import seaborn as sns

df = pd.read_csv(r'C:\DataAnalytics\DataAnalytics\DescriptiveAnalytics\data.csv')

import matplotlib.pyplot as plt

independent_var = ['UNRATE', 'NASDAQ', 'MORTGAGE30US', 'GDP', 'FEDFUNDS', 'DEBT', 'CPI']
for var in independent_var:
    plt.figure()
    # Regression Plot also by default includes
    # best-fitting regression line
    # which can be turned off via `fit_reg=False`
    sns.regplot(x=var, y='S&P500', data=df).set(title=f'Regression plot of {var} and S&P500')

#plt.show()

#dependent variable
y = df['S&P500']
#independent variable
x = df[['UNRATE', 'NASDAQ', 'MORTGAGE30US', 'GDP', 'FEDFUNDS', 'DEBT', 'CPI']]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y,test_size=0.2 ,random_state=42)

#Training a Linear Regression Model
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()

# fit the model to the training data (learn the coefficients)
linreg.fit(X_train, y_train)

# intercept and coeffecients
print(linreg.intercept_) 
print (linreg.coef_)

#defining coef. parameters
coeff_parameter = pd.DataFrame(linreg.coef_,x.columns,columns=['Coefficient'])
print(coeff_parameter)

#######################################################################################
#prediction
y_pred = linreg.predict(X_test)

#######################################################################################
import matplotlib.pyplot as plt
df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})

plt.scatter(y_test.squeeze(), y_pred.squeeze())
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')

plt.show()

#########################################################################################
#Evaluating the Model
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score
mae = mean_absolute_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

r = r2_score(y_test, y_pred)
print(f'r2: {r:.2f}')
print(f'Mean absolute percentage error: {mape:.2f}')
print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')