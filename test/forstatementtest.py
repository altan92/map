import networkx as nx
import sys
def main():
    for i in range(0, int(10)):
        print(i)
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'