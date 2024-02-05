# Startup info
echo "Installing GLauncher"
echo "Project can be found here: https://github.com/HttpAnimation/GLauncher"

# Git clone the branch stable
echo "Downloading the repo"
git clone -b https://github.com/HttpAnimation/GLauncher
echo "Done downloading the repo"

# Cd the repo
echo "Heading into the repo"
cd GLauncher
echo "Done heading into the repo"

# Remove extra files
echo "Removing extra / unsed files"
echo "Removing README.md"
rm README.md
echo "Done removing the readme"
echo "Removes configs/README.md"
rm configs/README.md
echo "Removing configs/README.md"
