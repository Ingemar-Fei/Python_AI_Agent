import unittest
import functions.get_files_info as gfi
import functions.get_file_content as gfc
import functions.write_file as wf
import functions.run_python as rp

class TestGetFilesInfo(unittest.TestCase):
    def test_get_files_content(self):
        test_set = [{
            'working_directory':'calculator',
            'file':'main.py',
        },{
            'working_directory':'calculator',
            'file':'tests.py',
        },{
            'working_directory':'calculator',
            'file':'../main.py',
        },{
            'working_directory':'calculator',
            'file':'nonexistent.py',
        },{
            'working_directory':'calculator',
            'file':'nonexistent_file',
        }]

        for test_case in test_set:
            print(rp.run_python_file(test_case['working_directory'], test_case['file']))

if  __name__ == '__main__':
    unittest.main()