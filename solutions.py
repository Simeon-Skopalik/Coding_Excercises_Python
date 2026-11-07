from collections import Counter

#Two Sum
def two_sum(nums: list[int], target: int) -> list[int]:
    """Return the indicies of two numbers in nums that add up to target.

    Args:
        nums: List of integers to search
        target: The sum to find
    
    Returns:
        A list of two indices [i,j], with i<j, where
        nums[i] + nums[j] = target
    
    Raises:
        ValueError: If no two numbers sum to target.

    """
    seen= {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
       
        seen[x] = i

    raise ValueError("No two numbers sum to the target")    

### Top K Frequent
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Returns the k most frequent elements in nums.

    Args:
        nums: List of integers to count.
        k: Number of most frequent values to return
        
    Returns:
        The k most frequent values. Oder among values with equal
        counts is not guaranteed. If k exceeds the number of distinct
        values, all distinct values are returned.
    
    """
    counts = Counter(nums) # Count how often each number appears

    k_common = counts.most_common(k)

    values = [value for value, _ in k_common]

    return values
