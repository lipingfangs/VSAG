def populationfrequencybed(coveragebedfilename,dictracks,mutilplesamplecolor,maintracklength,anncolor):
    coveragefile = open(coveragebedfilename,"r")
    coveragefileline =   coveragefile.readlines()
    coveragefile.close()
    readbottom = [] 
    populationfrequencybedrectedlist = []
    dicsamplesreadbottomtemp = {}
    samplesreadbottomtemplist =[]
    countsample = 0
    donerunsample = []
    readbottomtemplist = []
    trackstartlist = []
    textwithdraw = maintracklength/100 
    dicfrequencyscores = {}
    for i in coveragefileline:
        #print(i)
        samplename = i.split()[5]
        if samplename not in  samplesreadbottomtemplist:
            samplesreadbottomtemplist.append(samplename)
            dicsamplesreadbottomtemp[samplename] =  [countsample,mutilplesamplecolor[countsample]]
            countsample += 1
   # print(samplesreadbottomtemplist)
    #print(dicsamplesreadbottomtemp)
    for i in coveragefileline:
             
        samplename = i.split()[5]
        i =i.strip()
        chrom = i.split()[3]
        if chrom in dictracks.keys():
            readbottomtemp = dictracks[chrom][0] + 0.1 + dicsamplesreadbottomtemp[samplename][0]
            if readbottomtemp not in readbottomtemplist:
                readbottomtemplist.append(readbottomtemp)
            if dictracks[chrom][2] not in trackstartlist:
                trackstartlist.append(dictracks[chrom][2])
            readstart  =int(i.split()[1]) 
            readend =int(i.split()[2])

        #drawcoverage       
            coveragescores =  float(i.split()[4]) * 0.8 #*0.005
            readforpathpointlength = readstart - dictracks[chrom][1] 
            readfordrawstart= dictracks[chrom][2] + readforpathpointlength 
            readlength = readend - readstart
            try:
                dicfrequencyscores[str(readfordrawstart)+"_"+str(readlength)].append(float(i.split()[4]))
            except:
                dicfrequencyscores[str(readfordrawstart)+"_"+str(readlength)] = [readbottomtemp]
                dicfrequencyscores[str(readfordrawstart)+"_"+str(readlength)].append(float(i.split()[4]))
            left, bottom, width, height = (readfordrawstart, readbottomtemp,readlength,  coveragescores) 
            coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                            fill=True,
                                            color=dicsamplesreadbottomtemp[samplename][1],
                                           linewidth=0.5) 
            populationfrequencybedrectedlist.append(coveragerected)
        
    print(readbottomtemplist, trackstartlist)
    rulerlength = 5
    rulerheight = 0.8
    trackstartlist = int(len(readbottomtemplist)/len(trackstartlist)) * trackstartlist
    
    #ruler of frequencey
    for i in range(len(readbottomtemplist)): 
        left, bottom, width, height = (trackstartlist[i]-50 , readbottomtemplist[i],rulerlength,   rulerheight)
        coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color="black",
                                       linewidth=2)
        populationfrequencybedrectedlist.append(coveragerected)
        coveragerected=mpatches.Rectangle((left-5,bottom),width,height-0.75, 
                                        fill=True,
                                        color="black",
                                       linewidth=2)
        populationfrequencybedrectedlist.append(coveragerected)
        plt.text(left-textwithdraw,bottom-0.05,"0",fontsize=8)
        coveragerected=mpatches.Rectangle((left-5,bottom+0.75),width,height-0.75, 
                                        fill=True,
                                        color="black",
                                       linewidth=2)
        populationfrequencybedrectedlist.append(coveragerected)
        plt.text(left-textwithdraw,bottom+0.65,"1",fontsize=8)
        #plt.text("shahahs")
   # print(dicfrequencyscores)
    #difference annotation
    for i in dicfrequencyscores.keys():
        if len(dicfrequencyscores[i])>1:
            if abs(dicfrequencyscores[i][1]-dicfrequencyscores[i][2])>0.2:
                left, bottom, width, height = (float(i.split("_")[0]), dicfrequencyscores[i][0]-0.6,float(i.split("_")[1]), 0.5) 
                coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                                fill=True,
                                                color=anncolor,
                                               linewidth=0.5) 
                populationfrequencybedrectedlist.append(coveragerected)                
                
            
    
    return populationfrequencybedrectedlist,samplesreadbottomtemplist
