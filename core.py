import json


def new_game():
    return {"events": {}, "cap": 2, "paused": False, "clock": 0, "next_id": 1}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["next_id"] += 1
    return state


def add_event(state, eid, start, end):
    state["events"][eid] = (start, end)
    return True


def cancel_event(state, eid):
    return True


def move_event(state, eid, start, end):
    state["events"][eid] = (start, end)
    return True


def overlaps(state, a, b):
    start_a, end_a = state["events"][a]
    start_b, end_b = state["events"][b]
    return end_a <= start_b or end_b <= start_a


def free_slots(state):
    return len(state["events"]) - 1


def next_event(state):
    return max(state["events"].items(), key=lambda item: item[1][0])[0]


def tick(state):
    state["clock"] += 1
    return state["clock"]


def main():
    print("命令: add/cancel/move/overlaps/free/next/tick/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
