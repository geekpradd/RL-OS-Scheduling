mkdir -p model
python3 main.py -n $1 -b $2 -a $3 -f "model/$3"
python3 check.py -n $1 -b $2 -a $3 -f "model/$3" &
python3 chck_baseline.py -n $1 -b $2


 