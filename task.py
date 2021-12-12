import sys
import re
def help():
	sa = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
	sys.stdout.buffer.write(sa.encode('utf8'))

def add(p,s):
	f = open('task.txt', 'a')
	f.write(p)
	f.write(' ')
	f.write(s)
	f.write("\n")
	f.close()
	s = '"'+s+'"'
	print(f"Added task: {s} with priority {p}")

def nec():
	try:
		f = open('task.txt', 'r')
		for line in f:
			line = line.strip('\n')
			x=re.search(r'\d+', line).group()
			priority.append(int(x))
			line=line.lstrip("0123456789 ")
			line= f'{line} [{x}]'
			d.update({int(x): line})
	except:
		sys.stdout.buffer.write("There are no pending tasks!".encode('utf8'))

def ls():
	try:
		nec()
		k = 1
		for i in sorted(priority):
			sys.stdout.buffer.write(f"{k}. {d[i]}".encode('utf8'))
			sys.stdout.buffer.write("\n".encode('utf8'))
			k = k+1
	except Exception as e:
		raise e

def done(no):
	try:
		nec()
		no = int(no)
		f = open('completed.txt', 'a')
		if no==0:
			raise Exception
		x=sorted(priority)[no-1]
		st = d[x]
		st=st.rstrip("0123456789[] ")
		f.write(st)
		f.write("\n")
		f.close()
		print(f"Marked item as done.")	
		with open("task.txt", "r+") as f:
			lines = f.readlines()
			f.seek(0)
			for i in lines:
				if i.strip('\n') != f'{x} {st}':
					f.write(i)
			f.truncate()
	except:
		print(f"Error: no incomplete item with index #{no} exists.")

def deL(no):
	try:
		nec()
		no = int(no)
		if no==0:
			raise Exception
		x=sorted(priority)[no-1]
		st = d[x]
		st=st.rstrip("0123456789[] ")
		with open("task.txt", "r+") as f:
			lines = f.readlines()
			f.seek(0)
			for i in lines:
				if i.strip('\n') != f'{x} {st}':
					f.write(i)
			f.truncate()
		print(f"Deleted task #{no}")
	except Exception as e:
		print(f"Error: task with index #{no} does not exist. Nothing deleted.")

def report():
	try:
		F=open('task.txt', 'r')
		D=F.readlines()
		up=f'Pending : {len(D)}'
		sys.stdout.buffer.write(up.encode('utf8'))
		sys.stdout.buffer.write("\n".encode('utf8'))
		ls()
		sys.stdout.buffer.write("\n".encode('utf8'))
		nf = open('completed.txt', 'r')
		don=nf.readlines()
		p=1
		print(f'Completed : {len(don)}')
		for lines in don:
			lines = lines.strip('\n')
			print(f'{p}. {lines}')
			p=p+1
	except:
		print(f'error')

if __name__ == '__main__':
	try:
		d = {}
		priority = []
		args = sys.argv
		if(args[1] == 'del'):
			args[1] = 'deL'
		if(args[1] == 'add' and len(args[2:]) == 0):
			sys.stdout.buffer.write("Error: Missing tasks string. Nothing added!".encode('utf8'))
		elif(args[1] == 'done' and len(args[2:]) == 0):
			sys.stdout.buffer.write("Error: Missing NUMBER for marking tasks as done.".encode('utf8'))
		elif(args[1] == 'deL' and len(args[2:]) == 0):
			sys.stdout.buffer.write("Error: Missing NUMBER for deleting tasks.".encode('utf8'))
		else:
			globals()[args[1]](*args[2:])
	except Exception as e:
		s = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
		sys.stdout.buffer.write(s.encode('utf8'))