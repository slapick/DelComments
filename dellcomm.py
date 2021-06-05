import vk_api, json

with open('config.json', 'r', encoding = "utf-8") as f:
    data = json.load(f)

access_token = str(data["token"])
user_iddd = str(data["user_id"])
post_iddd = str(data["post_id"])
number_of_comm = int(data["comment_number"])

id_s = [0]
if bool(data["del_all"]):
	pass
else:
	id_s = data["ids"]

vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()

def main():
	for i in range(number_of_comm + 1):
		try:
			comm = vk.wall.getComment(owner_id=user_iddd, post_id = post_iddd, count='1', sort='asc', comment_id = i, v=5.124)
			comm = comm['items'][0]
			print(f"From id: {comm['from_id']}, Text: {comm['text']}")
			if comm['from_id'] in id_s or id_s[0] == 0:
				delcomm = vk.wall.deleteComment(owner_id=user_iddd, comment_id = i , v=5.124)
				print(f"Del: {i}")
		except Exception as e:
			print(f"Error: {repr(e)}, возможно комментария уже не существует (id: {i})")

if __name__ == "__main__":
	main()