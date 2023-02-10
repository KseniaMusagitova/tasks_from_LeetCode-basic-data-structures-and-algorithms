class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_splitted = version1.split(".")
        version2_splitted = version2.split(".")

        len_v1 = len(version1_splitted)
        len_v2 = len(version2_splitted)

        for i in range(max(len_v1, len_v2)):

            version1_number = int(version1_splitted[i]) if i < len_v1 else 0
            version2_number = int(version2_splitted[i]) if i < len_v2 else 0
            if version1_number > version2_number:
                return 1
            elif version1_number < version2_number:
                return -1
        return 0


sol = Solution()


print(sol.compareVersion(version1 = "1", version2 = "1.1"))