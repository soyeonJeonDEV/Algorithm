#https://programmers.co.kr/learn/courses/30/lessons/12901
#2016년
import datetime
def solution(a,b):
    weekday_list = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    weekday_info = datetime.datetime(2016,a,b).weekday()

    answer = weekday_list[weekday_info]

    return answer