# test_performance.py
import time
from django.test import TestCase
from app_courses.models import Course

class TestPerformance(TestCase):
    def test_query_performance(self):
        start_time = time.time()
        queryset = Course.objects.all()
        # Дополнительные операции с вашим queryset, если необходимо
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения запроса: {execution_time} секунд")
        # Проверьте, что время выполнения не превышает определенного порога
        assert execution_time < 1.0  # Например, порог 1.0 секунды

def test_addition():
    assert 1 + 1 == 2