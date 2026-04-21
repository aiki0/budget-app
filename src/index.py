from database.database_connection import get_database_connection
from repositories.budget_repository import BudgetRepository
from services.budget_service import BudgetService
from ui.ui import start_ui

def main():

    connection = get_database_connection()
    repository = BudgetRepository(connection)
    service = BudgetService(repository)
    start_ui(service)

if __name__ == "__main__":
    main()
