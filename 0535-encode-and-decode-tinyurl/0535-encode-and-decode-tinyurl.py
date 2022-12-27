class Codec:

    def encode(self, longUrl: str) -> str:
        shortUrl = ""
        self.char_map = {}
        self.slashes = {}
        i = 0
        while i < len(longUrl):
            key = longUrl[i]
            value = ""
            while i < len(longUrl) and longUrl[i] != "/":
                value += longUrl[i]
                i += 1
            slash_counter = 0
            while i < len(longUrl) and longUrl[i] == "/":
                slash_counter += 1
                i += 1
            if key not in self.char_map:
                self.char_map[key] = []
                self.slashes[key] = []
            shortUrl += str(len(self.char_map[key])) + key
            self.slashes[key].append(slash_counter)
            self.char_map[key].append(value)
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        longUrl = ""
        is_index = True
        for i in range(len(shortUrl)):
            if is_index:
                index = int(shortUrl[i])
            else:
                key = shortUrl[i]
                longUrl += self.char_map[key][index] + ("/" * self.slashes[key][index])
            is_index = not is_index
        return longUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))