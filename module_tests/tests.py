"""
Test cases for Bin Packing Backtracking Implementation
"""
import pytest
from src.bin_packing import BinPacking
from src.helpers.bin_packing_helper import backtrack_subset_sum


class TestBinPackingBacktracking:
    """Test suite for bin packing backtracking algorithm"""
    
    def test_simple_case(self):
        """Test Case 1: Simple case with two items that sum to capacity"""
        print("\n=== Test 1: Simple Case ===")
        bin_capacity = 10
        items = [2, 8]
        
        result = backtrack_subset_sum(bin_capacity, items)
        print(f"Capacity: {bin_capacity}")
        print(f"Items: {items}")
        print(f"Solutions found: {result}")
        
        assert len(result) == 1, "Should find exactly 1 solution"
        assert [2, 8] in result, "Should find [2, 8]"
        
    def test_multiple_solutions(self):
        """Test Case 2: Multiple valid combinations"""
        print("\n=== Test 2: Multiple Solutions ===")
        bin_capacity = 10
        items = [2, 5, 4, 7, 1, 3, 8, 6]
        
        result = backtrack_subset_sum(bin_capacity, items)
        print(f"Capacity: {bin_capacity}")
        print(f"Items: {items}")
        print(f"Number of solutions: {len(result)}")
        print(f"Solutions found:")
        for sol in result:
            print(f"  {sol} -> sum = {sum(sol)}")
        
        # Verify all solutions sum to bin_capacity
        for solution in result:
            assert sum(solution) == bin_capacity, f"Solution {solution} doesn't sum to {bin_capacity}"
        
        # Check for some expected solutions
        assert [2, 8] in result, "Should find [2, 8]"
        assert [3, 7] in result, "Should find [3, 7]"
        assert [4, 6] in result, "Should find [4, 6]"
        assert len(result) == 8, "Should find 8 solutions"
        
    def test_no_solution(self):
        """Test Case 3: No valid combination exists"""
        print("\n=== Test 3: No Solution ===")
        bin_capacity = 15
        items = [2, 3, 4, 5]
        
        result = backtrack_subset_sum(bin_capacity, items)
        print(f"Capacity: {bin_capacity}")
        print(f"Items: {items}")
        print(f"Solutions found: {result}")
        
        assert len(result) == 0, "Should find no solutions"
        
    def test_exact_match_single_item(self):
        """Test Case 4: Single item equals capacity"""
        print("\n=== Test 4: Single Item Exact Match ===")
        bin_capacity = 10
        items = [10, 5, 3, 2]
        
        result = backtrack_subset_sum(bin_capacity, items)
        print(f"Capacity: {bin_capacity}")
        print(f"Items: {items}")
        print(f"Solutions found: {result}")
        
        # Verify all solutions sum to bin_capacity
        for solution in result:
            assert sum(solution) == bin_capacity, f"Solution {solution} doesn't sum to {bin_capacity}"
        
        assert [10] in result, "Should find [10]"
        assert [2, 3, 5] in result, "Should find [2, 3, 5]"
        

class TestBinPackingIntegration:
    """Integration tests using the BinPacking class"""
    
    def test_bin_packing_class(self):
        """Test Case 5: Test through BinPacking class"""
        print("\n=== Test 5: Integration Test ===")
        
        # Create a temporary test input file
        import tempfile
        import os
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("15 3 5 7 8 10\n")
            f.write("20 5 10 7 3 15\n")
            temp_file = f.name
        
        try:
            # Create BinPacking instance
            packer = BinPacking(temp_file, result_file_name="test_results")
            
            # Test first instance: capacity=15, items=[3,5,7,8,10]
            result1 = packer.binpacking_backtracing(15, [3, 5, 7, 8, 10])
            print(f"\nInstance 1 - Capacity: 15, Items: [3, 5, 7, 8, 10]")
            print(f"Solutions: {result1}")
            
            # Verify all solutions sum correctly
            for solution in result1:
                assert sum(solution) == 15, f"Solution {solution} doesn't sum to 15"
            
            # Test second instance: capacity=20, items=[5,10,7,3,15]
            result2 = packer.binpacking_backtracing(20, [5, 10, 7, 3, 15])
            print(f"\nInstance 2 - Capacity: 20, Items: [5, 10, 7, 3, 15]")
            print(f"Solutions: {result2}")
            
            # Verify all solutions sum correctly
            for solution in result2:
                assert sum(solution) == 20, f"Solution {solution} doesn't sum to 20"
            
            print(f"\nTotal solutions for instance 1: {len(result1)}")
            print(f"Total solutions for instance 2: {len(result2)}")
            
        finally:
            # Clean up temp file
            if os.path.exists(temp_file):
                os.remove(temp_file)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])

