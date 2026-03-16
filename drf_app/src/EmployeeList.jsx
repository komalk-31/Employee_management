import React, { useEffect, useState } from "react";
import API from "./api";

export default function EmployeeList() {

    const [employees, setEmployees] = useState([]);

    useEffect(() => {
        getEmployees();
    }, []);

    const getEmployees = async () => {
        const response = await API.get("employeeList/");
        setEmployees(response.data);
    };

    return (
        <div>

            <h2>Employee List</h2>

            <ul>
                {employees.map(emp => (
                    <li key={emp.id}>
                        {emp.name} - {emp.salary}
                    </li>
                ))}

            </ul>

        </div>
    );
}