# SMSmall

## How to open jupyter notebook in Google Colab

- Click to the jupyter notebook you want to open
- From the url address, replace `github.com` with `colab.research.google.com/github/`

## Resources
- [Visualize the predictive power of a numerical feature in a classification problem](https://www.yourdatateacher.com/2022/03/30/visualize-the-predictive-power-of-a-numerical-feature-in-a-classification-problem/?fbclid=IwAR0fMpFNpv1phft8PSVX7j44cCWqq_iLh2HvAhsJCRrE8vFv-FLan3Ky1_I)
- [Matplotlib: Plotting Subplots in a Loop](https://engineeringfordatascience.com/posts/matplotlib_subplots/)
- [Using Pandas and Python to Explore Your Dataset](https://realpython.com/pandas-python-explore-dataset/)
- [Predicting Wine Quality with Several Classification Techniques](https://medium0.com/m/global-identity?redirectUrl=https%3A%2F%2Ftowardsdatascience.com%2Fpredicting-wine-quality-with-several-classification-techniques-179038ea6434)
- [Red Wine Quality Prediction Using Regression Modeling and Machine Learning](https://medium0.com/m/global-identity?redirectUrl=https%3A%2F%2Ftowardsdatascience.com%2Fred-wine-quality-prediction-using-regression-modeling-and-machine-learning-7a3e2c3e1f46)
- [Choosing the right estimator](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html?fbclid=IwAR1xeenr-qKR2C_pMwPV-9ppC5K38I6bSQwM004vmTsVzGh69vVXs-oBygE)

## Tutorials to set up collaboration workflow
1. Clone the repo on Github
```
git clone https://github.com/ScaleMind-C9308A/WineQuality.git
```
2. Inside the cloned directory, right click -> choose `Git Bash`. Then add 
the following code to create your new branch && setup virtualenv
```
cd SMSmall/
# Create your new branch
git checkout -b <yourname>_DataExplore_<Task>
# Merge your newly created branch with origin/SMSmall branch on remote
git merge origin/SMSmall
```
- An editing terminal (Vim) will open and show you the generated merging messages. To save the message and continue with the merge,
press `Esc` key -> type `:wq` -> press Enter
- Then run the following line to create new virtual environment
```
# Create virtual environment
virtualenv .env
source .env/bin/activate
```
3. Install the required python pkgs using one of the 2 options:
```
# Option 1: 
pip install -r requirements.txt
# Option 2:
pip install -U jupyter numpy pandas matplotlib scipy seaborn 
```
4. Open jupyter notebook
```
jupyter notebook
```
- Then choose the `SMSmall_Wine_quality_data_exploration.ipynb`
- Edit directly into the jupyter notebook according to assignments
  - **!Remember to comment your name before your code**
- (Optional) You can choose to read my notebook (only as reference!) `Data Exploration - Wine Dataset.ipynb`
5. Push changes to Github
- Open another terminal inside the repo, then run the following:
```
git pull origin SMSmall # pull before push
# Commit your changes and push your branch to Github
git add .
git commit -m "<Your message>"
git push -u origin <yourname>_DataExploration
```
