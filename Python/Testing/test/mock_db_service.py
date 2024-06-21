from src.service import Employee, DBService
from unittest.mock import Mock, patch
from typing import Callable


class TestDBService:

    """Mocks src.service.DBService"""

    @classmethod
    @patch('src.service.DBService.get_employee')
    def test_get_employee(cls, mocked_get_employee: Callable) -> None:

        mock_employee: Mock = Mock()
        mock_employee.employee_id = 1234
        mock_employee.get_employee_id.return_value = mock_employee.employee_id
        mock_employee.get_employee_name.return_value = 'MockEmployee'
        mock_employee.get_employee_type.return_value = 'Full Time'
        mock_employee.get_employee_salary.return_value = 1.5 * Employee.get_base_salary()

        mocked_get_employee.return_value = mock_employee

        employee: Employee = DBService.get_employee(employee_id=1)
        print(f'Employee Details:'
              f' {employee.get_employee_id()} {employee.get_employee_name()}'
              f' {employee.get_employee_type()} {employee.get_employee_salary()}')
        if employee.get_employee_type() == 'Full Time':
            assert employee.get_employee_salary() == 1.5 * Employee.get_base_salary()
        else:
            assert employee.get_employee_salary() == Employee.get_base_salary()

    @classmethod
    @patch('src.service.DBService.get_all_employees')
    def test_get_all_employees(cls, mocked_get_all_employees) -> None:

        full_time_employee_mock: Mock = Mock()
        full_time_employee_mock.employee_id = 1234
        full_time_employee_mock.get_employee_id.return_value = full_time_employee_mock.employee_id
        full_time_employee_mock.get_employee_name.return_value = 'FullTimeMockEmployee'
        full_time_employee_mock.get_employee_type.return_value = 'Full Time'
        full_time_employee_mock.get_employee_salary.return_value = 1.5 * Employee.get_base_salary()

        intern_employee_mock: Mock = Mock()
        intern_employee_mock.employee_id = 12345
        intern_employee_mock.get_employee_id.return_value = intern_employee_mock.employee_id
        intern_employee_mock.get_employee_name.return_value = 'InternMockEmployee'
        intern_employee_mock.get_employee_type.return_value = 'Intern'
        intern_employee_mock.get_employee_salary.return_value = Employee.get_base_salary()

        mocked_get_all_employees.return_value = [full_time_employee_mock, intern_employee_mock]

        employee: Employee
        for employee in DBService.get_all_employees():
            print(f'Checking Employee -> {employee.get_employee_name()} {employee.get_employee_salary()}')
            assert employee.get_employee_salary() == 1.5 * Employee.get_base_salary() if employee.get_employee_type() == 'Full Time' else employee.get_employee_salary() == float(Employee.get_base_salary())
