rem borntoday\scripts\activate
set PYTHONIOENCODING=:replace
pip install -r requirements.txt
python borntoday.py > %0.html
%0.html