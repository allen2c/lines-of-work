title = "TLS và mTLS"

content = """
TLS encrypt communication. mTLS (mutual TLS) thêm client certificate — cả hai
bên authenticate. Mekong Delta Tech dùng mTLS cho B2B integration nhạy cảm.

**TLS Basics:** Server cert, CA chain. TLS 1.2 minimum, prefer 1.3. Strong
cipher. Certificate validity. OCSP stapling. HSTS header.

**mTLS Flow:** Client có certificate. Server validate client cert. Extract
identity từ cert (CN, SAN). Use for authorization. Cert = credential.

**Certificate Management:** Issuance, renewal, revocation. Internal CA hoặc
public CA. Automated renewal (Let's Encrypt, cert-manager). Store cert securely.
Rotate before expiry. Revocation list khi compromise.

**Integration:** Client SDK support mTLS. Load cert from file/vault. Server
config require client auth. Document cert requirement. Onboarding flow cho
cert exchange.
"""  # noqa: E501

version = "0.0.1"
