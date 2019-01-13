l1=[656,'jhbd',884,'helo']
l2=[8434,'yo','AIO','ZU798']
l3=['sjcvhi',843]

print 'length1=',len(l1)
print 'length2=',len(l2)
print 'length3=',len(l3)

l1.append('fool')
print l1
l2.insert(3,786)
print l2
del l2[2]
print l2
l3.reverse()
print l3

print l1+l2+l3
l4=l1+l2+l3
l4.sort()
print l4

print max(l4)
print min(l4)
