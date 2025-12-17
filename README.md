# Eric's Weight
This project contains Eric's weight data from 08/2013 through 03/2025.

It also contains various visualizations and analyses using matplotlib,
plotly, and streamlit.


## Usage
```
# works with Python 3.12 on a Mac

# Install uv if you haven't already (https://github.com/astral-sh/uv)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a virtual environment and install dependencies
uv venv
source .venv/bin/activate
uv pip install -e .

# Launch Jupyter notebook
cd notebooks
jupyter notebook
```

### Alternative: Using pyenv with uv
If you want to use a specific Python version with pyenv:
```
# Install Python 3.12 via pyenv
pyenv install 3.12.0
pyenv local 3.12.0

# Create virtual environment with uv using pyenv's Python
uv venv --python $(pyenv which python)
source .venv/bin/activate
uv pip install -e .

cd notebooks
jupyter notebook
```