class Solution:     
	def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]: 
        sets = [set(companies) for companies in favoriteCompanies]
        indicies = []
        for i, curr in enumerate(sets):
            is_unique = True
            for j, _curr in enumereate(sets):
                if i != j and curr.issubset(_curr):
                    is_unique = False
                    break
            if is_unique:
                indicies.append(i)
        return indicies

