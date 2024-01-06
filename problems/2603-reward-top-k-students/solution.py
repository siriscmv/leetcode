from collections import defaultdict

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
      scores = defaultdict(int)
      for w in positive_feedback: scores[w] = 3
      for w in negative_feedback: scores[w] = -1

      students = [(sum([scores[w] for w in r.split(' ')]), i) for i, r in zip(student_id, report)]
      students.sort(key=lambda s: (-1 * s[0], s[1]))
      return list(map(lambda s: s[1], students))[:k]
