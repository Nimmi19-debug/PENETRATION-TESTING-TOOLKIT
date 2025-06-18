
def brute_force(username, passwords, correct_password="admin123"):
    attempts = []
    for pwd in passwords:
        if pwd == correct_password:
            return {"success": True, "username": username, "password": pwd, "attempts": attempts}
        attempts.append(pwd)
    return {"success": False, "username": username, "attempts": attempts}
