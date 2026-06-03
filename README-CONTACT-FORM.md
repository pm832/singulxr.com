# Contact Form - Quick Start

## 🚀 Get Started in 3 Minutes

### 1. Get Your Web3Forms Key
Visit [web3forms.com](https://web3forms.com) and sign up (free, no credit card needed). Copy your access key from the dashboard.

### 2. Run the Integration Script
```bash
cd /Users/pavelmakarevich/Documents/singulxr
python3 integrate-contact-form.py YOUR_ACCESS_KEY_HERE
```

### 3. Test It Out
Open `index.html` in your browser and test the form!

---

## 📁 Files Created

| File | Purpose |
|------|---------|
| `contact-form-snippet.html` | Complete contact form HTML + JS + CSS |
| `integrate-contact-form.py` | Automatic integration script |
| `CONTACT_FORM_SETUP.md` | Detailed setup guide |
| `README-CONTACT-FORM.md` | This quick start guide |

---

## ✨ What You Get

✅ **Fully functional contact form** matching your design
✅ **Email notifications** sent directly to your inbox
✅ **Spam protection** with honeypot field
✅ **Loading states** and user feedback
✅ **Mobile responsive** design
✅ **Free forever** (250 submissions/month on free tier)

---

## 🎨 Customization

### Change WhatsApp Number
Edit `contact-form-snippet.html` line 33:
```html
<a href="https://wa.me/19876543210"
```

### Update Contact Person
Edit lines 23-29 with your name and title.

### Add More Fields
Copy this pattern:
```html
<div class="cf-field">
  <span class="mono">Field Label</span>
  <input type="text" name="fieldname" placeholder="Placeholder">
</div>
```

---

## 🔧 Manual Integration

If the script doesn't work:

1. Open `contact-form-snippet.html`
2. Replace `YOUR_WEB3FORMS_ACCESS_KEY` with your key
3. Copy the entire content
4. Paste it before the `</body>` tag in your `index.html`

---

## 📖 Need More Help?

See `CONTACT_FORM_SETUP.md` for:
- Detailed setup instructions
- Troubleshooting guide
- Advanced configuration options
- Alternative form services

---

## ✅ Form Features

- **Name** field (required)
- **Email** field (required)
- **Company** field (optional)
- **Message** textarea (required)
- **Submit** button with loading state
- **Success/error** feedback messages

---

**Ready to go!** Just add your Web3Forms key and start receiving messages.
