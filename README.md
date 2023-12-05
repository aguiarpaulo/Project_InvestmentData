#My ETL Project
1. Clone the repository:
```bash
git clone https://github.com/aguiarpaulo/Project_InvestmentData.git

cd Project_InvestmentData
```
2. Configure the correct Python version with pyenv:
```bash
pyenv install 3.11.3
pyenv local 3.11.3
```
3. Install project dependencies:
```bash
poetry install
```
4. Activate the virtual environment:
```bash
poetry shell
```
5. Add selenium:
```bash
poetry add selenium
```
6. Run the pipeline run command to perform ETL:
```bash
python3 main.py
```
7. Check in the download foler if the file was generated correctly.
```
Contact:
Paulo Aguiar - aguiarlapaulo@gmail.com
