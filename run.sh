mkdir -p model
python main.py -n $1 -b $2 -a $3 -f "model/$3_$1_$2"
python check_baseline.py -n $1 -b $2 > o2 &
python check.py -n $1 -b $2 -a $3 -f "model/$3_$1_$2" > o1