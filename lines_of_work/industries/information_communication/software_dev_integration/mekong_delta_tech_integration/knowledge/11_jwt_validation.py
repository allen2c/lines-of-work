title = "Xác thực JWT"

content = """
JWT (JSON Web Token) được dùng rộng rãi cho stateless authentication. Validation đúng
cách là bắt buộc để tránh security vulnerability.

**Signature Verification:** Luôn verify signature trước khi tin payload. Dùng public key
hoặc secret từ issuer. Không trust alg in header — enforce expected algorithm (chống alg
confusion attack).

**Claims Validation:** Kiểm tra exp (expiration), iat (issued at), nbf (not before).
Validate aud (audience) và iss (issuer) nếu dùng. Reject token invalid hoặc expired.

**Key Management:** Public keys từ JWKS endpoint hoặc config. Cache với TTL ngắn. Rotate
keys theo policy. Không hardcode secret trong code.

**Token Storage (Client):** HttpOnly cookie cho web (chống XSS) hoặc secure storage
mobile. Không lưu trong localStorage khi có XSS risk. Token trong memory cho SPA.
"""  # noqa: E501

version = "0.0.1"
