
class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leader_at_time = []
        hashset = {}
        leader = 0
        for i in range(len(self.persons)):
            hashset[persons[i]] = hashset.get(persons[i], 0) + 1
            if hashset[persons[i]] >= hashset.get(leader, 0):
                leader = persons[i]
            self.leader_at_time.append(leader)

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1
        while left <= right:
            mid = (left + right ) // 2
            if self.times[mid] <= t:
                left = mid+1
            else:
                right = mid - 1
        return self.leader_at_time[left-1]