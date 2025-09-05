#!/usr/bin/env python3
"""Test script to reproduce the import issue."""

def test_basic_import():
    """Test basic shotgun_api3 import."""
    print("Testing basic import...")
    import shotgun_api3
    print("✓ import shotgun_api3 - SUCCESS")
    
def test_lib_import():
    """Test lib module imports that were failing."""
    print("Testing lib imports...")
    from shotgun_api3.lib import sgutils
    print("✓ from shotgun_api3.lib import sgutils - SUCCESS")
    
def test_shotgun_class():
    """Test that we can instantiate the main class."""
    print("Testing Shotgun class...")
    import shotgun_api3
    # Don't actually connect, just test instantiation
    sg = shotgun_api3.Shotgun("http://test.com", "test", "test", connect=False)
    print("✓ Shotgun class instantiation - SUCCESS")
    
if __name__ == "__main__":
    print("=" * 50)
    print("Testing shotgun_api3 installation from git...")
    print("=" * 50)
    
    try:
        test_basic_import()
        test_lib_import() 
        test_shotgun_class()
        print("\n🎉 All tests passed!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
