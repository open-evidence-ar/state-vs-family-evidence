#!/bin/bash
# Generate PGP key pair for State vs Family Evidence project
# Run this ONCE to create the signing key

echo "Generating PGP key for 'State vs Family Evidence'..."
echo "This key will be used to sign document builds and verify authenticity."
echo ""

# Generate the key (non-interactive)
gpg --batch --gen-key <<EOF
%no-protection
Key-Type: RSA
Key-Length: 4096
Name-Real: State vs Family Evidence
Name-Email: state-vs-family-evidence@protonmail.com
Expire-Date: 0
%commit
EOF

# Export public key
gpg --armor --export "State vs Family Evidence" > public.pem
echo ""
echo "Public key exported to public.pem"

# Export private key (for GitHub Actions secret)
gpg --armor --export-secret-keys "State vs Family Evidence" > private-key.asc
echo "Private key exported to private-key.asc"
echo ""
echo "IMPORTANT: Add the private key to GitHub Secrets as GPG_PRIVATE_KEY"
echo "Then delete private-key.asc after adding to secrets!"
echo ""
echo "To sign a build:"
echo "  gpg --armor --detach-sign --default-key 'State vs Family Evidence' _site/index.html"
echo "  mv _site/index.html.asc _site/signature"