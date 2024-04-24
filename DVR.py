m=[[0,1,1,99,1,1,99],

    [1,0,1,99,99,99,99],

    [1,1,0,1,99,99,99],

    [99,99,1,0,99,99,1],

    [1,99,99,99,0,99,99],

    [1,99,99,99,99,0,1],

    [99,99,99,1,99,1,0]]

l=[]

for i in range(len(m)):

    a=[]

    for j in range(len(m[i])):

        if m[i][j]!=99:

            a.append(j)

    l.append(a)

for i in range(len(m)):

    for j in range(len(m)):

        for k in l[i]:

            if m[i][k]+m[k][j]<m[i][j]:

                m[i][j]=m[i][k]+m[k][j] 

ch='A'

for i in range(len(m)):

    print("Node ",ch," to-->")

    c='A'

    for j in range(len(m)):

        print("   Node ",chr(ord(c)+j)," = ",m[i][j])

    ch=chr(ord(ch)+1)

    print()

