import numpy as np
import cv2
import math

img = cv2.imread('harris.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,50,0.10,1)
corners = np.int0(corners)

m=0
a=np.empty([4],dtype=int)
b=np.empty([4],dtype=int)

for i in corners:
    x,y = i.ravel()
    print x,y
    gray[x,y]=100
	#cv2.circle(img,(x,y),1,255,-1)
    #img[x,y]=[100,50,50]


rows,cols = gray.shape
print rows,cols
for i in range(0,rows):
  	for j in range(0,cols):
  		if np.any(gray[i,j]==100):
 			a[m]=i
			b[m]=j
			m=m+1
			
cv2.imwrite('shitom.jpg',gray)


boundaries = [	(80,120) ]

print a,b

for (lower, upper) in boundaries:
	
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 	
	mask = cv2.inRange(gray, lower, upper)
	output = cv2.bitwise_and(gray, gray, mask = mask)
 
	cv2.imwrite("images.jpg",  output)

# 2nd is small...
def point(a1,a2,b1,b2):
	print a1,a2,b1,b2
	ver_diff=abs(b1-b2)
	hor_diff=abs(a1-a2)

	dist= math.sqrt((ver_diff**2)+(hor_diff**2))
	print dist

	points=int(dist/10)
	print points

	a=np.empty([points+1],dtype=int)
	b=np.empty([points+1],dtype=int)

	ver_dis = int(ver_diff/points)
	hor_dis = int(hor_diff/points)

	for i in range(1,points):
		a[i]=a2+(i*hor_dis)
		b[i]=b2+(i*ver_dis)
		
	a[0]=a2
	b[0]=b2

	for i in range(0,points):
		output[a[i],b[i]]=100
		#print gray[a[i],b[i]]
	a[points]=a1
	b[points]=b1

	return points

# #print a,b
nett=0
count0=point(a[1],a[0],b[1],b[0])
nett=nett+count0
count1=point(a[3],a[1],b[3],b[1])
nett=nett+count1
count2=point(a[3],a[2],b[3],b[2])
nett=nett+count2
count3=point(a[2],a[0],b[2],b[0])
nett=nett+count3

hor_ch = ((count0+count2)/2)
ver_ch = ((count1+count3)/2)


cv2.imwrite('test.jpg',output)
print nett

x=0
m=np.empty([nett],dtype=int)		
n=np.empty([nett],dtype=int)
classifier=0	
if(hor_ch>ver_ch):
	for i in range(0,rows):
		for j in range(0,cols):
			if(output[i,j]==100):
				m[x]=i
				n[x]=j
				x=x+1
else:
	for j in range(0,cols):
		for i in range(0,rows):
			if(output[i,j]==100):
				m[x]=i
				n[x]=j
				x=x+1

#IMPORTANT: Plots the line
print m,n

for x in range(0,nett-1):
	cv2.line(output,(m[x],n[x]),(m[x+1],n[x+1]),(255,255,255),1)

cv2.imwrite("modified.jpg",output)

cv2.waitKey(0)