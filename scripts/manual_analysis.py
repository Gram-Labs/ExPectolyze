import csv 



def analysis1(gene):
    rnaseqdata = '/data/ruderferlab/sandbox/grahame/expecto/data/HBCC_DLPFC_eqtlResidualExpression_WithoutSVbasedOutierIndividualsV2.tsv'
    filtereddata = '/data/ruderferlab/sandbox/grahame/expecto/data/postmap_filtered.tsv'
    inter = '/data/ruderferlab/sandbox/grahame/expecto/data/intermediate_data.tsv'

    output1 = csv.writer(open('/data/ruderferlab/sandbox/grahame/expecto/data/intermediate_data.tsv', 'w'), delimiter='\t')
    output2 = csv.writer(open('/data/ruderferlab/sandbox/grahame/expecto/data/analysis_data.tsv', 'w'), delimiter='\t')


    with open(filtereddata, 'r') as datafile:

        datareader = csv.reader(datafile, delimiter='\t')
        
        variantList = []
        for line in datareader:
            
            if line[1] == gene:
                #print (line[0])
                variantList.append(int(line[0]))
                idList = line[4].strip('][').split(', ')
                newList = []
                for item in idList:
                    item = item.strip("''")
                    newList.append(item)
                newerList = []
                for item in newList:
                    if ':' in item:
                        itemSplit = item.split(':')
                        newerList.append(int(itemSplit[-1]))
                #print (newerList)
                output1.writerow([str(newerList)])
        print (variantList)
    datafile.close()
        

def analysis2(gene):

    print(' ')
    rnaseqdata = '/data/ruderferlab/sandbox/grahame/expecto/data/HBCC_DLPFC_eqtlResidualExpression_WithoutSVbasedOutierIndividualsV2.tsv'
    filtereddata = '/data/ruderferlab/sandbox/grahame/expecto/data/postmap_filtered.tsv'
    inter = '/data/ruderferlab/sandbox/grahame/expecto/data/intermediate_data.tsv'

    output2 = csv.writer(open('/data/ruderferlab/sandbox/grahame/expecto/data/analysis_data.tsv', 'w'), delimiter='\t')

    with open (rnaseqdata, 'r') as rnafile:

        rnareader = csv.reader(rnafile, delimiter='\t')
        #interreader = interfile.readlines()

        for rnaline in rnareader:
            if rnaline[0] == gene:
                rnalist = []
                for item in rnaline:
                    rnalist.append(item)
        
        #print (rnalist)
        #print(' ')

    for line1 in open(inter):
        #print (line1)
        list1 = str(line1)
        list2 = list1.rstrip()
        list3 = list2.strip('][').split(', ')
        #print (list3)
        
        for item in list3:
            itemindex = list3.index(item)   # these are the RNA-seq file indices
            list3[itemindex] = rnalist[int(item)]
        
        list4 = []
        for item in list3:
            if item != 'NA':
                list4.append(float(item))
        output2.writerow([str(list4)])

        tally = 0
        for item in list4:
            tally = tally + item
        avg = tally/(len(list4))
        print (str(avg))
        #print (list3)
                
         
              




                #print (newerList)
                #print (' ')



def analysis3(gene):

    varList = [2180524, 2181963, 2182342, 2182470, 2183754, 2184280, 2184401, 2184692, 2184988, 2185159, 2186985, 2187085, 2189196, 2189477, 2192433, 2192639, 2192948, 2193923, 2194015, 2195117, 2200169, 2200341, 2200390, 2200404, 2202148, 2202572, 2202774, 2202967, 2203490, 2204755, 2204790, 2205527, 2205548, 2205581, 2206444, 2207480, 2208751, 2211849, 2211944, 2213665, 2214431, 2214453, 2214743, 2214813, 2215121, 2215211, 2215651, 2216368, 2216391, 2217065, 2218129, 2218264, 2218265, 2218920, 2218937, 2218965, 2218968, 2219315, 2219439, 2219613, 2220070, 2220391, 2220425, 2220517, 2220649, 2221222, 2221273, 2221534, 2221634, 2221636, 2221838, 2222076, 2222177, 2222368, 2222497, 2222560, 2222583, 2223123, 2223258, 2223645, 2223866, 2224282, 2224609, 2224645, 2224836, 2225158, 2225251, 2225284, 2225412, 2226333, 2227422, 2227675, 2229156, 2229301, 2229447, 2229478, 2229553, 2229917, 2230511, 2230799, 2231463, 2231567, 2231966, 2232532, 2233312, 2233961, 2234251, 2234632, 2235019, 2235656, 2235662, 2235672, 2236339, 2236359, 2236697, 2236758, 2237248, 2240006, 2243518, 2243564, 2244905, 2245221, 2245439, 2245570, 2245633, 2246287, 2246513, 2247073, 2247399, 2247487, 2247645, 2247985, 2248383, 2248624, 2249236, 2251119, 2251160, 2251348, 2251357, 2251947, 2251982, 2252191, 2252759, 2254516, 2254910, 2255633, 2256011, 2256245, 2256288, 2256471, 2256933, 2257018, 2257491, 2257695, 2257727, 2257863, 2257886, 2257931, 2258323, 2258473, 2260050, 2260545, 2261177, 2261222, 2261983, 2263427, 2263438, 2263666, 2263888, 2264697, 2265026, 2265070, 2265176, 2265219, 2265794, 2265881, 2265969, 2266078, 2266714, 2266725, 2266807, 2266933, 2267297, 2267557, 2268570, 2268580, 2268650, 2268668, 2268678, 2268738, 2268791, 2269881, 2269899, 2269948, 2270009, 2270098, 2271674, 2271706, 2271864, 2272003, 2272064, 2272203, 2272226, 2272246, 2272481, 2272890, 2272903, 2273144, 2273286, 2273572, 2273576, 2273905, 2274173, 2274438, 2274884, 2274956, 2275138, 2275376, 2275695, 2275949, 2276022, 2276073, 2276196, 2276419, 2276881, 2276996, 2277166, 2277213, 2277392, 2277550, 2277827, 2278115, 2278240, 2278648, 2278651]
    filtereddata = '/data/ruderferlab/sandbox/grahame/expecto/data/postmap_filtered.tsv'

    with open (filtereddata, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader: 
            if int(line[0]) in varList:
                print (float(line[2]))








if __name__ == '__main__':

    choice = input('Analyze by gene or person? ')

    if choice == 'gene':
        gene = input('Gene: ')
        analysis3(gene)
'''
    elif choice == 'person':
        person = input('DNA ID of person: ')
        analysis3(person)
'''