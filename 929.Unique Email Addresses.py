class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mySet = set()
        for email in emails:
            [local , domain] = email.split("@")
            local = local.replace('.', '')
            local = local.split('+')[0]
            print(local)
            domain = domain.split(".com")[0]
            print(domain)
            mySet.add(local + '@' + domain)

        return len(mySet)
