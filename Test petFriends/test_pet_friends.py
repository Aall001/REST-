import os.path

from api import PetFriends
from settings import valid_email, valid_password

df = PetFriends()


def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    """Проверяем что запрос апи ключа возвращает статус 200 и в результате содержит слово 'key' """
    status, result = df.get_api_key(email, password)
    assert  status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter = ''):
    """Проверяем, что на запрос всех питомцев возвращает не пустой список.
    для этого сначала возвращаем арi ключ и сохраняем его в переменную auth_key
    Затем используя этот ключ запрашиваем список, и проверяем, что он не пустой
    Доступное значение параметра filter - 'my_pets' либо '' """
    _, auth_key = df.get_api_key(valid_email, valid_password)
    status, result = df.get_list_of_pets(auth_key,filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_post_add_new_pet_with_valid_data(name= 'Барсик', animal_type= "Чудо", age= "5", pet_photo= "images/pet_photo1.jpeg"):
    """Проверяем, что можно добавить питомца с корректными данными """

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = df.get_api_key(valid_email,valid_password)
    status, result = df.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_delete_pet_by_valid_id():
    """Проверяем возможность удалять питомца по id"""

    _, auth_key = df.get_api_key(valid_email, valid_password)
    _, my_pets = df.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) == 0:
        df.post_add_new_pet(auth_key, 'Виталик', 'лось', "2", "image/opisanie_lva.jpeg")
        _, my_pets = df.get_list_of_pets(auth_key,'my_pets')

    pet_id = my_pets['pets'][0]['id']
    status, _ = df.delete_pet_from_database(auth_key,pet_id)

    _, my_pets = df.get_list_of_pets(auth_key, 'my_pets')

    status, result = df.delete_pet_from_database(auth_key, pet_id)
    assert status == 200
    assert pet_id not in my_pets.values()


def test_update_information_about_pet_valid_values(name = 'Кокки', animal_type = 'цыпленок', age = '1'):
    """Проверка, можно ли изменять данные своих питомцев"""

    _, auth_key = df.get_api_key(valid_email, valid_password)
    _, my_pets = df.get_list_of_pets(auth_key,'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = df.update_information_about_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception('There is no my pets')




