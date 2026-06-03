#!/usr/bin/env python3
"""
SingulXR Contact Form Integration Script

This script automatically integrates the Web3Forms contact form
into your bundled index.html file.

Usage:
    python3 integrate-contact-form.py YOUR_WEB3FORMS_ACCESS_KEY

Example:
    python3 integrate-contact-form.py abc123-def456-ghi789
"""

import sys
import re
import html
import shutil
from datetime import datetime

def main():
    # Check for access key argument
    if len(sys.argv) < 2:
        print("❌ Error: Web3Forms Access Key required")
        print("\nUsage:")
        print("  python3 integrate-contact-form.py YOUR_ACCESS_KEY")
        print("\nGet your access key from: https://web3forms.com")
        sys.exit(1)

    access_key = sys.argv[1]

    # Validate access key format (basic check)
    if len(access_key) < 10:
        print("❌ Error: Access key seems invalid (too short)")
        print("Please check your Web3Forms dashboard for the correct key")
        sys.exit(1)

    print("🚀 SingulXR Contact Form Integration")
    print("=" * 50)
    print(f"Access Key: {access_key[:10]}...")
    print()

    # Read the contact form snippet
    print("📖 Reading contact form template...")
    try:
        with open('contact-form-snippet.html', 'r', encoding='utf-8') as f:
            form_html = f.read()
    except FileNotFoundError:
        print("❌ Error: contact-form-snippet.html not found")
        print("Make sure you're running this script from the project directory")
        sys.exit(1)

    # Replace the access key placeholder
    form_html = form_html.replace('YOUR_WEB3FORMS_ACCESS_KEY', access_key)
    print("✓ Access key configured")

    # Read index.html
    print("📖 Reading index.html...")
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ Error: index.html not found")
        sys.exit(1)

    # Check if form already exists
    if 'id="contactForm"' in content or 'id="contact"' in content:
        print("⚠️  Warning: Contact form may already exist in index.html")
        response = input("Continue and replace it? (y/n): ")
        if response.lower() != 'y':
            print("❌ Aborted")
            sys.exit(0)

    # Backup original file
    backup_name = f'index.backup.{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
    print(f"💾 Creating backup: {backup_name}")
    shutil.copy2('index.html', backup_name)
    print(f"✓ Backup created")

    # Find the bundler template section
    print("🔍 Locating template section...")
    match = re.search(r'<script type="__bundler/template">(.*?)</script>', content, re.DOTALL)

    if not match:
        print("❌ Error: Could not find bundler template section")
        print("This file may not be a valid bundled SingulXR HTML file")
        sys.exit(1)

    template_content = match.group(1)
    decoded = html.unescape(template_content)

    print("✓ Template found")

    # Find a good injection point (before </body> in the template)
    if '</body>' in decoded:
        print("📝 Injecting contact form...")

        # Remove any existing contact sections first
        decoded = re.sub(r'<section[^>]*id="contact"[^>]*>.*?</section>', '', decoded, flags=re.DOTALL)

        # Prepare the form HTML (remove comments and extra whitespace for cleaner output)
        form_html_clean = re.sub(r'<!--.*?-->', '', form_html, flags=re.DOTALL)
        form_html_clean = re.sub(r'\n\s*\n', '\n', form_html_clean)

        # Insert before </body>
        modified_template = decoded.replace('</body>', form_html_clean + '\n</body>')

        # Re-encode for the bundle
        print("🔒 Re-encoding template...")
        encoded_template = html.escape(modified_template)

        # Replace in the full content
        modified_content = content.replace(template_content, encoded_template)

        # Write the modified file
        print("💾 Writing updated index.html...")
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(modified_content)

        print()
        print("✅ SUCCESS!")
        print("=" * 50)
        print("✓ Contact form integrated successfully!")
        print(f"✓ Original file backed up to: {backup_name}")
        print()
        print("📋 Next Steps:")
        print("  1. Open index.html in your browser")
        print("  2. Scroll to the bottom to see the contact form")
        print("  3. Test the form with your email")
        print("  4. (Optional) Customize the contact info")
        print()
        print("📖 For customization options, see: CONTACT_FORM_SETUP.md")
        print()

    else:
        print("❌ Error: Could not find </body> tag in template")
        print("Manual integration required - see CONTACT_FORM_SETUP.md")
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
