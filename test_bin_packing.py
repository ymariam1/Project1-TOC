"""
Test cases for Bin Packing Backtracking Implementation
"""
import pytest
import tempfile
import os
from src.bin_packing import BinPacking


class TestBinPackingBacktracking:
    """Test suite for bin packing backtracking algorithm"""
    
    @pytest.fixture
    def packer(self):
        """Create a BinPacking instance with a temporary file"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("10 2 8\n")  # Dummy data, we'll use direct method calls
            temp_file = f.name
        
        packer = BinPacking(temp_file, result_file_name="test_results")
        yield packer
        
        # Cleanup
        if os.path.exists(temp_file):
            os.remove(temp_file)
    
    def test_simple_case(self, packer):
        """Test Case 1: Simple case with two items that sum to capacity"""
        bin_capacity = 10
        items = [2, 8]
        
        result = packer.binpacking_backtracing(bin_capacity, items)
        print(f"\nCapacity: {bin_capacity}")
        print(f"Items: {items}")
        print(f"Solutions found: {result}")
        
        assert len(result) == 1, "Should find exactly 1 solution"
        assert [2, 8] in result, "Should find [2, 8]"
        
    def test_multiple_solutions(self, packer):
        """Test Case 2: Multiple valid combinations"""
        bin_capacity = 10
        items = [2, 5, 4, 7, 1, 3, 8, 6]
        
        result = packer.binpacking_backtracing(bin_capacity, items)
        print(f"\nCapacity: {bin_capacity}")
        print(f"Items: {items}")
        print(f"Number of solutions: {len(result)}")
        print(f"Solutions found:")
        for sol in result:
            print(f"  {sol} -> sum = {sum(sol)}")
        
        for solution in result:
            assert sum(solution) == bin_capacity, f"Solution {solution} doesn't sum to {bin_capacity}"
        
        assert [2, 8] in result, "Should find [2, 8]"
        assert [3, 7] in result, "Should find [3, 7]"
        assert [4, 6] in result, "Should find [4, 6]"
        assert len(result) == 8, f"Should find 8 solutions, but found {len(result)}"
        
    def test_no_solution(self, packer):
        """Test Case 3: No valid combination exists"""
        bin_capacity = 15
        items = [2, 3, 4, 5]
        
        result = packer.binpacking_backtracing(bin_capacity, items)
        print(f"\nCapacity: {bin_capacity}")
        print(f"Items: {items}")
        print(f"Solutions found: {result}")
        
        assert len(result) == 0, "Should find no solutions"

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])

