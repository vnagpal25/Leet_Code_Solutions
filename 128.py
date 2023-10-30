class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # hashing allows for O(1) membership check
        
        longest_seq = 0 # 0 initially

        for num in num_set:
            # we need to start counting from the start not the middle
            if (num - 1) not in num_set:
                seq_len = 0
                while num + seq_len in num_set:
                    seq_len += 1
                longest_seq = max(seq_len, longest_seq)
        return longest_seq
