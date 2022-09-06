# Resources/ References
- [Wikipedia](https://en.wikipedia.org/wiki/Feature_scaling)

# What is feature scaling?

- Feature scaling/ Data Normalization is a method used to normalize the range of independent 
variables or features of data. 
- Example: 
    - Feature A originally ranges from 50000 to 300,000. 
    - After Scaling: Feature A ranges from 0 to 1
- In a ML Project Pipeline, Feature Scaling is generally performed during
 the data preprocessing step. 

# Why Feature Scaling?

- The range of all features should be normalized so that each feature 
contributes approximately proportionately to the Cost Function
- Gradient descent converges much faster with feature scaling than without it
- Apply feature scaling if regularization is used as part of the
 loss function (so that coefficients are penalized appropriately)

# How to deal with missing values: 5 Examples

### Lan
- Get rid of all the rows with missing values
``` Python
df.dropna()
```

### Ha Ngo
- Replacing With Mean/Median/Mode
``` Python
df.isnull().sum()
df.fillna(df.mean())
df.fillna(df.median())
df['.....'] = df['....'].fillna(df['.....'].mode()[0])

``` 
### Hieu
- Predictive Techniques: based on observation techniques, assumptions to produce variables with correlation relationships, not random
### Minh

### Dat
- Filling with a regression model
``` Python
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
df.head()
testdf = df[df['.....'].isnull()==True]
traindf = df[df['.....'].isnull()==False]
y = traindf['.....']
traindf.drop(".....",axis=1,inplace=True)
lr.fit(traindf,y)
testdf.drop(".....",axis=1,inplace=True)
pred = lr.predict(testdf)
testdf['.....']= pred
```
