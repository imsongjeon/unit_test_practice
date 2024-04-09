

def is_valid_email(email):
    if email.count('@') != 1:
        return False
    username, domain = email.split('@')
    if not username:
        return False

    if domain[0] in ['.', '-'] or domain[-1] in ['.', '-']:
        return False
    for i in range(len(domain) - 1):
        if domain[i] in ['_', '.', '-'] and not domain[i+1].isalnum():
            return False
    if domain == 'localhost':
        return True
    if domain.count('.') == 0:
        return False
    domain_elemtents = domain.split('.')
    # Allowed characters: letters, numbers, dashes for domain
    for element in domain_elemtents:
        if not element.isalnum() and '-' not in element:
            return False
    # The last portion of the domain must be at least two characters
    if len(domain_elemtents[-1]) < 2:
        return False
    return True

if __name__ == '__main__':
    email = 'abc.@mail.com'
    print(is_valid_email(email))