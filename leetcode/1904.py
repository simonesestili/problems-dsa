class Solution:     
	def numberOfRounds(self, startTime: str, finishTime: str) -> int:         
		startTime, finishTime = self.parseTime(startTime), self.parseTime(finishTime)
        if finishTime < startTime:
            finishTime += 24
        startTime, finishTime = self.roundUp(startTime), self.roundDown(finishTime)
        games = int((finishTime - startTime) * 4)
        return games if games > 0 else 0

    def roundUp(self, n):
        whole, decimal = int(n), n % (1 if not int(n) else int(n)) 
        if decimal == 0:
            return whole
        if decimal <= 0.25:
            return whole + 0.25
        if decimal <= 0.5:
            return whole + 0.5
        if decimal <= 0.75:
            return whole + 0.75
        return whole + 1 

    def roundDown(self, n):
        whole, decimal = int(n), n % (1 if not int(n) else int(n))
        if decimal >= 0.75:
            return whole + 0.75
        if decimal >= 0.5:
            return whole + 0.5
        if decimal >= 0.25:
            return whole + 0.25
        return whole

    def parseTime(self, time):
        return int(time[:2]) + int(time[3:]) / 60
