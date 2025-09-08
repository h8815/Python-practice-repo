def main():
    import random
    import string
    from datetime import datetime

    users = ["jethalal", "gulabo", "babita"]

    def generate_password(length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))

    # Timestamp header
    timestamp = datetime.now().strftime("\n\n>>>> On date: %a %b %d 00:00:01 AM IST %Y")
    output = f"{timestamp}\n"

    # Generate user passwords
    for user in users:
        password = generate_password()
        output += (
            f"✅ Password changed for {user} \n"
            f"🔑 Password: ({password})\n"
            f"📧 Email sent to {user} \n\n"
        )

    output += "Password change and email notification completed."
    return output
