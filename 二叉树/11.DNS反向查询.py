class TireNode:
    def __init__(self):
        CHAR_COUNT=11
        self.isLeaf=False
        self.url=None
        self.child=[None]*CHAR_COUNT
        i=0
        while i<CHAR_COUNT:
            self.child[i]=None
            i+=1
def getIndexFromChar(c):
    return 10 if c=='.' else (ord(c)-ord('0'))
def getCharFromIndex(i):
    return '.' if i==10 else ('0'+str(i))

class DNSache:
    def __init__(self):
        self.CHAR_COUNT=11
        self.root=TireNode()
    def insert(self,ip,url):
        lens=len(ip)
        pCrawl=self.root
        level=0
        while level<lens:
            index=getIndexFromChar(ip[level])
            if pCrawl.child[index]==None:
                pCrawl.child[index]=TireNode()
            pCrawl=pCrawl.child[index]
            pCrawl.isLeaf=True
            pCrawl.url=url
            level+=1
    def searchDNSache(self,ip):
            pCrawl=self.root
            lens=len(ip)
            level=0
            while level<lens:
                index=getIndexFromChar(ip[level])
                if pCrawl.child[index]==None:
                    return None
                pCrawl=pCrawl.child[index]
                level+=1
            if pCrawl!=None and pCrawl.isLeaf:
                return pCrawl.url
            return None
if __name__ == '__main__':
    ipAdds=['10.57.11.127','121.57.61.129','66.125.100.103']
    url=['www.samsung.com','www.samsung.net','www.google.com']
    n=len(ipAdds)
    cache=DNSache()
    for i in range(n):
        cache.insert(ipAdds[i],url[i])
        i+=1
    ip='121.57.61.129'
    res_url=cache.searchDNSache(ip)
    if res_url:
        print("ok>",res_url)
    else:
        print("no")















