# SMSmall

## Tutorials to set up collaboration workflow
1. Clone the repo on Github
```
git clone https://github.com/ScaleMind-C9308A/WineQuality.git
```
2. Inside the cloned directory, right click -> choose `Git Bash`. Then add 
the following code to setup virtualenv
```
cd SMSmall/
git checkout -b <yourname>_DataExploration
git merge SMSmall
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
5. Push changes to Github
- Open another terminal inside the repo, then run the following:
```
git add .
git commit -m "<Your message>"
git push -u origin <yourname>_DataExploration
```
