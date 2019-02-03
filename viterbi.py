import numpy as np


def run_viterbi(emission_scores, trans_scores, start_scores, end_scores):
    """Run the Viterbi algorithm.

    N - number of tokens (length of sentence)
    L - number of labels

    As an input, you are given:
    - Emission scores, as an NxL array
    - Transition scores (Yp -> Yc), as an LxL array
    - Start transition scores (S -> Y), as an Lx1 array
    - End transition scores (Y -> E), as an Lx1 array

    You have to return a tuple (s,y), where:
    - s is the score of the best sequence
    - y is the size N array/seq of integers representing the best sequence.
    """
    L = start_scores.shape[0]
    assert end_scores.shape[0] == L
    assert trans_scores.shape[0] == L
    assert trans_scores.shape[1] == L
    assert emission_scores.shape[1] == L
    N = emission_scores.shape[0]
    
    #print("1.",L)
    #print("2.",N)
    #emission_scores = [[emission_scores[j][i] for j in range(len(emission_scores))] for i in range(len(emission_scores[0]))]
    #start_scores=tf.transpose(start_scores)
    #print("E:",emission_scores)
    #print ("S",start_scores)
    
    y = [[0] * (N) for j in range(L)]
    path= [[0] * (N) for j in range(L)]
    for i in range(L):
        y[i][0]=(start_scores[i]+emission_scores[0][i])
        #print (y)
        path[i][0]=i
        #print ("Path:",path)
    for t in range (1,N):
        #new_path=[[0] * (N+1) for j in range(L+1)]
        for o in range(0,L):
            prob=-float("inf")
            state=0
            for m in range(0,L):
                nprob = (y[m][t-1] + trans_scores[m][o] + emission_scores[t][o])
                if (nprob > prob):
                        prob = nprob
                        state = m 
#                if (o==L-1):
#                        y[o][t-1]=(end_scores[o]+y[t][o])
            #y[o][t]=prob
            y[o][t]=prob
            path[o][t]=state
    for m in range(0,L):
        y[m][N-1]=end_scores[m]+y[m][N-1]
        
        # Don't need to remember the old paths
        # path = newpath
    prob=-float("inf")
    state=0
    for i in range (0,L):
        if (y[i][N-1] > prob):
            prob=y[i][N-1]
            state=i
    
    print (y)
    print("l",path)
    y1=[]
    for t in range (N-1,-1,-1):
        y1.append(state)
        state=path[state][t]
        #print (list(reversed(y1)))
    return (prob,list(reversed(y1)))
            
        
        
                        
        
         #stupid sequence
#    for i in range(N):
#          y.append(i % L)
#    # score set to 0
#    return (0.0, y)
