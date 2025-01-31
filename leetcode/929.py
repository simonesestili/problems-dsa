class Solution:
    def numUniqueEmails(self, emails) -> int:
        uniqueMail = set()
        for email in emails:
            uniqueMail.add(self.fix(email))
        return len(uniqueMail)    

    def fix(self, email: str) -> str:
        local, domain = email.split('@')
        local = local.replace('.', '').split('+')[0]
        return f'{local}@{domain}'
