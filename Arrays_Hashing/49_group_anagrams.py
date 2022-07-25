class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = []
        for i in range(len(strs)):
            item = ''.join(sorted(strs[i]))    
            added = False
            for j in range(len(output)):
                if output[j][0] == item: 
                    added = True
                    output[j].append(strs[i])     
            if not added: 
                output.append([item, strs[i]])       
        
        for i in range(len(output)):
            output[i].pop(0)
                       
        return output
