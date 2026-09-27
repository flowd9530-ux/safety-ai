def process_frame(frame, objects):
    has_person = False
    has_helmet = False
    for obj in objects:
        if obj['class'] == 'person':
            has_person = True
        if obj['class'] == 'helmet':
            has_helmet = True
    if has_person and not has_helmet:
            return frame, [{'type': 'no_helmet', 'message': 'Сотрудник без каски'}]
    else: return frame, []