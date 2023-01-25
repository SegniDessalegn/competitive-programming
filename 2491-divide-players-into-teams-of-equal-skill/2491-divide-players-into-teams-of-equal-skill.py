class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        l = 0
        r = len(skill) - 1
        team_sum = skill[l] + skill[r]
        chem_sum = 0
        while l < r:
            if skill[l] + skill[r] != team_sum:
                return -1
            chem_sum += (skill[l] * skill[r])
            l += 1
            r -= 1
        
        return chem_sum
        