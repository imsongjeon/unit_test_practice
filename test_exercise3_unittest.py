import unittest
import psycopg2

from unittest.mock import patch, MagicMock
from exercise3 import get_all_rows_from_table 


class TestExercise3(unittest.TestCase):
    def setUp(self):
        self.db_credentials = {
            'dbname': 'testdb', 'user': 'testuser', 'password': 'secret', 'host': 'localhost', 'port': '5432'
        }
    
    @patch('exercise3.psycopg2.connect')
    def test_successful_retrieval(self, mock_psycopg2_connect):
        table_name = 'test_table'

        mock_cur = MagicMock()
        mock_cur.fetchall.return_value = [('Row1',1), ('Row2',2)]
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cur
        mock_psycopg2_connect.return_value = mock_conn

        rows = get_all_rows_from_table(self.db_credentials, table_name)

        mock_psycopg2_connect.assert_called_once_with(**self.db_credentials)
        mock_cur.execute.assert_called_once_with('SELECT * FROM %s', (table_name,))
        self.assertEqual(rows, [('Row1',1), ('Row2',2)])

    
    @patch('exercise3.psycopg2.connect')
    def test_tabel_does_not_exist(self, mock_psycopg2_connect):
        table_name = 'test_table2'

        mock_cur = MagicMock()
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cur
        mock_psycopg2_connect.return_value = mock_conn

        result = get_all_rows_from_table(self.db_credentials, table_name)

        self.assertIsNone(result)


    @patch('exercise3.psycopg2.connect')
    @patch('builtins.print')
    def test_invalid_credentials(self, mock_print, mock_psycopg2_connect):
        self.db_credentials['password'] = 'wrong_password'
        table_name = 'test_table'

        expected_error_message = f'FATAL: password authentication failed for user "{self.db_credentials["user"]}"'
        mock_psycopg2_connect.side_effect = psycopg2.OperationalError(expected_error_message)

        result = get_all_rows_from_table(self.db_credentials, table_name)
        
        self.assertIsNone(result)
        mock_print.assert_called_with(f'Error: {expected_error_message}')


    @patch('exercise3.psycopg2.connect')
    def test_empty_result_set(self, mock_psycopg2_connect):
        table_name = 'test_table'

        mock_cur = MagicMock()
        mock_cur.fetchall.return_value = []
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cur
        mock_psycopg2_connect.return_value = mock_conn
        result = get_all_rows_from_table(self.db_credentials, table_name)

        self.assertEqual(result, [])


    @patch('exercise3.psycopg2.connect')
    def test_database_connection_error(self, mock_psycopg2_connect):
        table_name = 'test_table'

        mock_psycopg2_connect.side_effect = psycopg2.errors.ConnectionFailure('database connection failed')

        result = get_all_rows_from_table(self.db_credentials, table_name)
        
        self.assertIsNone(result)


    @patch('exercise3.psycopg2.connect')
    def test_query_execution_failure(self, mock_psycopg2_connect):
        table_name = 'test_table'

        mock_cur = MagicMock()
        mock_cur.execute.side_effect = psycopg2.errors.IntegrityError('query execution failed')
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cur
        mock_psycopg2_connect.return_value = mock_conn

        result = get_all_rows_from_table(self.db_credentials, table_name)

        self.assertIsNone(result)


    @patch('exercise3.psycopg2.connect')
    def test_timeout_error(self, mock_psycopg2_connect):
        table_name = 'test_table'

        mock_psycopg2_connect.side_effect = psycopg2.OperationalError('database connection timeout')

        result = get_all_rows_from_table(self.db_credentials, table_name)
        
        self.assertIsNone(result)


    @patch('exercise3.psycopg2.connect')
    def test_handling_sql_injection(self, mock_psycopg2_connect):
        table_name = 'users; DROP TABLE users; --'

        mock_cur = MagicMock()
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cur
        mock_psycopg2_connect.return_value = mock_conn

        result = get_all_rows_from_table(self.db_credentials, table_name)

        mock_cur.execute.assert_not_called()
        self.assertIsNone(result)


    @patch('exercise3.psycopg2.connect')
    def test_large_data_retrieval(self, mock_psycopg2_connect):
        table_name = 'test_table'

        mock_cur = MagicMock()
        mock_cur.fetchall.return_value = [(f'Row{index}',index) for index in range(100_000)]
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cur
        mock_psycopg2_connect.return_value = mock_conn

        rows = get_all_rows_from_table(self.db_credentials, table_name)

        self.assertEqual(rows, [(f'Row{index}',index) for index in range(100_000)])

    @patch('exercise3.psycopg2.connect')
    def test_schema_specific_access(self, mock_psycopg2_connect):
        table_name_with_schema = 'public.test_table'
        table_name = 'test_table'

        mock_cur = MagicMock()
        mock_cur.fetchall.return_value = [('Row1',1), ('Row2',2)]
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cur
        mock_psycopg2_connect.return_value = mock_conn

        rows = get_all_rows_from_table(self.db_credentials, table_name_with_schema)

        self.assertEqual(rows, [('Row1',1), ('Row2',2)])
        mock_cur.execute.assert_called_once_with('SELECT * FROM %s', (table_name,))

if __name__ == '__main__':
    unittest.main()