class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_e = {}
        for email in emails:
            [local, domain] = email.split('@')
            domain = '@' + domain
            local = local.split('+')[0]
            # local = ''.join(local.split('.'))
            local = local.replace('.', '')  # replace is more efficient
            unique_e[local + domain] = 1

        return len(unique_e.keys())

sol = Solution()

print(sol.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))