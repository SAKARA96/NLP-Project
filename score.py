def get_score(score,match_type):
    if "tie" in score:
        return 10
    elif "wkt" in score:
        score=score.strip().split()
        for i in score:
            if i.isdigit():
                nwkts= int(i)
        if nwkts <4:
            return 10
        if nwkts>=4 and nwkts<=7:
            return 5
        if nwkts>=8:
            return 3
    elif "wicket" in score:
        score=score.strip().split()
        for i in score:
            if i.isdigit():
                nwkts= int(i)      
        if nwkts <4:
            return 10
        if nwkts>=4 and nwkts<=7:
            return 5
        if nwkts>=8:
            return 3
    elif "run" in score:
        score=score.strip().split()
        for i in score:
            if i.isdigit():
                nruns= int(i)
        if "T20" in match_type:
            if (nruns>=1 and nruns<=5):
                return 10
            if (nruns>5 and nruns<=10): 
                return 7
            if (nruns>10 and nruns<=20): 
                return 5
            if nruns>20:
                return 1
        if "ODI" in match_type:
            if nruns<=10:
                return 10
            if nruns>10 and nruns<=25:
                return 7
            if nruns>25 and nruns<=40:
                return 5
            if nruns>40:
                return 1
            

