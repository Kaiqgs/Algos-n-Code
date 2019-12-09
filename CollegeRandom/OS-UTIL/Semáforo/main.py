from process import Process, ProcType
from collections import deque
import random

#critical region size;
REGION_SIZE = 1000
#how many times to iterate loading processes;
ITERATION_SIZE = 200
#how many events a process can do;
EVENTS_SIZE = 10

print_map = {ProcType.Include:"incluiu", 
             ProcType.Exclude:"excluiu"}

def new_processes():
  proclist = [Process(ProcType.Include, i) for i in range(5)] +\
             [Process(ProcType.Exclude, j) for j in range(5)]
  random.shuffle(proclist)
  return proclist

def create_region():
  return deque(maxlen=REGION_SIZE)

def print_so(idx, proc, insidx, valid):
  if(valid):
    print(f"Carga[{idx}]: {proc} {print_map[proc.ptype]} em posição[{insidx}]")
  else:
    print(f"Carga[{idx}]: {proc} {print_map[proc.ptype]}, mas tentativa falhou! Mudando processo.")

def main():

	crit_region = create_region()
	for i in range(ITERATION_SIZE):
	  proclist = new_processes()
	  for process in proclist:
	    for j in range(EVENTS_SIZE):
	      if(len(crit_region) < REGION_SIZE and 
	        process.ptype == ProcType.Include):
	        print_so(i, process, len(crit_region), True)
	        crit_region.append("INCLUDED")
	        
	      elif(len(crit_region) > 0 and
	           process.ptype == ProcType.Exclude):
	        print_so(i, process, 0, True)
	        crit_region.popleft()
	      else:
	          print_so(i, process, None, False) 
	          break
	print('Saída final:\n',','.join(crit_region))

if __name__ == '__main__':
	main()