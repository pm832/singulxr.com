# SingulXR Contact Form Setup Guide

## Overview
This guide will help you integrate the Web3Forms contact form into your SingulXR landing page.

## Quick Setup (3 steps)

### Step 1: Get Your Web3Forms Access Key

1. Go to [https://web3forms.com](https://web3forms.com)
2. Sign up for a free account (no credit card required)
3. Once logged in, you'll see your **Access Key** in the dashboard
4. Copy this key - you'll need it in Step 3

### Step 2: Choose Your Integration Method

#### Option A: Automatic Integration (Recommended)
Run the provided integration script:

```bash
cd /Users/pavelmakarevich/Documents/singulxr
python3 integrate-contact-form.py YOUR_ACCESS_KEY_HERE
```

This will automatically update your `index.html` with the contact form.

#### Option B: Manual Integration
1. Open `contact-form-snippet.html`
2. Find and replace `YOUR_WEB3FORMS_ACCESS_KEY` with your actual access key
3. Copy the entire content
4. Paste it into your React component or HTML before the footer section

### Step 3: Customize (Optional)

#### Update Contact Information
Edit these sections in the contact form:

1. **WhatsApp Link** (line ~33):
   ```html
   <a href="https://wa.me/YOUR_PHONE_NUMBER"
   ```
   Replace `YOUR_PHONE_NUMBER` with your WhatsApp number (include country code, e.g., `19876543210`)

2. **Contact Person Card** (lines ~23-29):
   ```html
   <div class="contact-person">
     <div class="cp-avatar">SX</div>
     <div class="cp-body">
       <b>SingulXR Team</b>
       <em>Innovation Partners</em>
     </div>
   </div>
   ```
   Replace with your actual name, title, or team information.

3. **Section Text** (lines ~18-20):
   Customize the heading and description to match your brand voice.

### Step 4: Test Your Form

1. Open your updated `index.html` in a browser
2. Scroll to the contact section
3. Fill out the form with test data
4. Click "Send Message"
5. Check your email (the one you registered with Web3Forms) for the submission

## Features

✅ **Fully Functional**: Sends emails directly to your inbox via Web3Forms
✅ **Spam Protection**: Includes honeypot field for bot prevention
✅ **Loading States**: Shows spinner and feedback during submission
✅ **Success/Error Messages**: Clear user feedback
✅ **Mobile Responsive**: Works perfectly on all devices
✅ **Styled to Match**: Uses your existing design system CSS
✅ **Free Forever**: Web3Forms free tier includes 250 submissions/month

## How It Works

1. User fills out the contact form
2. JavaScript captures the form submission
3. Data is sent securely to Web3Forms API via HTTPS
4. Web3Forms forwards the email to your inbox
5. User sees success message

## Web3Forms Features

- **No Backend Required**: Pure frontend solution
- **Email Notifications**: Get submissions directly in your email
- **File Uploads**: Support for attachments (can be enabled)
- **Custom Redirects**: Redirect users after submission
- **Webhook Support**: Integrate with other services
- **Spam Filtering**: Built-in spam protection

## Advanced Configuration

### Add More Form Fields

Add new fields by inserting this structure in the form:

```html
<div class="cf-field">
  <span class="mono">Phone</span>
  <input type="tel" name="phone" placeholder="+1 (555) 000-0000">
</div>
```

### Customize Email Subject

Edit the hidden field:
```html
<input type="hidden" name="subject" value="Your Custom Subject">
```

### Add Redirect After Submission

Add this hidden field:
```html
<input type="hidden" name="redirect" value="https://yoursite.com/thank-you">
```

### Enable File Uploads

Add a file input field:
```html
<div class="cf-field">
  <span class="mono">Attachment</span>
  <input type="file" name="attachment" accept=".pdf,.doc,.docx">
</div>
```

## Troubleshooting

### Form Not Sending
- ✓ Check that you've replaced `YOUR_WEB3FORMS_ACCESS_KEY` with your actual key
- ✓ Verify the access key is correct in your Web3Forms dashboard
- ✓ Open browser console (F12) and check for JavaScript errors
- ✓ Make sure you're testing from an actual domain (not `file://`)

### Not Receiving Emails
- ✓ Check your spam folder
- ✓ Verify the email address in your Web3Forms account
- ✓ Check Web3Forms dashboard for submission logs

### Styling Issues
- ✓ Make sure the CSS from your index.html is loading
- ✓ All necessary classes (`.contact-grid`, `.cform`, etc.) are defined in your stylesheet

## Support

- **Web3Forms Documentation**: https://docs.web3forms.com
- **Web3Forms Support**: support@web3forms.com
- **SingulXR Issues**: Check your project repository

## Alternative Services

If Web3Forms doesn't meet your needs, consider:

1. **FormSubmit.co**: Even simpler, no signup needed
2. **EmailJS**: More features, requires account setup
3. **Netlify Forms**: Perfect if you're hosting on Netlify
4. **Custom Backend**: Build your own API endpoint

---

**Need help?** The contact form is ready to go - just add your access key and you're done!
