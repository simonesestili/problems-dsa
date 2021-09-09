class Solution:
	def angleClock(self, hour: int, minutes: int) -> float:
		hour %= 12
		hour_angle = (hour * 30) + (minutes / 2)
		minute_angle = minutes * 6
		return min( abs(hour_angle - minute_angle), abs(360 - max(minute_angle, hour_angle) + min(hour_angle, minute_angle)))
