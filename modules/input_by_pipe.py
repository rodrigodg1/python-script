import sys

#no terminal, executar: 
# echo "Rodrigo" | python3 input_by_pipe.py 
for n in sys.stdin:
    print(f"Ola {n}")

