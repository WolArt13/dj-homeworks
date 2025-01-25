import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student

@pytest.fixture
def client():
    return APIClient()
    
@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    
    return factory
    
@pytest.mark.django_db
def test_get_course(client, course_factory, student_factory):
    students = student_factory(_quantity=3)
    courses = course_factory(_quantity=1)
    courses[0].students.set(students)
    
    url = '/api/v1/courses/'
    responce = client.get(url)
    
    assert responce.status_code == 200
    assert len(responce.data) == 1
    assert responce.data[0]['students'] == [student.id for student in students]
    assert responce.data[0]['id'] == courses[0].id
    assert responce.data[0]['name'] == courses[0].name

@pytest.mark.django_db
def test_get_courses_list(client, course_factory, student_factory):
    students = student_factory(_quantity=3)
    courses = course_factory(_quantity=5)
    for course in courses:
        course.students.set(students)
    
    url = '/api/v1/courses/'
    responce = client.get(url)
    print(responce.data)
    
    assert responce.status_code == 200
    assert len(responce.data) == 5
    for i, course in enumerate(responce.data):
        assert course['students'] == [student.id for student in students]
        assert course['id'] == courses[i].id
        assert course['name'] == courses[i].name

@pytest.mark.django_db
def test_course_filter_id(client, course_factory):
    courses = course_factory(_quantity=5)
    
    url = '/api/v1/courses/?id={}'.format(courses[3].id)
    responce = client.get(url)
    
    assert responce.status_code == 200
    assert len(responce.data) == 1
    assert responce.data[0]['id'] == courses[3].id

@pytest.mark.django_db
def test_course_filter_name(client, course_factory):
    courses = course_factory(_quantity=5)
    
    
    url = '/api/v1/courses/?name={}'.format(courses[3].name)
    responce = client.get(url)
    
    assert responce.status_code == 200
    assert len(responce.data) == 1
    assert responce.data[0]['name'] == courses[3].name
    
@pytest.mark.django_db
def test_course_create(client, student_factory):
    students = student_factory(_quantity=3)
    data = {
        'name': 'Test Course',
        'students': [student.id for student in students]
    }
    
    url = '/api/v1/courses/'
    responce = client.post(url, data=data)
    
    assert responce.status_code == 201
    assert responce.data['name'] == data['name']
    assert len(responce.data['students']) == len(data['students'])
    assert set(responce.data['students']) == set(data['students'])

@pytest.mark.django_db
def test_course_update(client, course_factory, student_factory):
    courses = course_factory(_quantity=3)
    new_data = {
        'name': 'Updated Test Course',
        'students': []
    }
    
    url = '/api/v1/courses/{}/'.format(courses[1].id)
    responce = client.put(url, data=new_data)
    
    assert responce.status_code == 200
    assert responce.data['name'] == new_data['name'] and responce.data['name']!= courses[1].name
    
@pytest.mark.django_db
def test_course_delete(client, course_factory):
    courses = course_factory(_quantity=3)
    
    url = '/api/v1/courses/{}/'.format(courses[1].id)
    responce = client.delete(url)
    
    assert responce.status_code == 204