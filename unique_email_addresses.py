# 929. Unique Email Addresses
# https://leetcode.com/problems/unique-email-addresses/

def numUniqueEmails(emails: List[str]) -> int:
  def normalize(email: str) -> str:
    local, domain = email.split("@")
    local = local.replace(".", "")
    return local.split("+")[0] + "@" + domain

  return len({normalize(email) for email in emails})
