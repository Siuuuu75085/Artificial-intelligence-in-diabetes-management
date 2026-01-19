from werkzeug.security import generate_password_hash,check_password_hash
USERS={
"admin":{"password":generate_password_hash("admin123"),"role":"admin"},
"doctor":{"password":generate_password_hash("doctor123"),"role":"doctor"}
}
def authenticate(u,p):
    if u in USERS and check_password_hash(USERS[u]["password"],p):
        return {"username":u,"role":USERS[u]["role"]}
