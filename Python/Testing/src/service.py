from typing import Dict, List, Optional, Union


DB = {
    1: {'employee_id': 1, 'employee_name': 'Employee1', 'employee_type': 'Full Time'},
    2: {'employee_id': 2, 'employee_name': 'Employee2', 'employee_type': 'Full Time'},
    3: {'employee_id': 3, 'employee_name': 'Employee3', 'employee_type': 'Intern'}
}


class Employee:

    __BASE_SALARY: int = 150000

    def __init__(self, employee_id: int, employee_name: str, employee_type: str) -> None:
        self.employee_id: int = employee_id
        self.__employee_name: str = employee_name
        self.__employee_type: str = employee_type

    @classmethod
    def get_base_salary(cls) -> int:
        return cls.__BASE_SALARY

    def get_employee_id(self) -> int:
        return self.employee_id

    def get_employee_name(self) -> str:
        return self.__employee_name

    def get_employee_type(self) -> str:
        return self.__employee_type

    def get_employee_salary(self) -> float:
        base_salary: int = self.__class__.get_base_salary()
        return float(base_salary) if self.__employee_type == 'Intern' else float(base_salary * 1.5)


class DBService:

    @classmethod
    def get_employee(cls, employee_id: int) -> Optional[Employee]:
        global DB

        employee: Dict[str, Union[int, str]] = DB.get(employee_id, None)
        return Employee(employee_id=employee.get('employee_id'),
                        employee_name=employee.get('employee_name'),
                        employee_type=employee.get('employee_type')) if employee is not None else None

    @classmethod
    def get_all_employees(cls) -> List[Employee]:
        employees: List[Employee] = list()
        employee_id: int
        employee_details: Dict[str, Union[int, str]]
        for employee_id, employee_details in DB.items():
            employees.append(Employee(employee_id=employee_id,
                                      employee_name=employee_details.get('employee_name'),
                                      employee_type=employee_details.get('employee_type')))
        return employees


# client
def client() -> None:
    employee_1: Optional[Employee] = DBService.get_employee(employee_id=1)
    print(f'Employee Details:'
          f' {employee_1.get_employee_id()} {employee_1.get_employee_name()}'
          f' {employee_1.get_employee_type()} {employee_1.get_employee_salary()}')
