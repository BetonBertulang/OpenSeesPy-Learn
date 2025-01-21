from openseespy.opensees import*

wipe() 

#Create model
# model('basic', '-ndm', ndm, '-ndf', ndf=ndm*(ndm+1)/2)
model('basic','-ndm',2,'-ndf',2)

#Define node
x  = [0,144,168,72]
y = [0,0,0,96]

for i in range(4):
    node(i,x[i],y[i])

printModel()