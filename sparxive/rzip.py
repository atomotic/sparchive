import subprocess

def compress(uncompressed, compressed, level=6):
    args = ["rzip", uncompressed, "-k", "-%d"%(level), "-o", compressed]
    subprocess.check_call(args)
    
def uncompress(compressed, uncompressed):
    args = ["rzip", compressed, "-d", "-k", "-o", uncompressed]
    subprocess.check_call(args)