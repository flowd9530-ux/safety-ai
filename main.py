from detector.model import detect
from detector.rules import process_frame
from backend.db import save_event
for frame in range(1, 11):
    objects = detect(frame)
    frame, events = process_frame(frame, objects)
    for event in events:
        save_event(event, frame)