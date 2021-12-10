rm output.txt
#{ /usr/bin/time -f "%U\n%M.0" python3 4082809473_1605039563_6426152619_basic.py input.txt output.txt ; } 2>> output.txt
{ gtime -f "%U\n%M.0" python3 4082809473_1605039563_6426152619_basic.py input.txt output.txt ; } 2>> output.txt