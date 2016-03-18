import recsys.algorithm
from recsys.algorithm.factorize import SVD

def Reco():
	print "User?"
	User = int(raw_input())
	rec = svd.recommend(User, is_row=False)

	movies = []
	for line in open('./ml-1m/movies.dat'):
    		data = line.strip('\r\n').split('::')
    		movies.append(data[1])
	for i in range(len(rec)):
		print movies[rec[i][0]]

def Rate():
	print "User?"
	User = int(raw_input())
	print "Movie?"
	mov = int(raw_input())
	print "rate?"
	rate = int(raw_input())
	file = open('ratings.dat','a')
	file.write(str(User)+"::"+str(mov)+"::"+str(rate)+"::94324324323\n")
	file.close()

def Compute():
	svd = SVD()
	svd.load_data(filename='./ml-1m/ratings.dat', sep='::', format={'col':0, 'row':1, 'value':2, 'ids': int})
	svd.compute(k=100, min_values=10, pre_normalize=None, mean_center=True, post_normalize=True, savefile='./mvsvd')
	
svd = SVD(filename='./mvsvd')
print "task?\n1:recommend to user\n2:Add users rating\n3::recompute SVD"
t= int(raw_input())
if t==1:
	Reco()
if t==2:
	Rate()
if t==3:
	Compute()

