class Solution {
	public List<Integer> findDisappearedNumbers(int[] nums) {
		boolean[] seen = new boolean[nums.length + 1];
		seen[0] = true;
		for(int num : nums)
			seen[num] = true;	
		List<Integer> missing = new ArrayList<>();
		for(int i = 0; i < seen.length; i++) 
			if(!seen[i])
				missing.add(i); 
		return missing;
	}
}

