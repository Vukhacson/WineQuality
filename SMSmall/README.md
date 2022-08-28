# SMSmall

## Tutorials to set up Jupyter Notebook on Local Machine
1. Clone the repo on Github
```
git clone https://github.com/ScaleMind-C9308A/WineQuality.git
```
2. Inside the cloned directory, right click -> choose `Git Bash`. Then add 
the following code to setup virtualenv
```
cd SMSmall/
virtualenv .env
source .env/bin/activate
```
3. Install the python pkgs using one of the 2 options:
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
