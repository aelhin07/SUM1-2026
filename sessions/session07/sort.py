# sort.py

class SortingAlgorithms:
    def sort_one(self, lst):
        """Sort One"""
        for i in range(0, len(lst)-1):
            min_index = i
            for j in range(i+1, len(lst)):  # linearly traverse the unsorted portion
                if lst[j] < lst[min_index]:
                    min_index = j
            # swap the smallest number with the first element in the unsorted region
            lst[i], lst[min_index] = lst[min_index], lst[i]
        return lst

    def sort_two(self, lst):
        """Sort Two"""
        if len(lst) > 1:
            # Split part of the algorithm
            middle = len(lst) // 2  # floor division to find middle of the list
            left_list = lst[:middle]
            right_list = lst[middle:]
            
            # Recursively sort both halves
            self.sort_two(left_list)
            self.sort_two(right_list)
            
            # Merge part of the algorithm
            left_idx = right_idx = merged_idx = 0
            
            while left_idx < len(left_list) and right_idx < len(right_list):
                if left_list[left_idx] < right_list[right_idx]:
                    lst[merged_idx] = left_list[left_idx]
                    left_idx += 1
                else:
                    lst[merged_idx] = right_list[right_idx]
                    right_idx += 1
                merged_idx += 1
            
            # Handle remaining elements
            while left_idx < len(left_list):
                lst[merged_idx] = left_list[left_idx]
                left_idx += 1
                merged_idx += 1
                
            while right_idx < len(right_list):
                lst[merged_idx] = right_list[right_idx]
                right_idx += 1
                merged_idx += 1
                
        return lst

    def sort_three(self, lst):
        """ Sort Three"""
        unsorted_end = len(lst) - 1
        while unsorted_end > 0:
            for i in range(unsorted_end):
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
            unsorted_end -= 1
        return lst


