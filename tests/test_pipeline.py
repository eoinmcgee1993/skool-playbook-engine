import unittest
from engine.pipeline import deduplicate

class PipelineTests(unittest.TestCase):
    def test_dedup_preserves_provenance(self):
        a={"title":"A","claim":"Same","source_locator":"lesson-1"}
        b={"title":"A","claim":"Same","source_locator":"lesson-2"}
        result=deduplicate([a,b])
        self.assertEqual(len(result),1)
        self.assertEqual(set(result[0]["source_locator"]),{"lesson-1","lesson-2"})

if __name__ == "__main__":
    unittest.main()
