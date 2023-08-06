class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        
        @cache
        def count(song, left):
            if left == 0:
                if song == n:
                    return 1
                return 0
            
            total = 0
            if song + 1 <= n:
                total += (n - song) * count(song + 1, left - 1)
            
            if song - k > 0:
                total += (song - k) * count(song, left - 1)
            
            return total % (10 ** 9 + 7)
        
        return count(0, goal)