import os

def find_duplicates(base_dir):
    """
    This function checks for duplicate files in corresponding + and - directories.
    """
    # Loop through problem numbers from 0 to 6
    for i in range(7):
        plus_dir = os.path.join(base_dir, f"{i}+")
        minus_dir = os.path.join(base_dir, f"{i}-")
        
        # Collect all files in each directory
        if os.path.exists(plus_dir) and os.path.exists(minus_dir):
            plus_files = set(os.listdir(plus_dir))
            minus_files = set(os.listdir(minus_dir))
            
            # Find intersection of file sets
            duplicates = plus_files & minus_files
            
            if duplicates:
                print(f"Duplicate files found between {i}+ and {i}-: {duplicates}")
            else:
                print(f"No duplicates found between {i}+ and {i}-")
        else:
            print(f"Directories {i}+ or {i}- not found. Skipping...")

def main():
    # Set the path to the base directory containing all the data
    base_dir = "."
    find_duplicates(base_dir)

if __name__ == "__main__":
    main()
