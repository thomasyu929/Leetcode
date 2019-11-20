class Solution:
    def compareVersion(self, version1, version2):
        version1 = list(map(int, version1.split('.')))
        # version1 = [int(i) for i in version1.split('.')]
        version2 = list(map(int, version2.split('.')))
        x = len(version1) - len(version2)
        if x > 0:
            version2 = version2 + [0]*x
        else:
            version1 = version1 + [0]*(-x)
        for i in range(len(version1)):
            if version1[i] > version2[i]:
                return 1
            elif version1[i] < version2[i]:
                return -1
        return 0