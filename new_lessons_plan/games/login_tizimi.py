users = {
    "admin": "1234",
    "user": "abcd"
}

login = input("Login: ")
password = input("Parol: ")

if login in users and users[login] == password:
    print("✅ Xush kelibsiz,", login)
else:
    print("❌ Login yoki parol noto‘g‘ri")



