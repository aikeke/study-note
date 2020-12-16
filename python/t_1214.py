def groupAnagrams(strs):
    moban={}
    for i in strs:              
        temp="".join(sorted(i))
        if moban.get(temp):
            moban.get(temp).append(i)
        else:
            moban[temp]=[i]
    return moban.values()
strs=["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
