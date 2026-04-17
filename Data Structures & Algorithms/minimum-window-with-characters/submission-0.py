class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #s->input string ,t->target string
        if t=="": return ""#edge case->if t is empty nthing to match so return empty string 
        need={}#freq map of t
        for c in t:
            need[c]=1+need.get(c,0)
        have=0#how many of thsoe r currently satisfied
        need_count=len(need)
        window={}#stores frequency of characters in current window
        res=[-1,-1]
        res_len=float('inf')
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)#add current character to window frequency
            if c in need and window[c]==need[c]:
                have+=1
                # Current window is valid (contains all required chars)
                #now we try to minimise it
            while have==need_count:
                if (r-l+1)<res_len:
                    res=[l,r]
                    res_len=r-l+1
                
                window[s[l]]-=1
                if s[l] in need and window[s[l]]<need[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if res_len!=float("inf") else ""


                


        