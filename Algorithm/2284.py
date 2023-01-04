def largestWordCount(messages: list[str], senders: list[str]) -> str:
    from collections import defaultdict
    tb = defaultdict(int)
    for meg , name in zip(messages,senders):
        tb[name] += len(meg.split(' '))
    mx = 0
    nmx = ''
    for name,value in tb.items():
        if value > mx:
            mx = value
            nmx = name
        elif value == mx:
            nmx = max(name,nmx)
    return nmx

if __name__ == '__main__':
    meg = ["tP x M VC h lmD","D X XF w V","sh m Pgl","pN pa","C SL m G Pn v","K z UL B W ee","Yf yo n V U Za f np","j J sk f qr e v t","L Q cJ c J Z jp E","Be a aO","nI c Gb k Y C QS N","Yi Bts","gp No g s VR","py A S sNf","ZS H Bi De dj dsh","ep MA KI Q Ou"]
    nam = ["OXlq","IFGaW","XQPeWJRszU","Gb","HArIr","Gb","FnZd","FnZd","HArIr","OXlq","IFGaW","XQPeWJRszU","EMoUs","Gb","EMoUs","EMoUs"]
    print(largestWordCount(meg,nam))