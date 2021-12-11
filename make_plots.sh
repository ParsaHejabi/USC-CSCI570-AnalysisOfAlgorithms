ITER=1
for input in ./inputs2/input*.txt; do
  echo "Running basic algorithm for $input";
  #{ /usr/bin/time -f "%U\n%M.0" python3 4082809473_1605039563_6426152619_basic.py input.txt ; } 2>> output.txt
  { gtime -f "%U\n%M.0" python3 4082809473_1605039563_6426152619_basic.py "${input}" ; } 2>> ./outputs2/output${ITER}_basic.txt

  echo "Running efficient algorithm for $input";
  #{ /usr/bin/time -f "%U\n%M.0" python3 4082809473_1605039563_6426152619_efficient.py input.txt ; } 2>> output.txt
  { gtime -f "%U\n%M.0" python3 4082809473_1605039563_6426152619_efficient.py "${input}" ; } 2>> ./outputs2/output${ITER}_efficient.txt
  ((ITER=ITER+1))
#  if [[ "$ITER" -eq 11 ]]; then
#    break;
#  fi
done