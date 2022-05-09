import shlex
import subprocess

p = None

def start_effect(effect_file):
  global p
  cmd = "sudo killall cava"
  cmds = shlex.split(cmd)
  subprocess.Popen(cmds)
  if(p != None):
    p.kill()
  cmd = "sudo python3 ./effects/" + effect_file
  cmds = shlex.split(cmd)
  p = subprocess.Popen(cmds, start_new_session=True)
