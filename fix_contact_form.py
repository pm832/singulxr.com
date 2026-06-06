#!/usr/bin/env python3
"""
Fix the SingulXR contact form.

The form is a React component bundled (gzip+base64) inside the
__bundler/manifest asset dc1de9c2-...  It must be patched THERE — editing the
__bundler/template never affects the rendered form.

Changes:
  * Company field  -> Email field (type=email, required)
  * WhatsApp window.open submit -> fetch POST to Web3Forms
"""
import re, json, base64, gzip

INDEX = 'index.html'
ASSET_UUID = 'dc1de9c2-63d1-465e-b453-0989a2af2c07'
WEB3FORMS_KEY = '0161a224-36b5-4911-af23-cf99c8207678'

OLD_COMPONENT = '''function ContactForm() {
  const [sent, setSent] = useState(false);
  const submit = (e) => {
    e.preventDefault();
    const f = e.currentTarget;
    const company = encodeURIComponent(f.company.value || '—');
    const name = encodeURIComponent(f.name.value || '—');
    const msg = encodeURIComponent(f.message.value || '');
    // route through WhatsApp so the message reaches Pavel directly
    const text = `Hi SingulXR, I'm ${decodeURIComponent(name)} from ${decodeURIComponent(company)}.%0A%0A${msg}`;
    window.open(`${WA}?text=${text}`, '_blank');
    setSent(true);
    void company; void msg;
  };
  return (
    <form className="cform" onSubmit={submit}>
      <div className="cf-row">
        <label className="cf-field">
          <span>Company</span>
          <input name="company" type="text" placeholder="Acme Corp" autoComplete="organization" />
        </label>
        <label className="cf-field">
          <span>Name</span>
          <input name="name" type="text" placeholder="Your name" autoComplete="name" required />
        </label>
      </div>
      <label className="cf-field">
        <span>How can we help?</span>
        <textarea name="message" rows="4" placeholder="Tell us the KPI you want to move, or the problem you're exploring…" required></textarea>
      </label>
      <button type="submit" className="btn btn-primary" onClick={ripple}>
        {sent ? 'Opening WhatsApp…' : 'Send message'} <span aria-hidden="true">→</span>
      </button>
    </form>
  );
}'''

NEW_COMPONENT = '''function ContactForm() {
  const [status, setStatus] = useState('idle');
  const submit = async (e) => {
    e.preventDefault();
    const f = e.currentTarget;
    setStatus('sending');
    const payload = {
      access_key: 'WEB3FORMS_KEY',
      subject: 'New Contact Form Submission from SingulXR',
      from_name: 'SingulXR Website',
      name: f.name.value || '',
      email: f.email.value || '',
      message: f.message.value || ''
    };
    try {
      const res = await fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      if (data.success) { setStatus('sent'); f.reset(); }
      else setStatus('error');
    } catch (err) {
      setStatus('error');
    }
  };
  const label = status === 'sending' ? 'Sending…'
    : status === 'sent' ? 'Message sent ✓'
    : status === 'error' ? 'Failed — try again'
    : 'Send message';
  return (
    <form className="cform" onSubmit={submit}>
      <div className="cf-row">
        <label className="cf-field">
          <span>Name</span>
          <input name="name" type="text" placeholder="Your name" autoComplete="name" required />
        </label>
        <label className="cf-field">
          <span>Email</span>
          <input name="email" type="email" placeholder="you@company.com" autoComplete="email" required />
        </label>
      </div>
      <label className="cf-field">
        <span>How can we help?</span>
        <textarea name="message" rows="4" placeholder="Tell us the KPI you want to move, or the problem you're exploring…" required></textarea>
      </label>
      <button type="submit" className="btn btn-primary" onClick={ripple} disabled={status === 'sending'}>
        {label} <span aria-hidden="true">→</span>
      </button>
    </form>
  );
}'''.replace('WEB3FORMS_KEY', WEB3FORMS_KEY)


def main():
    with open(INDEX, 'r', encoding='utf-8') as fh:
        content = fh.read()

    mm = re.search(r'<script type="__bundler/manifest">\s*(.*?)\s*</script>',
                   content, re.DOTALL)
    manifest = json.loads(mm.group(1))
    entry = manifest[ASSET_UUID]

    old_b64 = entry['data']
    src = gzip.decompress(base64.b64decode(old_b64)).decode('utf-8')

    if OLD_COMPONENT not in src:
        print('ERROR: original ContactForm block not found — aborting.')
        return 1

    new_src = src.replace(OLD_COMPONENT, NEW_COMPONENT)
    assert 'name="company"' not in new_src, 'company field still present!'
    assert 'window.open(`${WA}?text' not in new_src, 'WhatsApp submit still present!'
    assert 'api.web3forms.com/submit' in new_src, 'web3forms endpoint missing!'

    # Re-gzip (mtime=0 for deterministic output) and re-base64
    new_bytes = gzip.compress(new_src.encode('utf-8'), mtime=0)
    new_b64 = base64.b64encode(new_bytes).decode('ascii')

    # Patch the base64 string in-place (unique within the file)
    assert content.count(old_b64) == 1, 'asset data not uniquely found'
    content = content.replace(old_b64, new_b64)

    with open(INDEX, 'w', encoding='utf-8') as fh:
        fh.write(content)

    print('✓ Patched ContactForm in asset', ASSET_UUID)
    print('  - Company field -> Email field')
    print('  - WhatsApp submit -> Web3Forms fetch POST')
    print(f'  - asset size {len(old_b64)} -> {len(new_b64)} (base64 chars)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
