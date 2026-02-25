title = "Cấu hình CORS"

content = """
CORS (Cross-Origin Resource Sharing) cho phép browser request API từ domain
khác. Cần configure đúng cho web client integration. Mekong Delta Tech config
CORS cho public API.

**Mechanism:** Browser send preflight OPTIONS. Server response CORS headers:
Access-Control-Allow-Origin, Allow-Methods, Allow-Headers. Credentials với
Allow-Credentials. Cache preflight (Access-Control-Max-Age).

**Security:** Don't use * for Allow-Origin khi credentials. Whitelist origin.
Validate Origin header. Different config cho different env. Production
restrictive. Document allowed origins.

**Credentials:** Cookie, auth header require credentials: true. Origin must
be specific, not *. HTTPS. SameSite cookie consideration.

**Troubleshooting:** Preflight fail = check server config. Missing header.
CORS error trong console. Test với curl (no CORS) vs browser. Document CORS
cho integrator.
"""  # noqa: E501

version = "0.0.1"
