# borntoday
Python script to extract a list of who was born or died on a specific date and output as HTML

Wikipedia has a page for each day of the year eg: https://en.wikipedia.org/wiki/December_11

Use this to generate the list


Notes:
I had problems running this due to Unicode error messages
  * "UnicodeEncodeError: 'charmap' codec can't encode character ";
The suggested solution is to run the console as unicode
  * py -mpip install win-unicode-console
  * py -mrun your_script.py
or, to replace any unicode characters with an empty string
  * set PYTHONIOENCODING=:replace
[See this Stackoverflow page for more info](http://stackoverflow.com/questions/5419/python-unicode-and-the-windows-console/32176732#32176732)
