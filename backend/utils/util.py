from flask import Flask, request, jsonify
from jose import jwt
from jose.exceptions import JWTError
import requests
from functools import wraps

AUTH0_DOMAIN = "dev-vwmcthm72y47461e.us.auth0.com"
API_AUDIENCE = "https://dev-vwmcthm72y47461e.us.auth0.com/api/v2/"
ALGORITHMS = ["RS256"]

app = Flask(__name__)

def get_jwks():
    jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
    return requests.get(jwks_url).json()["keys"]

def get_public_key(token):
    unverified_header = jwt.get_unverified_header(token)
    for key in get_jwks():
        if key["kid"] == unverified_header["kid"]:
            return {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    raise Exception("Public key not found.")

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("Authorization", None)
        if not auth:
            return jsonify({"error": "Authorization header is expected"}), 401

        parts = auth.split()
        if parts[0].lower() != "bearer" or len(parts) != 2:
            return jsonify({"error": "Invalid auth header"}), 401

        token = parts[1]
        try:
            public_key = get_public_key(token)
            payload = jwt.decode(
                token,
                public_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f"https://{AUTH0_DOMAIN}/"
            )
        except JWTError as e:
            return jsonify({"error": "Invalid token", "details": str(e)}), 401
        
        kwargs['subject'] = payload['sub']

        return f(*args, **kwargs)
    return decorated


