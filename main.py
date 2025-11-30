import requests

base_url = "https://pokeapi.co/api/v2"

def get_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        print("data retrieved")
        data = response.json()
        print(data["abilities"].name)
    else:
        print(f"failed to fetch data {response.status_code}")

get_info("charmander")
import random
# Generate a larger dataset with 100 random integers between 1 and 999
large_dataset = [random.randint(1, 999) for _ in range(100)]

# sorting algorithm
def sorting(list):
    if len(list) <= 1:
        return list
    mid_of_list = len(list)//2
    left_hand = sorting(list[mid_of_list:])
    right_hand = sorting(list[:mid_of_list])
    return merge_sorted(left_hand, right_hand)

# function to merge the sorted element
def merge_sorted(coll1, coll2):
    merged_element = []
    left_index = 0
    right_index = 0
    while left_index < len(coll1) and right_index < len(coll2):
        if coll1[left_index] < coll2[right_index]:
           merged_element.append(coll1[left_index]) 
           left_index+=1
        else:
            merged_element.append(coll2[right_index]) 
            right_index+=1
    while left_index < len(coll1):
        merged_element.append(coll1[left_index])
        left_index +=1
    while right_index < len(coll2):
        merged_element.append(coll2[right_index])
        right_index +=1
    return merged_element

print(sorting(large_dataset))

