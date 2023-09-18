import subprocess

while True:
    input = input("enter command:")
    input = input.split(" ")
    if "exit" in input:
        break
    proc = subprocess.Popen(input,stdout=subprocess.PIPE)
    del input
    while True:
        out = proc.stdout.readline()
        if proc.poll is not None or not out:
            break
        print(out.decode("utf-8"))
        del out