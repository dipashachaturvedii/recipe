# import unittest
# from scrapers.scraper import parse, extract, parse_result

# class ScraperTestCase(unittest.TestCase):
#     def test_parse(self):
#         # Test the parse function
#         page_source = "<html><body><article class='post-summary primary'>...</article></body></html>"
#         result = parse(page_source)
#         self.assertIsInstance(result, dict)
#         self.assertGreater(len(result), 0)

#     def test_extract(self):
#         # Test the extract function
#         article = "<article class='post-summary primary'>...</article>"
#         result = extract(article)
#         self.assertIsInstance(result, dict)
#         self.assertEqual(len(result), 1)
#         self.assertIn(0, result)

#     def test_parse_result(self):
#         # Test the parse_result function
#         article = "<article class='post-summary primary'>...</article>"
#         result = parse_result(article)
#         self.assertIsInstance(result, dict)
#         self.assertGreater(len(result), 0)
#         self.assertIn("name", result)
#         self.assertIn("category", result)
#         # Add more assertions based on the expected output of parse_result

# if __name__ == '__main__':
#     unittest.main()
