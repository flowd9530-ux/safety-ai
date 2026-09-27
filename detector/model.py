helmet = {'class': 'helmet', 'conf': 0.8, "box": [140, 50, 210, 110]}
person = {'class': 'person', 'conf': 0.9, 'box' : [100, 50, 250, 400]}
def detect(frame):
    if frame % 2 == 0:
        return [person, helmet]
    else:
        return [person]