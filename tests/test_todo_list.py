"""
Unit tests for the To-Do List application.
"""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import todo_list


class TestTodoList(unittest.TestCase):

    def setUp(self):
        """Set up a temporary tasks file for each test."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.tasks_file = Path(self.temp_dir.name) / "tasks.json"
        todo_list.TASKS_FILE = self.tasks_file

    def tearDown(self):
        """Clean up the temporary directory."""
        self.temp_dir.cleanup()

    # ---------- load_tasks / save_tasks ----------

    def test_load_tasks_returns_empty_list_when_file_missing(self):
        tasks = todo_list.load_tasks()
        self.assertEqual(tasks, [])

    def test_save_and_load_tasks_roundtrip(self):
        tasks = [{"description": "Test task", "completed": False}]
        todo_list.save_tasks(tasks)
        loaded = todo_list.load_tasks()
        self.assertEqual(loaded, tasks)

    def test_load_tasks_handles_corrupt_file(self):
        self.tasks_file.write_text("not valid json {", encoding="utf-8")
        tasks = todo_list.load_tasks()
        self.assertEqual(tasks, [])

    # ---------- add_task ----------

    @patch("builtins.input", return_value="Buy milk")
    @patch("builtins.print")
    def test_add_task_appends_task(self, mock_print, mock_input):
        tasks = []
        todo_list.add_task(tasks)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Buy milk")
        self.assertFalse(tasks[0]["completed"])

    @patch("builtins.input", return_value="   ")
    @patch("builtins.print")
    def test_add_task_rejects_empty_description(self, mock_print, mock_input):
        tasks = []
        todo_list.add_task(tasks)
        self.assertEqual(len(tasks), 0)

    # ---------- edit_task ----------

    @patch("builtins.input", side_effect=["1", "Updated task"])
    @patch("builtins.print")
    def test_edit_task_updates_description(self, mock_print, mock_input):
        tasks = [{"description": "Old task", "completed": False}]
        todo_list.edit_task(tasks)
        self.assertEqual(tasks[0]["description"], "Updated task")

    # ---------- remove_task ----------

    @patch("builtins.input", return_value="1")
    @patch("builtins.print")
    def test_remove_task_deletes_task(self, mock_print, mock_input):
        tasks = [{"description": "To remove", "completed": False}]
        todo_list.remove_task(tasks)
        self.assertEqual(len(tasks), 0)

    # ---------- complete_task ----------

    @patch("builtins.input", return_value="1")
    @patch("builtins.print")
    def test_complete_task_marks_as_completed(self, mock_print, mock_input):
        tasks = [{"description": "Task", "completed": False}]
        todo_list.complete_task(tasks)
        self.assertTrue(tasks[0]["completed"])

    # ---------- get_task_index ----------

    @patch("builtins.input", return_value="99")
    @patch("builtins.print")
    def test_get_task_index_rejects_out_of_range(self, mock_print, mock_input):
        tasks = [{"description": "Task", "completed": False}]
        result = todo_list.get_task_index(tasks, "Enter number: ")
        self.assertIsNone(result)

    @patch("builtins.input", return_value="abc")
    @patch("builtins.print")
    def test_get_task_index_rejects_non_integer(self, mock_print, mock_input):
        tasks = [{"description": "Task", "completed": False}]
        result = todo_list.get_task_index(tasks, "Enter number: ")
        self.assertIsNone(result)

    # ---------- view_tasks ----------

    @patch("builtins.print")
    def test_view_tasks_with_empty_list(self, mock_print):
        todo_list.view_tasks([])
        mock_print.assert_called_with("No tasks in the list.")

    # ---------- search_tasks ----------

    @patch("builtins.input", return_value="code")
    @patch("builtins.print")
    def test_search_tasks_finds_matching(self, mock_print, mock_input):
        tasks = [
            {"description": "write code", "completed": False},
            {"description": "buy milk", "completed": False},
        ]
        todo_list.search_tasks(tasks)
        # Verify "Search results:" was printed (indicates a match was found)
        printed_output = " ".join(str(call) for call in mock_print.call_args_list)
        self.assertIn("Search results", printed_output)


if __name__ == "__main__":
    unittest.main()