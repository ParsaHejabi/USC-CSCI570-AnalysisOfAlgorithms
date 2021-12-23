rm output.txt
{ /usr/bin/time -f "%U\n%M.0" python3 efficient.py input.txt ; } 2>> output.txt
#{ gtime -f "%U\n%M.0" python3 efficient.py input.txt ; } 2>> output.txt