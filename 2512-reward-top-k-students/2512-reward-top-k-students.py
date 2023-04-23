class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        points = []
        for i in range(len(report)):
            point = 0
            for word in report[i].split():
                if word in positive_feedback:
                    point += 3
                elif word in negative_feedback:
                    point -= 1
            points.append((point, i))
        
        points.sort(key = lambda p : (-p[0], student_id[p[1]]))
        rank = []
        for i in range(min(k, len(points))):
            rank.append(student_id[points[i][1]])
        
        return rank