# Security Policy

## Supported Versions

We provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.0   | :white_check_mark: |
| < 2.0.0 | :x:                |

## Security Best Practices

### Configuration Files

**Never commit or share:**
- `config/password.txt` - Contains account passwords
- `config/5sim_config.txt` - Contains API keys
- `data/accounts.json` - Contains created account details

### API Keys

- Keep 5sim API keys secure
- Don't share API keys publicly
- Rotate API keys regularly
- Use environment variables if possible

### Passwords

- Use strong, unique passwords
- Don't reuse passwords
- Store passwords securely
- Don't share passwords

## Reporting a Vulnerability

If you discover a security vulnerability, please:

1. **Do NOT** create a public GitHub issue
2. Email us at: [Contact through website](https://www.shadowhackr.com)
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We will respond within 48 hours and work with you to resolve the issue.

## Security Updates

Security updates will be:
- Released as soon as possible
- Documented in CHANGELOG.md
- Tagged with security labels

## Responsible Disclosure

We follow responsible disclosure practices:
- We will credit you for reporting vulnerabilities
- We will work with you to fix the issue
- We will not take legal action against security researchers

## Contact

For security concerns:
- Website: https://www.shadowhackr.com
- Facebook: www.facebook.com/ShadowHackr
- WhatsApp: +962796668987

---

**Thank you for helping keep Gmail Creator Pro secure!**

