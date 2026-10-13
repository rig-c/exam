import subprocess,sys,shlex,datetime
from pathlib import Path
cmd=sys.argv[1:]
with open('run/transcript.md','a') as f:f.write('\n```sh\n'+shlex.join(cmd)+'\n```\n')
p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
print(p.stdout)
with open('run/transcript.md','a') as f:f.write('```text\n'+'\n'.join(p.stdout.splitlines()[-16:])+f'\nexit: {p.returncode}\n```\n')
sys.exit(p.returncode)
