
from nltk.corpus import wordnet as wn


def get_all_similar_tos(word, pos=None):
    sim_tos=[]
    for ss in wn.synsets(word):
            for sim in ss.similar_tos():
                for lemma in sim.lemma_names():
                    sim_tos.append(str(lemma))
    return sim_tos

def get_all_hyponyms(word, pos=None):
    hypo=[]
    for ss in wn.synsets(word, pos=pos):
            for hyp in ss.hyponyms():
                for lemma in hyp.lemma_names():
                    hypo.append(str(lemma))
    return hypo


def get_all_synsets(word, pos=None):
    sset=[]
    for ss in wn.synsets(word):
        for lemma in ss.lemma_names():
             sset.append(str(lemma))
    return sset

#--------------------------------------------------------------------------------------------------------#
    
def exc_con_rain():
    contro_list=[]
    excite_list=[]
    excite_google=['amazing','fantastic','exciting','dramatic','terrific','excellent','thriller','fierce','alas','phew','outstanding']
    contro_google=['controversy','controversial','arguable','vexed','argument','bickering',
                   'difference','discussion','fuss','quarrel','row','beef','rumpus','dissention']
    for words in excite_google:
        s=get_all_similar_tos(words)
        for w in s:
            if w not in excite_list:
                excite_list.append(w)
        if words not in excite_list:
            excite_list.append(words)
    for words in contro_google:
        s=get_all_similar_tos(words)
        for w in s:
            if w not in contro_list:
                contro_list.append(w)
        if words not in contro_list:
            contro_list.append(words)
    rain_list=[]
    h=[]
    s=get_all_synsets('rain')
    for word in s:
        if word not in rain_list:
            rain_list.append(word)
        
    for word in s:
        h=get_all_hyponyms(word)
        for w in h:
            if w not in rain_list:
                rain_list.append(w)
    return excite_list, contro_list,rain_list

    
exc_con_rain()
