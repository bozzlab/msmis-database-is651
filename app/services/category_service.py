from sqlalchemy.orm import Session

from app.constants.category_type import CategoryType
from app.models.models import IncomeCategories, ExpenseCategories
from app.schemas.category import CategoryResponse, BaseCategoryResponse

CATEGORY_TYPE_MODEL_MAP = {
    CategoryType.INCOME: IncomeCategories,
    CategoryType.EXPENSE: ExpenseCategories,
}


class CategoryService:
    def __init__(self, db_session: Session) -> None:
        self.db = db_session

    def get_categories(
        self, user_id: int, category_types: list[CategoryType] = list(CategoryType)
    ) -> CategoryResponse:
        response = CategoryResponse(income=[], expense=[])

        for category_type in category_types:
            model = CATEGORY_TYPE_MODEL_MAP.get(category_type)
            db_categories = self.db.query(model).filter(model.user_id == user_id).all()

            if db_categories:
                for db_category in db_categories:
                    setattr(
                        response,
                        category_type.value.lower(),
                        [
                            BaseCategoryResponse.from_orm(db_category)
                            for db_category in db_categories
                        ],
                    )

        return response
