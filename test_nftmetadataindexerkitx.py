# test_nftmetadataindexerkitx.py
"""
Tests for NftMetadataIndexerKitX module.
"""

import unittest
from nftmetadataindexerkitx import NftMetadataIndexerKitX

class TestNftMetadataIndexerKitX(unittest.TestCase):
    """Test cases for NftMetadataIndexerKitX class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMetadataIndexerKitX()
        self.assertIsInstance(instance, NftMetadataIndexerKitX)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMetadataIndexerKitX()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
