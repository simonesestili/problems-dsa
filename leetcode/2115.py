class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        graph, indeg = defaultdict(list), defaultdict(int)
        for recipe, reqs in zip(recipes, ingredients):
            for req in reqs:
                graph[req].append(recipe)
            indeg[recipe] = len(reqs)

        ans, q, recipes = [], deque(supplies), set(recipes)
        while q:
            item = q.popleft()
            if item in recipes:
                ans.append(item)
            for parent in graph[item]:
                indeg[parent] -= 1
                if not indeg[parent]:
                    q.append(parent)
        return ans

