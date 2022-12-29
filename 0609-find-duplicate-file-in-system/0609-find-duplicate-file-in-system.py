class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_path = defaultdict(list)
        for path in paths:
            for i in range(len(path)):
                if path[i] == " ":
                    dir_path = path[:i]
                    files = path[i + 1:].split()
                    for file in files:
                        for j in range(len(file)):
                            if file[j] == "(":
                                content = file[j + 1:len(file) - 1]
                                content_path[content].append(dir_path + "/" + file[:j])
                                break
                    break
        return [content_path[path] for path in content_path if len(content_path[path]) > 1]