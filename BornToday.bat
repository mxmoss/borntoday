rem borntoday\scripts\activate
set PYTHONIOENCODING=:replace
python -m venv borntoday
borntoday\Scripts\activate
pip install -r requirements.txt
python borntoday.py > %0.html
%0.html