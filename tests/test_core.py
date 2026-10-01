import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_duplicate_event_rejected(self):
        state = core.new_game()
        self.assertTrue(core.add_event(state, 1, 1, 2))
        self.assertFalse(core.add_event(state, 1, 3, 4))

    def test_02_capacity_rejected(self):
        state = core.new_game()
        self.assertTrue(core.add_event(state, 1, 1, 2))
        self.assertTrue(core.add_event(state, 2, 3, 4))
        self.assertFalse(core.add_event(state, 3, 5, 6))

    def test_03_cancel_removes(self):
        state = core.new_game()
        core.add_event(state, 1, 1, 2)
        core.cancel_event(state, 1)
        self.assertNotIn(1, state["events"])

    def test_04_move_occupied_rejected(self):
        state = core.new_game()
        core.add_event(state, 1, 1, 2)
        core.add_event(state, 2, 3, 4)
        self.assertFalse(core.move_event(state, 2, 1, 2))

    def test_05_overlap_true(self):
        state = core.new_game()
        core.add_event(state, 1, 1, 3)
        core.add_event(state, 2, 2, 4)
        self.assertTrue(core.overlaps(state, 1, 2))

    def test_06_free_slots_count(self):
        state = core.new_game()
        core.add_event(state, 1, 1, 2)
        self.assertEqual(core.free_slots(state), 1)

    def test_07_next_earliest(self):
        state = core.new_game()
        core.add_event(state, 1, 5, 6)
        core.add_event(state, 2, 1, 2)
        self.assertEqual(core.next_event(state), 2)

    def test_08_paused_clock(self):
        state = core.new_game()
        state["paused"] = True
        core.tick(state)
        self.assertEqual(state["clock"], 0)

    def test_09_move_out_of_range_rejected(self):
        state = core.new_game()
        core.add_event(state, 1, 1, 2)
        self.assertFalse(core.move_event(state, 1, -1, 0))

    def test_10_load_preserves_id(self):
        state = core.new_game()
        state["next_id"] = 8
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["next_id"], 8)


if __name__ == "__main__":
    unittest.main()
