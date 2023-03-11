import requests
import time

# resp = requests.post('http://127.0.0.1:5000/upscale', files={
#     'files': open('lama_300px.png', 'rb')
# })
# resp_data = resp.json()
# print(resp_data)
# task_id = resp_data.get('task_id')
# print(task_id)
#
# while True:
#     resp = requests.get(f'http://127.0.0.1:5000/tasks/{task_id}')
#     print(resp.json())
#     time.sleep(10)
#     if resp.json()['status'] == 'SUCCESS':
#         print('task done')
#         break

path_out = 'files/38134f27-8741-4ebf-947b-ef2710e4cdf4_out.png'
output_file = '38134f27-8741-4ebf-947b-ef2710e4cdf4_out.png'
resp_file = requests.get(f'http://127.0.0.1:5000/processed/{output_file}')
print(resp_file.status_code)
print(resp_file.json())

