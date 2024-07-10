def read_file(filename):
    exclude_message = "Scraped by Kyanite - https://idiotide.sellix.io/"
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip() != exclude_message]


def write_combos(usernames, passwords, output_filename):
    with open(output_filename, 'w') as file:
        for username in usernames:
            for password in passwords:
                file.write(f"{username}:{password}\n")

def main():
    usernames = read_file('usernames.txt')
    passwords = read_file('passwords.txt')
    write_combos(usernames, passwords, 'combos.txt')
    total_combos = len(usernames) * len(passwords)
    input(f"[+] {total_combos}/{total_combos} Combos were made")

if __name__ == "__main__":
    main()
