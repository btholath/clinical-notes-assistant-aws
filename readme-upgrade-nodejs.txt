Upgrade Node.js

Recommended: Upgrade Node.js
You have a few options:
Option 1: Using nvm (Node Version Manager) - Recommended
bash# Install nvm if you don't have it
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# Restart terminal or run:
source ~/.bashrc

# Install and use Node.js 20
nvm install 20
nvm use 20

# Verify
node --version
Option 2: Using NodeSource (system-wide)
bash# Add NodeSource repository for Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -

# Install Node.js
sudo apt-get install -y nodejs

# Verify
node --version