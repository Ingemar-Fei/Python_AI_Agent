import unittest
import functions.get_files_info as gfi

class TestGetFilesInfo(unittest.TestCase):
    def test_get_files_content(self):
        test_set = [{
            'working_directory':'calculator',
            'file':'main.py',
        },{
            'working_directory':'calculator',
            'file':'pkg/calculator.py',
        },{
            'working_directory':'calculator',
            'file':'/bin/cat',
        }]

        for test_case in test_set:
            print(gfi.get_file_content(test_case['working_directory'], test_case['file']))

if  __name__ == '__main__':
    unittest.main()